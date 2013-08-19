# FixIndents

A simple yet flexible utility to convert indentation in your source code files.

## Why?

I needed to convert indentations in a source code file, and I wasn't able to find anything
really flexible to do this. So, this script is an attempt to code something flexible enough
to handle any possible use-case.

## Usage

### fixindents -h

    usage: fixindents.py [-h] [--version] (--source-tabs | --source-size SIZE)
                         (--dest-tabs | --dest-size SIZE) --source SOURCE
                         (--dest DEST | --debug) [--exclude EXCLUDE]
                         [--extensions EXTENSIONS]

    A simple yet flexible utility to convert indentation.

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      --source-tabs         Source file uses tabs for indentation.
      --source-size SIZE    Indents size in source file(s).
      --dest-tabs           Use tabs for indentation in destination file.
      --dest-size SIZE      Indents size in destination file.
      --source SOURCE       File of folder from which code should be read.
      --dest DEST           File or folder to which code should be written.
      --debug               Output converted data to console, don't write
                            anything.
      --exclude EXCLUDE     Comma-separated list of directory names to ignore.
                            Only useful when SOURCE is a directory.
      --extensions EXTENSIONS
                            Comma-separated list of specific file extensions to
                            convert. Only useful when SOURCE is a directory.

### Exemples

* Convert `fixindents.py` 4-spaces indents to tab indents, write to `fixendents_tabs.py`:


    fixindents.py --source-size 4 --dest-tabs --source fixindents.py --dest fixindents_tabs.py

* Convert previously created `fixindents_tabs.py` to 2-spaces indents, write to `fixindents_space.py`:


    fixindents.py --source-tabs --dest-size 2 --source fixindents_tabs.py --dest fixindents_space.py

* Convert all files in the `FixIndents` folder from 4-spaces to tabs, write to the `FixIndentsTabs` folder:


    fixindents.py --source-size 4 --dest-tabs --source FixIndents --dest FixIndentsTabs

* Convert 4-spaces `.py` files in the `FixIndents` folder to tabs, write to the `FixIndentsTabs` folder:


    fixindents.py --source-size 4 --dest-tabs --source FixIndents --dest FixIndentsTabs --extentions ".py"

## Contribute

Feel free to fork this repository and improve the code, any pull-request will be welcome.
