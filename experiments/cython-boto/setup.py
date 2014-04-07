from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="Boto",
    ext_modules=(
        cythonize('boto/[a-z]*.py', error_on_unknown_names=False) +
        cythonize('boto/gs/[a-z]*.py', error_on_unknown_names=False) +
        cythonize('boto/pyami/[a-z]*.py', error_on_unknown_names=False) +
        cythonize('boto/s3/[a-z]*.py', error_on_unknown_names=False) +
        cythonize('boto/utils/[a-z]*.py', error_on_unknown_names=False) +
        []
        ),
    )
