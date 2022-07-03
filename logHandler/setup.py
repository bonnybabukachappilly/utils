from setuptools import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='logHandler',
    version='0.0.1',
    description='Add basic log functionality.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    py_modules=[
        'logHandler'
    ],
    extras_require={
        'dev': [
            'pytest==7.1.2'
        ]
    },
    classifiers=[
        'Programming Langauge :: Python :: 3',
        'Programming Langauge :: Python :: 3.8',
        'Programming Langauge :: Python :: 3.9',
        'Programming Langauge :: Python :: 3.10',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE Version 3',
        'Operating System :: Windows'
    ],
)
