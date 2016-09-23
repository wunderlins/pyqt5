PHONY: gui

FILE_UI = ui/ad/ad/dialog.ui
FILE_MAIN = AuthWindow.py
FILE_APP = tray.py
FILE_EXE = tray

#pyinstaller_opts = -s --clean
pyinstaller_opts = --clean

ifeq ($(OS),Windows_NT)
	make   = ./bin/make
	magick = ./bin/magick.exe
else
	make   = make
	magick = ImageMagick
endif

gui:
	pyuic5 -x -o $(FILE_MAIN) $(FILE_UI)

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

