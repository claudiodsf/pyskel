#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This script sets the package name and author name and email in the source
code of a Python package created with pyskel.

The script will ask for the package name, author name and author email,
then it will search every file in the current directory and subdirectory,
replace "pyskel", "Author Name" and "author@email.com" with the provided
inputs.

Files that match the ignore patterns in ".gitignore" will be skipped.
"""
import os
import contextlib
import textwrap
import subprocess


def main():
    """
    Main function of the script.
    """
    print(textwrap.fill(__doc__, 80))
    print()
    answer = input("Continue? [y/n] ")
    if answer.lower() != "y":
        return
    # Interactive prompt for package name, author name and author email
    # the answer cannot be empty
    while True:
        package_name = input("Package name: ")
        if package_name:
            break
    while True:
        author_name = input("Author name: ")
        if author_name:
            break
    while True:
        author_email = input("Author email: ")
        if author_email:
            break
    # Build a file list using the system command "git -ls-files"
    filelist = subprocess.check_output(
        'git ls-files', shell=True).splitlines()
    # Remove the file "set_package_and_author.py" from the list
    with contextlib.suppress(ValueError):
        filelist.remove(b"set_package_and_author.py")
    # Replace the strings "pyskel", "Author Name" and "author@email.com"
    # with the provided inputs for every file in the list
    for filename in filelist:
        with open(filename, "rb") as f:
            content = f.read()
        content = content.replace(b"pyskel", package_name.encode())
        content = content.replace(b"Author Name", author_name.encode())
        content = content.replace(b"author@email.com", author_email.encode())
        with open(filename, "wb") as f:
            f.write(content)
    # rename the script file
    os.rename(
        os.path.join("pyskel", "scripts", "pyskel.py"),
        os.path.join("pyskel", "scripts", package_name + ".py")
    )
    # replace the directory named "pyskel" with package_name
    os.rename("pyskel", package_name)
    # Print a message to the user
    print("Done. Please check the changes and commit them.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAborted by user.")
