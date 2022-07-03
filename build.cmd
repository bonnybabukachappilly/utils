python setup.py bdist_wheel sdist
pip install -e .[testing]
tox

@REM check-manifest --create