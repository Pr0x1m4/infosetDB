from distutils.core import setup
from setuptools import find_packages

from maintenance.database import DatabaseSetup

install_requires = [
    "Flask",
    "celery",
    "setuptools",
    "PyMySQL",
    "PyYAML",
    "requests",
    "SQLAlchemy",
    "SQLAlchemy-Utils",
    "Werkzeug",
    "redis"
]

tests_require = [
    "mock",
    "nose"
]

setup(
    name='Infoset DB',
    version='2.1.1',
    author='Jordan Jones',
    author_email='jordn_jones94@gmail.com',
    maintainer="The Palisadoes Foundation",
    maintainer_email="jordn_jones94@gmail.com",
    url="https://github.com/PalisadoesFoundation/infoset-ng",
    install_requires=install_requires,
    tests_require=tests_require,
    packages=find_packages('.'),
    license='Apache License 2',
    cmdclass={
        'install': DatabaseSetup,
    },
)
