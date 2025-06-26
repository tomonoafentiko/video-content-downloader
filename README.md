# 📥 Content Downloader Suite

A Python project with a GUI for downloading video content. This app provides an easy-to-use interface to download various video types with batch support and progress tracking.

---

## 🔧 Setup

### 1. Clone the repository

```bash
git clone https://github.com/tomonoafentiko.git
cd your-repo-name
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# On Windows PowerShell
.\.venv\Scripts\Activate.ps1

# On Windows CMD
.\.venv\Scripts\activate.bat

# On macOS/Linux
source .venv/bin/activate
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

### 5. Build a standalone executable (optional)

To build an executable with PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=icon.ico gui.py
```

> 📌 **Note**: You may need to ensure that Tcl/Tk DLLs required by Tkinter are available on your system for the executable to run properly. You might also need to customize the `.spec` file to include extra DLLs or resources depending on your environment.

---

## 📞 Contact

**Panji Mwale**  
📱 +260967167916, +260971854854  
📧 panjimwaletomonoafentiko@gmail.com
