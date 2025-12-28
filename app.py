"""
Ubuntu Initiative Website - Flask Application
==============================================
This serves the website from the 'public' folder.

To customize the website:
- Edit HTML files in the 'public/' folder
- Edit styles in 'public/css/style.css'
- Add your images to 'public/images/' folder
"""

from flask import Flask, send_from_directory, request, redirect
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')
app.secret_key = os.environ.get('SESSION_SECRET', 'ubuntu-initiative-secret-key')

# ============================================
# ROUTES - Serve HTML files from public folder
# ============================================

@app.route('/')
def home():
    """Home page"""
    return send_from_directory('public', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    """Serve any file from public folder"""
    return send_from_directory('public', path)

# ============================================
# RUN THE APPLICATION
# ============================================

if __name__ == '__main__':
    print("Ubuntu Initiative Website running at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
