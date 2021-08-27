import sys
from cx_Freeze import setup, Executable
from cx_Freeze.dist import build

build_exe_options = {"packages":["os"],
                     "includes":["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
setup(
    name = "Transcribe",
    version = "0.1",
    description = "Ele transcreve vídeos",
    options = {"build_exe": build_exe_options},
    executables = [Executable("interface.py", base=base)]
)