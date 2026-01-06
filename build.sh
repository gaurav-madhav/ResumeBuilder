#!/bin/bash

# Build script for Resume Builder
# This script builds both frontend and backend for production

set -e  # Exit on error

echo "=========================================="
echo "Building Resume Builder for Production"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if API URL is provided
if [ -z "$REACT_APP_API_URL" ]; then
    echo -e "${BLUE}Note: REACT_APP_API_URL not set. Using default (localhost:5000)${NC}"
    echo "Set REACT_APP_API_URL environment variable for production build"
    echo "Example: REACT_APP_API_URL=https://api.buildcustomresume.com ./build.sh"
    echo ""
    REACT_APP_API_URL="http://localhost:5000"
fi

# Build Frontend
echo -e "${GREEN}Building Frontend...${NC}"
cd frontend

if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

echo "Building React app..."
REACT_APP_API_URL=$REACT_APP_API_URL npm run build

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Frontend build successful!${NC}"
    echo "Build output: frontend/build/"
else
    echo "✗ Frontend build failed!"
    exit 1
fi

cd ..

# Prepare Backend
echo ""
echo -e "${GREEN}Preparing Backend...${NC}"
cd backend

if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing/updating backend dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Backend dependencies installed!${NC}"
else
    echo "✗ Backend setup failed!"
    exit 1
fi

cd ..

echo ""
echo "=========================================="
echo -e "${GREEN}Build Complete!${NC}"
echo "=========================================="
echo ""
echo "Frontend build: frontend/build/"
echo "Backend ready: backend/"
echo ""
echo "To test locally:"
echo "  1. Start backend: cd backend && source venv/bin/activate && python app.py"
echo "  2. Serve frontend: cd frontend && npx serve -s build -l 3000"
echo ""

