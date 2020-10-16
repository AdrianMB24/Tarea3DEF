"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
#long_description = (here / 'README.txt').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(

    name='Tarea3DEF',
    version='1.0.0',
    description='Paquete con metodos Tarea 3',
    author='Carlos_Joseph_Adrian_Emmanuel', 
    packages=['Metodos'],
    python_requires='>=3',
    install_requires=['pillow', 'tabulate', 'playsound', 'numpy']
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    #entry_points={  # Optional
    #    'console_scripts': [
    #       'sample=sample:main',
    #    ],
    # },

)
