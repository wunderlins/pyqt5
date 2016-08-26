# pyqt5

This packages enables you to create a Qt% application in python and build a native binary for Windows, OSX (10.7+) and Linux.

## requirements

On all platforms:
- gnu make (gmake on OSX, make on linux by default)
- [QtStudio](https://www.qt.io/ide/), GPL Edition is free
- Python 2.7 (3.x is supoorted but not in this project)
- Qt5 (binary and header files)
- python packages: PyQt5
- PyInstaller (via pip, ports or apt)

## Workflow

- Use QtDesigner to build your user interface
- copy the UI File to this project folder
- TODO: copy ressources
- subclass the ui file to add event, see app.py for an example
- TODO: configure make file in the header to reflect the ressources name
- run `make clean` and `make <platform>`
- you should find the executable or app bundle in `dist/<platform>/$FILE_EXE`

## OSX

### Installation
MacOS notoriously ships with old python installations. The best options so far has proven to be the macos ports system [1](https://www.macports.org) (in a true unix spirit). 

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

### Installation
Install the official python 2.7 release from 
[http://python.org](http://python.org). Use `pip` to install the following 
packages:
- 
- PyQt5 for PYthon 2.7: https://github.com/pyqt/python-qt5

## Linux

### Installation

Install the following packages with pip:
- PyInstaller

Install pyqt5 with apt
`sudo apt-get install python-pyqt5 python-pyqt5-dbg pyqt5-dev-tools`

