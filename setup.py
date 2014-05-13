from setuptools import setup

APP = ['timerbar.py']
DATA_FILES = ['data']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'parsedatetime'],
    'iconfile': 'data/rooster-128.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
