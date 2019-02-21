python_home = 'var/www/catalog_app/catalog_app/venv3'

import sys
import site

# Calculate path to site-packages directory.

python_version = '.'.join(map(str, sys.version_info[:2]))
site_packages = python_home + '/lib/python%s/site-packages' % python_version
site.addsitedir(site_packages)

# Remember original sys.path.

prev_sys_path = list(sys.path)

# Add the site-packages directory.

site.addsitedir(site_packages)

# Reorder sys.path so new directories at the front.

new_sys_path = []

for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)

sys.path[:0] = new_sys_path

import logging
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0,"/var/www/catalog_app/")

from catalog_app.application import app as application
application.secret_key = 'Add your secret key'
