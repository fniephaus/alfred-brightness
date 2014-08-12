all: clean build

build:
	cd src ; \
	zip ../Display-Brightness.alfredworkflow . -r --exclude=*.DS_Store* --exclude=*.pyc*

clean:
	rm -f *.alfredworkflow