PHONY:

FILE_UI = mainwindow.ui
FILE_APP = systray.py
FILE_EXE = systray

pyinstaller_opts = -s

ui:
	pyuic5 -x -o $(FILE_APP) $(FILE_UI)

clean:
	rm -rf build/*
	#rm -rf dist/*

osx: clean
	pyinstaller $(pyinstaller_opts) -n $(FILE_EXE) --distpath dist/$@ -w $(FILE_APP)

linux: clean
	pyinstaller $(pyinstaller_opts) -n $(FILE_EXE) --distpath dist/$@ -F -w $(FILE_APP)

windows: clean
	pyinstaller $(pyinstaller_opts) -n $(FILE_EXE) --distpath dist/$@ -F -w $(FILE_APP)

ressources:
	pyrcc5 -no-compress -o systray_rc.py systray.qrc

test:
	echo $@

build-%:
	#n := $(subst 'build-', '', "$@")
	n = $@
	echo $@

