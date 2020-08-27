#!C:\Users\admin\Desktop\MiPush_Server_Python_20170704\xmpush-python-1.0.4\venv\Scripts\python3.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==9.0.3','console_scripts','pip3'
__requires__ = 'pip==9.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==9.0.3', 'console_scripts', 'pip3')()
    )
