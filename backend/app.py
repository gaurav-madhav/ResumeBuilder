from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import tempfile
from werkzeug.utils import secure_filename
from resume_enhancer import ResumeEnhancer

app = Flask(__name__)

# CORS configuration - allow your domain
allowed_origins = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000,https://buildcustomresume.com,https://www.buildcustomresume.com').split(',')
CORS(app, origins=allowed_origins)

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

@app.route('/api/enhance-resume', methods=['POST'])
def enhance_resume():
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
        # Note: Temporary files in temp_dir will be cleaned up by the OS
        # For production, consider implementing a cleanup job
        return send_file(
            enhanced_resume_path,
            as_attachment=True,
            download_name=f'enhanced_resume.{output_format}',
            mimetype='application/pdf' if output_format == 'pdf' else 'application/msword'
        )
    
    except Exception as e:
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
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Development mode
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)

