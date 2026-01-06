# Build Instructions

This guide explains how to build the Resume Builder application for production.

## Frontend Build

### Development Build (for testing)

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies (if not already done):
```bash
npm install
```

3. Build for production:
```bash
# For local testing (uses localhost API)
npm run build

# For production (uses production API URL)
REACT_APP_API_URL=https://api.buildcustomresume.com npm run build
```

4. The build output will be in `frontend/build/` directory

### Production Build

For deployment, you'll typically set the API URL as an environment variable in your hosting platform. The build command will use that variable:

```bash
npm run build
```

The build process will:
- Optimize and minify JavaScript
- Optimize CSS
- Create production-ready static files
- Output to `frontend/build/` directory

## Backend Build

The backend doesn't require a traditional "build" step, but you need to:

1. Install dependencies:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. For production, use gunicorn:
```bash
gunicorn --config gunicorn_config.py wsgi:app
```

## Testing Production Build Locally

### Test Frontend Build Locally

1. Build the frontend:
```bash
cd frontend
REACT_APP_API_URL=http://localhost:5000 npm run build
```

2. Install a simple HTTP server:
```bash
npm install -g serve
```

3. Serve the build:
```bash
serve -s build -l 3000
```

4. In another terminal, start the backend:
```bash
cd backend
source venv/bin/activate
python app.py
```

5. Visit http://localhost:3000 to test

### Alternative: Use Python's HTTP Server

```bash
cd frontend/build
python3 -m http.server 3000
```

## Build Scripts

You can also use the provided build scripts (see below).

## Environment Variables

### Frontend
- `REACT_APP_API_URL` - Backend API URL (required for production)

### Backend
- `FLASK_ENV` - Set to `production` for production
- `ALLOWED_ORIGINS` - Comma-separated list of allowed origins
- `PORT` - Port number (default: 5000)

## Production Checklist

Before deploying:
- [ ] Frontend builds without errors
- [ ] Backend dependencies installed
- [ ] Environment variables set correctly
- [ ] Test production build locally
- [ ] Verify API connectivity
- [ ] Check file upload functionality
- [ ] Test resume enhancement
- [ ] Verify download works

