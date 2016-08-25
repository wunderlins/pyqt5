# pyqt5

## OSX

### Installation
MacOS notoriously ships with old python installations. The best options so far has proven to be the macos ports system [1] (in a true unix spirit). 

The following packages are required for PyQT5:

- python27
- py27-pyqt5

1) [https://www.macports.org](https://www.macports.org)

### Usage
- use a recent python installation, I am using macports `python27` and `py27-pyqt5`
- create ui file with QTCreator
- convert it to python with `pyuic5 -x -o mainwindow.py mainwindow.ui`. `pyuic5` was installed with pyqt5. the -x flag will add a boilerplate main() function which sould be subclassed if one wants to extend the generated code
- freeze it with `/py27/bin/cxfreeze --target-name=<exename> -OO <mainfile.py>`. This will produce an OSX binary with dependencies in the same folder
- or create a dmg like: `python setup.py bdist_dmg`

### setup.py

	import sys
	from cx_Freeze import setup, Executable
	
	# Dependencies are automatically detected, but it might need fine tuning.
	#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
	build_exe_options = {
	        #"optimize": 2,
	        "packages" : ["atexit", "sip"],
	        #"excludes": ["tkinter"]
	}
	
	# GUI applications require a different base on Windows (the default is for a
	# console application).
	base = None
	if sys.platform == "win32":
	    base = "Win32GUI"
	
	setup(  name = "hello",
        version = "0.1",
        description = "Hello Work as OSX.app",
        options = {"build_exe": build_exe_options},
        executables = [Executable("mainwindow.py", base=base)])

## Windows
TBD

## Linux
TBD