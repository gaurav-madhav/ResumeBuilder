#!/bin/bash
# Start script for backend
# This ensures we're in the right directory and start gunicorn correctly

cd "$(dirname "$0")"
exec gunicorn app:app --bind 0.0.0.0:${PORT:-5000} --workers 2 --timeout 120

