from distutils.core import setup

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
    version='2.1.0',
    author='Jordan Jones',
    author_email='jordn_jones94@gmail.com',
    maintainer="The Palisadoes Foundation",
    maintainer_email="jordn_jones94@gmail.com",
    url="https://github.com/PalisadoesFoundation/infoset-ng",
    install_requires=install_requires,
    tests_require=tests_require,
    packages=['infosetdb', ],
    license='Apache License 2',
)
