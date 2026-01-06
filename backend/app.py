from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import tempfile
from werkzeug.utils import secure_filename
from resume_enhancer import ResumeEnhancer

app = Flask(__name__)

# CORS configuration - allow your domain
allowed_origins = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000,https://buildcustomresume.com,https://www.buildcustomresume.com').split(',')
# Remove empty strings from origins list
allowed_origins = [origin.strip() for origin in allowed_origins if origin.strip()]

# Configure CORS - Simple and permissive for now to debug
if allowed_origins and allowed_origins != ['*']:
    CORS(app, 
         resources={
             r"/api/*": {
                 "origins": allowed_origins,
                 "methods": ["GET", "POST", "OPTIONS", "PUT", "DELETE"],
                 "allow_headers": ["Content-Type", "Authorization", "X-Requested-With"],
                 "supports_credentials": True,
                 "max_age": 3600
             }
         })
else:
    # Allow all origins if not specified (for debugging)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configuration
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 10 * 1024 * 1024))  # 10MB default

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@app.route('/api/routes', methods=['GET'])
def list_routes():
    """Debug endpoint to list all registered routes"""
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify({'routes': routes}), 200

@app.route('/api/test', methods=['GET', 'POST', 'OPTIONS'])
def test_endpoint():
    """Test endpoint to verify routing works"""
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok', 'method': 'OPTIONS'}), 200
    return jsonify({
        'status': 'ok',
        'method': request.method,
        'headers': dict(request.headers),
        'cors_configured': True
    }), 200

@app.route('/api/enhance-resume', methods=['POST', 'OPTIONS'])
@app.route('/api/enhance-resume/', methods=['POST', 'OPTIONS'])  # Handle trailing slash
def enhance_resume():
    # Log the request for debugging
    print(f"Request received: {request.method} {request.path}")
    print(f"Headers: {dict(request.headers)}")
    
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        print("Handling OPTIONS request")
        response = jsonify({'status': 'ok', 'message': 'CORS preflight successful'})
        return response
    
    try:
        # Check if files are present
        if 'resume' not in request.files:
            return jsonify({'error': 'No resume file provided'}), 400
        
        resume_file = request.files['resume']
        job_posting = request.form.get('job_posting', '')
        
        if resume_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not job_posting:
            return jsonify({'error': 'Job posting is required'}), 400
        
        if not allowed_file(resume_file.filename):
            return jsonify({'error': 'Invalid file type. Only PDF, DOC, and DOCX are allowed'}), 400
        
        # Save uploaded file
        filename = secure_filename(resume_file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        resume_file.save(filepath)
        
        # Initialize enhancer and process
        enhancer = ResumeEnhancer()
        output_format = request.form.get('output_format', 'pdf').lower()
        
        enhanced_resume_path = enhancer.enhance_resume(
            resume_path=filepath,
            job_posting=job_posting,
            output_format=output_format
        )
        
        # Clean up uploaded file
        os.remove(filepath)
        
        # Send enhanced resume
        return send_file(
            enhanced_resume_path,
            as_attachment=True,
            download_name=f'enhanced_resume.{output_format}',
            mimetype='application/pdf' if output_format == 'pdf' else 'application/msword'
        )
    
    except Exception as e:
        # Log the error for debugging
        import traceback
        error_trace = traceback.format_exc()
        print(f"Error in enhance_resume: {str(e)}")
        print(f"Traceback: {error_trace}")
        
        # Clean up on error
        if 'filepath' in locals() and os.path.exists(filepath):
            try:
                os.remove(filepath)
            except:
                pass
        if 'enhanced_resume_path' in locals() and os.path.exists(enhanced_resume_path):
            try:
                os.remove(enhanced_resume_path)
            except:
                pass
        
        # Return user-friendly error message
        error_message = str(e)
        # Don't expose internal errors in production, but log them
        if os.getenv('FLASK_ENV') == 'production':
            # In production, provide generic message but log details
            return jsonify({'error': 'An error occurred while processing your resume. Please try again or contact support.'}), 500
        else:
            # In development, show full error
            return jsonify({'error': error_message, 'traceback': error_trace}), 500

# Add error handler for 405
@app.errorhandler(405)
def method_not_allowed(e):
    print(f"405 Error: Method {request.method} not allowed for {request.path}")
    print(f"Request URL: {request.url}")
    print(f"Request method: {request.method}")
    
    # Get all routes for this path
    matching_routes = []
    for rule in app.url_map.iter_rules():
        if str(rule) == request.path or str(rule) == request.path.rstrip('/'):
            matching_routes.append({
                'path': str(rule),
                'methods': list(rule.methods)
            })
    
    return jsonify({
        'error': f'Method {request.method} not allowed',
        'path': request.path,
        'request_method': request.method,
        'matching_routes': matching_routes,
        'message': 'Please use POST method to enhance resume',
        'allowed_methods': ['POST', 'OPTIONS']
    }), 405

if __name__ == '__main__':
    # Development mode
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
