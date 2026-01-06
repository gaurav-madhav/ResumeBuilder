# Resume Builder

A full-stack web application that enhances resumes by analyzing job postings and adding relevant keywords. Built with Python (Flask) backend and React frontend.

## Features

- Upload resumes in PDF, DOC, or DOCX format
- Input job posting or key responsibilities
- Automatic keyword extraction and resume enhancement
- Download enhanced resume in PDF or DOCX format
- Modern, responsive UI

## Project Structure

```
ResumeBuilder/
├── backend/
│   ├── app.py                 # Flask application
│   ├── resume_enhancer.py     # Resume processing logic
│   ├── requirements.txt       # Python dependencies
│   └── uploads/               # Temporary upload directory
└── frontend/
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── App.js             # Main React component
    │   ├── App.css            # Styles
    │   ├── index.js           # React entry point
    │   └── index.css          # Global styles
    └── package.json           # Node dependencies
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Flask server:
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The frontend will run on `http://localhost:3000`

## Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Upload your resume (PDF, DOC, or DOCX)
3. Paste the job posting or key responsibilities
4. Select your preferred output format (PDF or DOCX)
5. Click "Enhance Resume"
6. Your enhanced resume will be automatically downloaded

## API Endpoints

- `GET /api/health` - Health check endpoint
- `POST /api/enhance-resume` - Enhance resume endpoint
  - Form data:
    - `resume`: Resume file (PDF, DOC, or DOCX)
    - `job_posting`: Job posting text
    - `output_format`: Output format (pdf or docx)

## Technologies Used

### Backend
- Flask - Web framework
- PyPDF2 - PDF processing
- python-docx - DOCX processing
- reportlab - PDF generation
- flask-cors - CORS handling

### Frontend
- React - UI framework
- Axios - HTTP client
- CSS3 - Styling

## Notes

- The application uses temporary files for processing
- Uploaded files are automatically cleaned up after processing
- For production use, consider adding:
  - Authentication/authorization
  - Rate limiting
  - Better error handling
  - More sophisticated NLP for keyword matching
  - Database for storing user sessions
  - File size limits and validation

## Deployment

This application is configured for deployment to `buildcustomresume.com`. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions and [NAMECHEAP_DNS_SETUP.md](NAMECHEAP_DNS_SETUP.md) for DNS configuration.

### Quick Deployment Options

1. **Railway + Vercel** (Recommended)
   - Backend: Railway
   - Frontend: Vercel
   - Automatic SSL included

2. **Render** (Full Stack)
   - Both backend and frontend on Render
   - Free tier available

3. **DigitalOcean App Platform**
   - Full control with good performance
   - Reasonable pricing

See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions.

## License

MIT

