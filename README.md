#TimerBar
Super-simple OSX bar applet that counts down from a set interval and notifies.

Uses rumps as the library: <https://github.com/tito/rumps>

Uses parsedatetime for custom timer: <https://github.com/bear/parsedatetime>

Uses icons from <http://icons8.com/icons/>, who generously offer them for free in exchange for a link!

To Create a standalon app, ensure you have py2app installed and use:

    python setup.py py2app

the resulting app is in the dist directory

## Known Issues

* Building with virtualenv requires you to create an ``Info.plist`` in the
directory.
See [this comment by **Waldo1979**](https://github.com/jaredks/rumps/issues/47)
for a fix. Just use ``which python`` to find your virtualenv's directory.
