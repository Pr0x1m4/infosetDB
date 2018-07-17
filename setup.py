from distutils.core import setup
from setuptools import find_packages

from setup.database import DatabaseSetup

setup(
    name='Infoset DB',
    version='2.1.1',
    author='Jordan Jones',
    author_email='proxima.aust@gmail.com',
    maintainer="The Palisadoes Foundation",
    maintainer_email="proxima.aust@gmail.com",
    url="https://github.com/PalisadoesFoundation/infoset-ng",
    license='Apache License 2',
    cmdclass={
        'db': DatabaseSetup,
    },
)
