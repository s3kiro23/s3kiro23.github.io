#!/usr/bin/env python

import netrc
import time
import json

from pygithub3 import Github

repos_out = 'repos.json'

auth = netrc.netrc()

try:
  (user, _, token) = auth.authenticators('api.github.com')
  ghclient = Github(token)
  logged_in = True
  print("Logged in")
except Exception as e:
  ghclient = Github()
  logged_in = False
  print(f"Not logged in with error : {e}")
  
def gh_repos():
  print('Fetching all repos information...')

  if not logged_in:
    print('Not logged in.  Please login to GitHub.')
    time.sleep(2.0) # Take a nap so GitHub doesn't aggressively throttle us.

  repos = ghclient.get_user().get_repos()
  repos_formatted = {repo.name: repo.topics for repo in repos}

  with open(repos_out, 'w') as f:
      json.dump(repos_formatted, f, indent=4) 


gh_repos()