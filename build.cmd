python setup.py bdist_wheel sdist
pip install -e .[dev]
tox

@REM check-manifest --create