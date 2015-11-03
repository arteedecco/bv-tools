from setuptools import setup

setup(
    name='bv-tools',
    version='0.1',
    py_modules=['bvtools'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        bvtools=bvtools:cli
    ''',
)
