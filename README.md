# s3kiro23.github.io

S3kiro23 Repos List Portal
=========================


A simple, static portal which outlines my projets and contributions.


Development
-----------

### Run the site locally
```bash
gem install bundler
bundle install
bundle exec jekyll serve
```


### Update list of repos:
```bash
pip install pystache pygithub3
./update_repos.py
```

### Generate static file:
```bash
./generate.py
```

About the code
-----------

Repositories are listed in the `repos.json` file as a map of repository names
to a list of their categories. Invoking the `generate.py` script will update
the `index.html` page with the latest repos by using the `index.mustache` file
as a template.

Repository data is pulled via the GitHub API (e.g., website). To make authenticated
requests and work around the rate-limiting, add an entry for api.github.com to
your ~/.netrc file, preferably with a Personal Access Token from
https://github.com/settings/tokens

    machine api.github.com
      login YourUsername
      password PersonalAccessToken

Images are loaded by convention from the `repo_images/` directory. Ensure the
name is the same as the repo name in the `repos.json` file and has a `.jpg`
extension. Currently all images are rotated 10 degrees counter-clockwise to
break up the overwhelming horizontal and vertical visual lines on the page.