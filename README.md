# URL Opener

## Table of Contents

- [URL Opener](#url-opener)
  - [Table of Contents](#table-of-contents)
  - [About the project](#about-the-project)
    - [How it works](#how-it-works)
    - [Content overview](#content-overview)
  - [Getting started](#getting-started)
    - [Prerequisites and example usage](#prerequisites-and-example-usage)
    - [Running tests](#running-tests)
  - [Versioning](#versioning)
    - [Using git as a version control system](#using-git-as-a-version-control-system)
  - [Resources used to create this project](#resources-used-to-create-this-project)
  - [License](#license)
  - [Copyright](#copyright)

## About the project

A command-line tool that allows users to open multiple websites simultaneously, each in a separate tab in Firefox. It reads URLs from an XML file and opens them based on the specified segment.

### How it works

When the program is executed, it reads the structure of the `data.xml` file. The script must be called with a parameter that matches one of the tags a step below the root tags in the hierarchy. This parameter identifies the correct section of the file. The script then iterates over all `<url>` tags within that section and opens each URL in a new Firefox browser tab.

### Content overview

    .
    ├── data/ - data directory with urls
    ├── tests/ - unit and regression tests
    ├── __init__.py - package initialization
    ├── .bumbversion.cfg - automatically process version
    ├── .gitignore - excludes unnecessary files
    ├── COPYRIGHT - project copyright
    ├── LICENSE - license text
    ├── README.md - project information
    ├── requirements.txt - project requirements
    └── open_url.py - main program

## Getting started

### Prerequisites and example usage

0. Clone the repository:

```bash
git clone https://github.com/CH6832/online-resources-to-stay-updated.git
```

1. Navigate into the folder:

```bash
cd online-resources-to-stay-updated
```

2. Install requirements:

```bash
pip3 install -r requirements.txt
```

3. Examples with the required parameters:

```bash
py url_opener.py websites
```

```bash
py url_opener.py articles
```

### Running tests

pytest test_url_launcher.py

## Versioning

The project uses Semantic Versioning to manage versions. Semantic Versioning follows the format MAJOR.MINOR.PATCH, where:

* MAJOR version increments indicate incompatible changes or major updates.
* MINOR version increments indicate new features or improvements that are backward-compatible.
* PATCH version increments indicate backward-compatible bug fixes.

Versioning Example

* 1.0.0: Initial release with basic functionality.
* 1.1.0: Added new features like tab completion and command aliases.
* 1.1.1: Fixed bugs and improved error handling.

To see the current version of the project, check the __version__ attribute in the script or refer to the version tags in the Git repository.

### Using git as a version control system

0. Initialize a Git Repository:

```sh
git init
```

1. Add and Commit Changes

```sh
git add .
git commit -m "Initial commit"
```

2. Tagging releases

```sh
git tag -a v1.0.0 -m "Initial release"

```

3. Pushing to remote repo

```sh
git remote add origin https://github.com/CH6832/online-resources-to-stay-updated.git
git push origin main --tags
```

## Resources used to create this project

* Python
  * [Python 3.12 documentation](https://docs.python.org/3/)
  * [Built-in Functions](https://docs.python.org/3/library/functions.html)
  * [Python Module Index](https://docs.python.org/3/py-modindex.html)
  * [pytest: helps you write better programs](https://docs.pytest.org/en/8.2.x/)
  * [pylint](https://pylint.readthedocs.io/en/stable/)
  * [mypy](https://mypy.readthedocs.io/en/stable/)
  * [xml.etree.ElementTree](https://docs.python.org/3.11/library/xml.etree.elementtree.html)
* XML
  * [Extensible Markup Language (XML) 1.0 (Fifth Edition)](https://www.w3.org/TR/xml/)
  * [W3C XML Schema Definition Language (XSD)](https://www.w3.org/TR/xmlschema11-1/)
* Markdwon
  * [Basic syntax](https://www.markdownguide.org/basic-syntax/)
  * [Complete list of github markdown emojis](https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia)
  * [Awesome template](http://github.com/Human-Activity-Recognition/blob/main/README.md)
  * [.gitignore file](https://git-scm.com/docs/gitignore)
* Editor
  * [Visual Studio Code](https://code.visualstudio.com/)
* Commandline tools
  * [Build Command-Line Interfaces With Python's argparse](https://realpython.com/command-line-interfaces-python-argparse/)
  * [Master the Art of Command Line: Your Ultimate Guide to Developing Powerful Tools](https://hackernoon.com/master-the-art-of-command-line-your-ultimate-guide-to-developing-powerful-tools)
  * [Command Line Interface Guidelines](https://clig.dev/)
  * [Building a Network Command Line Interface in Go](https://tutorialedge.net/golang/building-a-cli-in-go/)

## License

This project is licensed under the terms of the [GPL v3](LICENSE).

## Copyright

See the [COPYRIGHT](COPYRIGHT) file for copyright and licensing details.
