# Content Downloader Suite

A Python project with a GUI for downloading video content. This app provides an easy-to-use interface to download various video types.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/tomonoafentiko/your-repo-name.git
   cd your-repo-name
   
2. Create and activate a virtual environment:
python -m venv .venv
# On Windows PowerShell
.\.venv\Scripts\Activate.ps1
# On Windows CMD
.\.venv\Scripts\activate.bat
# On macOS/Linux
source .venv/bin/activate


3. Install the required dependencies:
pip install -r requirements.txt

4. Run the application:
python main.py
5. To build a standalone executable with PyInstaller, run:
pyinstaller --onefile --hidden-import=_tkinter gui.py

Please note that you may need to ensure that Tcl/Tk DLLs required by Tkinter are available on your system for the executable to work properly.
You might need to customize the PyInstaller .spec file to include additional binaries or DLLs depending on your environment.

CONTACT:

Panji Mwale | +260967167916, +260971854854 | panjimwaletomonoafentiko@gmail.com