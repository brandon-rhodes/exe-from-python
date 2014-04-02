# Download and run Nuitka directly out of its .tar.gz archive, since
# installing it in a virtual environment will cause it to use the
# environment's site.py in every standalone executable.  Which makes
# every standalone executable will give IOError for "orig-prefix.txt".

# Override the target script on the command line: make TARGET=...
TARGET := hello
VERSION := 0.5.1.1
PYTHON := /usr/bin/python2.7
NUITKA := Nuitka-$(VERSION)/bin/nuitka

all: $(TARGET).exe $(TARGET).dist/$(TARGET).exe

$(TARGET).exe: Nuitka-$(VERSION)/bin/nuitka
	$(PYTHON) $(NUITKA) ../scripts/$(TARGET).py

$(TARGET).dist/$(TARGET).exe: Nuitka-$(VERSION)/bin/nuitka
	$(PYTHON) $(NUITKA) --standalone ../scripts/$(TARGET).py

$(NUITKA): Nuitka-$(VERSION).tar.gz
	tar xvfz Nuitka-$(VERSION).tar.gz
	touch $(NUITKA)

Nuitka-$(VERSION).tar.gz:
	wget https://pypi.python.org/packages/source/N/Nuitka/Nuitka-$(VERSION).tar.gz#md5=f99f120a0f6f4c814095054bff53a497
