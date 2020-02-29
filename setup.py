import os
import sys
import speech_recognition as sr
from cx_Freeze import setup, Executable

base = None
if(sys.platform == "win32"):
    base = "Win32GUI"

executables = {
    Executable("Automatização.py", base = base)
}

buildOptions = dict (
    packages = [],
    includes = ["os", "sys", "speech_recognition"],
    include_files = ["destinos.txt", "tarefas.txt"],
    excludes = []
)

setup(
    name = "Automatico",
    version = "1.0",
    description = "Teste01",
    options = dict(build_exe = buildOptions),
    executables = executables
)