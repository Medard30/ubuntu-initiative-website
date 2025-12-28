UBUNTU INITIATIVE WEBSITE - LOCAL SETUP
========================================

OPTION 1: Simple Preview (No Python needed)
--------------------------------------------
1. Open VS Code
2. Install "Live Server" extension
3. Right-click on public/index.html and select "Open with Live Server"
4. The website will open in your browser

OPTION 2: Run with Python/Flask
-------------------------------
1. Install Python dependencies:
   pip install -r requirements.txt

2. Run the app:
   python app.py

3. Open http://localhost:5000 in your browser

Note: Contact/Volunteer forms require a database connection.
For local testing without database, the forms won't save data.

EDITING THE WEBSITE
-------------------
- Edit HTML files in public/ folder to change content
- Edit public/css/style.css to change colors and styling
- Replace images in public/images/ folder with your own
- Look for "EDIT" comments in HTML files for guidance

TO ADD YOUR GOFUNDME LINK
-------------------------
1. Open public/index.html
2. Find the "Donate Now" button (search for "GoFundMe")
3. Replace the "#" with your GoFundMe campaign URL

FOLDER STRUCTURE
----------------
public/
  index.html          - Home page
  about.html          - About Us page
  programs.html       - Programs page
  impact.html         - Impact page
  gallery.html        - Photo gallery
  get-involved.html   - Volunteer signup
  contact.html        - Contact form
  css/
    style.css         - All styling
  images/             - All photos
