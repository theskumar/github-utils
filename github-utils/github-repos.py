from __future__ import print_function
from github3 import login
from getpass import getpass, getuser
import sys
try:
    import readline  # noqa
except ImportError:
    pass

try:
    user = raw_input('GitHub username: ')
except KeyboardInterrupt:
    user = getuser()

password = getpass('GitHub password for {0}: '.format(user))
organization_name = raw_input('GitHub organisation: ')

# Obviously you could also prompt for an OAuth token
if not (user and password):
    print("Cowardly refusing to login without a username and password.")
    sys.exit(1)

if not organization_name:
    print("Cowardly refusing because oraganization name is required.")
    sys.exit(1)


g = login(user, password)
org = g.organization(organization_name)
for repo in org.iter_repos():
    print(repo.html_url)
