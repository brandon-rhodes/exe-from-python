# Based on the Makefile at:
# https://github.com/cython/cython/blob/master/Demos/embed/Makefile

# You can override the TARGET on the command line with: make TARGET=...
TARGET := hello

PYTHON := python
PYVERSION := $(shell $(PYTHON) -c "import sys; print(sys.version[:3])")

INCDIR := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc())")
PLATINCDIR := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc(plat_specific=True))")
LIBDIR1 := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
LIBDIR2 := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBPL'))")
PYLIB := $(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBRARY')[3:-2])")

CC := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('CC'))")
LINKCC := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LINKCC'))")
LINKFORSHARED := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LINKFORSHARED'))")
LIBS := $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('LIBS'))")
SYSLIBS :=  $(shell $(PYTHON) -c "import distutils.sysconfig; print(distutils.sysconfig.get_config_var('SYSLIBS'))")

ifeq "$(TARGET)" "cascade"
 MAIN := cascade_init
 SCRIPT := cascade_init.pyx
 EXTRAS := cascade cascade2 cascade3
else
 MAIN := $(TARGET)
 SCRIPT := $(TARGET).py
 EXTRAS :=
endif

OBJECTS := $(addsuffix .o, $(MAIN) $(EXTRAS))

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(LINKCC) -o $@ $(OBJECTS) -L$(LIBDIR1) -L$(LIBDIR2) -l$(PYLIB) \
		$(LIBS) $(SYSLIBS) $(LINKFORSHARED)

$(OBJECTS): %.o: %.c
	$(CC) -c $< -I$(INCDIR) -I$(PLATINCDIR)

$(MAIN).c: ../scripts/$(SCRIPT)
	cython -o $@ --embed $<

$(addsuffix .c, $(EXTRAS)): %.c: ../scripts/%.py
	cython -o $@ $<

clean:
	rm -f *.c *.o
