"""
Main entry point for platforms that auto-detect main.py
This file imports the Flask app from app.py
"""
from app import app

if __name__ == "__main__":
    app.run()

