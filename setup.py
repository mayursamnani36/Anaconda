import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\owner\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\owner\AppData\Local\Programs\Python\Python37\tcl\tk8.6'
executables = [cx_Freeze.Executable("first.py")]
cx_Freeze.setup(
    name="Anaconda",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["apple.png", "snakehead.png"]}},

    description="Anaconda Game Tutorials",
    executables=executables

)
