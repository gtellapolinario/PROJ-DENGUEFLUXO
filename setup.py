"""   import cxfreeze  # Import the sys module for system-specific parameters and functions."""
from cx_Freeze import setup, Executable

build_options = {"packages": ["tkinter", "datetime"]}

import sys
base = 'Win32Gui' if sys.platform== 'win32' else None

executables = [Executable("FluxoDengue 1.0.py", base=base, icon="dg.ico")]

setup(
    name="FluxoDengue 1.0",
    version="1.0",
    description="Fluxo Dengue",
    options={"build_exe": build_options},
    executables=executables
)
