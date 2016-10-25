from cx_Freeze import setup, Executable

setup(
    name="PDV",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("pdv_main.py")])