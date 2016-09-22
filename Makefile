PHONY:

FILE_UI = mainwindow.ui
FILE_APP = tray.py
FILE_EXE = tray

pyinstaller_opts = -s --clean

ui:
	pyuic5 -x -o $(FILE_APP) $(FILE_UI)

clean:
	rm -rf build/*
	#rm -rf dist/*

osx: clean
	pyinstaller $(pyinstaller_opts) -n $(FILE_EXE) --distpath dist/$@ -w $(FILE_APP)

linux: clean
	pyinstaller $(pyinstaller_opts) -n $(FILE_EXE) --distpath dist/$@ -F -w $(FILE_APP)

windows: #clean
	pyinstaller $(pyinstaller_opts) -n $(FILE_EXE) --distpath dist/$@ -F -w $(FILE_APP)

ressources:
	pyrcc5 -no-compress -o systray_rc.py systray.qrc

test:
	echo $@

build-%:
	#n := $(subst 'build-', '', "$@")
	n = $@
	echo $@

