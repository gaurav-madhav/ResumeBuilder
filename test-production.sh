#!/bin/bash

# Test production build locally
# This script builds and tests the production version locally

set -e

echo "=========================================="
echo "Testing Production Build Locally"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Build the application
echo -e "${BLUE}Building application...${NC}"
REACT_APP_API_URL=http://localhost:5000 ./build.sh

echo ""
echo -e "${YELLOW}Starting servers...${NC}"
echo ""

# Start backend in background
echo -e "${GREEN}Starting backend on http://localhost:5000...${NC}"
cd backend
source venv/bin/activate
python app.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Check if backend is running
if curl -s http://localhost:5000/api/health > /dev/null; then
    echo -e "${GREEN}✓ Backend is running${NC}"
else
    echo "✗ Backend failed to start"
    kill $BACKEND_PID 2>/dev/null || true
    exit 1
fi

# Start frontend server
echo -e "${GREEN}Starting frontend on http://localhost:3000...${NC}"
cd frontend

# Check if serve is installed
if ! command -v serve &> /dev/null; then
    echo "Installing 'serve' package..."
    npm install -g serve
fi

serve -s build -l 3000 &
FRONTEND_PID=$!
cd ..

echo ""
echo "=========================================="
echo -e "${GREEN}Servers Running!${NC}"
echo "=========================================="
echo ""
echo "Frontend: http://localhost:3000"
echo "Backend:  http://localhost:5000"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop both servers${NC}"
echo ""

# Wait for user interrupt
trap "echo ''; echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null || true; exit" INT
wait

