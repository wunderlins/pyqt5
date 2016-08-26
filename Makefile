
clean:
	rm -rf build/*
	rm -rf dist/*

osx: clean
	pyinstaller -w mainwindow.py

linux: clean
	pyinstaller -F -w mainwindow.py
