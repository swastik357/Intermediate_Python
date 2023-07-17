Meme Generator:

Task: Python application to create memes using user inputs through a command line and web interface. 

Inputs: quote, author, and image.

Important File Packages: QuoteEngine(for parsing files) and MemeEngine(for creating memes)

Packages: ABC, Typing, Argparse, os, Requests, Pillow, Pandas, Flask, Subprocess, Python-docx

Usage: 
Flask Web Interface: Run python3 app.py in terminal and visit http://127.0.0.1:5000/

Command Line Interface: Run python3 meme.py in terminal with optional arguments:
--body: quote text(it's a string) 
--author: quote author(it's a string) 
--path: path to image file

Important Packages Summary:

QuoteEngine: For parsing files for information regarding quote body and quote author 
MemeEngine: For creating memes 
_data: Contains important project data like quotes and images 
tmp: Memes generated from CLI(meme.py) stored here
static: Memes generated from web interface(app.py) stored here

