#!"c:\users\kwaku biney\desktop\spotify_project\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'huey==2.3.0','console_scripts','huey_consumer'
__requires__ = 'huey==2.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('huey==2.3.0', 'console_scripts', 'huey_consumer')()
    )