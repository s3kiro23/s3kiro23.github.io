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
  
def fetching_repos():
  print('Fetching all repos information...')
  # Use the following for development so you do not hammer the GitHub API.
  #return {'name': name, 'html_url': 'http://google.com', 'homepage': 'http://example.com', 'description': 'Description!'}

  if not logged_in:
    print('Not logged in.  Please login to GitHub.')
    time.sleep(2.0) # Take a nap so GitHub doesn't aggressively throttle us.

  try:
    repos = ghclient.get_user().get_repos()
  except:
    print('Error fetching repos.')
    return
  
  repos_list = {}  # Dict pour stocker les informations des dépéts

  repos_list = {repo.name: repo.topics for repo in repos}
  
  with open(repos_out, 'w') as f:
      json.dump(repos_list, f, indent=4) 
  
fetching_repos()