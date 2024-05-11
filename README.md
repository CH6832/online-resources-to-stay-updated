# Latest Tech News

## :newspaper: About the project

A small commandline which allows the user to open multiple websites at the same time, each in a separate tab.

### How it works

The ```open.py``` is the main program. If it's called, it reads in the structure of the ```data.xml``` file. The file must be called with a parameter, that has the same name as one of the tags a step below in the hierarchy of the root tags. Via this parameter, the script identifies the correct section of the file. It then iterates over all ```<url>``` tags and opens each url in a new browser tab.

### Content overview

    .
    ├── CODE_OF_CONDUCT.md - project code of conduct
    ├── COPYRIGHT - project copyright
    ├── data.xml - url storage
    ├── data.xsd - schema for the resources
    ├── LICENSE - license text
    ├── open_test.py - test functions of open.py    
    ├── open.py - main program
    ├── README.md - relevant information about the project
    └── requirements.txt - requirements to run the project

## :runner: Getting started

### Prerequisites and example usage

0. Clone the repository:

```bash
git clone https://github.com/CH6832/online-resources-to-stay-updated.git
```

1. Extract the project:

```bash
tar -xf online-resources-to-stay-updated.zip
```

2. Navigate into the folder:

```bash
cd online-resources-to-stay-updated
```

3. Install requirements:

```bash
pip3 install -r requirements.txt
```

4. Run script:

```bash
python3 open.py documentation
```

## :books: Resources used to create this project

* Python
  * [Python 3.12 documentation](https://docs.python.org/3/)
  * [Built-in Functions](https://docs.python.org/3/library/functions.html)
  * [Python Module Index](https://docs.python.org/3/py-modindex.html)
  * [unittest - Unit testing framework](https://docs.python.org/3/library/unittest.html)
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

## :bookmark: License

This project is licensed under the terms of the [GPL v3](LICENSE).

## :copyright: Copyright

See the [COPYRIGHT](COPYRIGHT) file for copyright and licensing details.

## :straight_ruler: Code of Conduct

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing to this project.
