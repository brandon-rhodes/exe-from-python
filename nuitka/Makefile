# You can override the TARGET on the command line with: make TARGET=...
TARGET := hello

# We download and run Nuitka directly out of its .tar.gz archive, since
# installing it in a virtual environment will cause it to use the
# environment's site.py in every standalone executable.  Which makes
# every standalone executable give IOError for "orig-prefix.txt".

VERSION := 0.5.1.1
NUITKA := ../cache/Nuitka-$(VERSION)/bin/nuitka
URL := https://pypi.python.org/packages/source/N/Nuitka/Nuitka-$(VERSION).tar.gz#md5=f99f120a0f6f4c814095054bff53a497

# We run Nuitka with the system Python, but add the virtual
# environment's site-packages directory manually to PYTHONPATH so that
# Nuitka can find our dependencies.

SITE_PACKAGES := $(shell python -c 'import sys; print [p for p in sys.path if "site-packages" in p][0]')
PYTHON := PYTHONPATH=$(SITE_PACKAGES) /usr/bin/python2.7

all: $(TARGET).exe $(TARGET).dist/$(TARGET).exe

$(TARGET).exe: $(NUITKA)
	$(PYTHON) $(NUITKA) ../scripts/$(TARGET).py

$(TARGET).dist/$(TARGET).exe: $(NUITKA)
	$(PYTHON) $(NUITKA) --standalone ../scripts/$(TARGET).py

$(NUITKA): ../cache/Nuitka-$(VERSION).tar.gz
	cd ../cache && tar xvfz Nuitka-$(VERSION).tar.gz && touch $(NUITKA)

../cache/Nuitka-$(VERSION).tar.gz:
	mkdir -p ../cache && cd ../cache && wget $(URL)
