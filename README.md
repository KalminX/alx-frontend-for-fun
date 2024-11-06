# Markdown to HTML Converter

This project is a Python-based converter that transforms Markdown files into HTML, simulating how GitHub renders README files as HTML. Created as part of the ALX program, it’s a practical exercise in handling Markdown content programmatically.

## Features
- Converts standard Markdown syntax to HTML.
- Validates input arguments and file existence, providing clear error messages.
- Exits cleanly with appropriate status codes based on input validity.

## Requirements
1. **Argument Validation**:
   - If the number of arguments is less than 2, the program will:
     - Print an error to STDERR: `Usage: ./markdown2html.py README.md README.html`
     - Exit with status code `1`.
2. **File Existence**:
   - If the specified Markdown file does not exist, the program will:
     - Print an error to STDERR: `Missing <filename>`
     - Exit with status code `1`.
3. **Successful Execution**:
   - If the input is valid and the Markdown file exists, the program will:
     - Convert the Markdown file to HTML.
     - Print nothing and exit with status code `0`.

## Installation

To use this project:
1. Clone the repository:
   ```bash
   git clone https://github.com/KalminX/alx-frontend-for-fun.git
