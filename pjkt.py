#! python3
""" This script is to help me create and organize files and folders for new projects """

# TODO: refactor code and create neccesarry initial files for the project type
# TODO: using the open() method create and write boiler plate code to initialized files
# TODO: use flags to extend application ability and try running command from script to download pjkt dependencies

import sys, os, pprint
from build import Build

# Project type structures

react_pjkt_folders = [
  "/components",
  "/lib",
  "/pages",
  "/server",
  "/static"
]
# get arguments passed in from command
# 1st command - Project destination folder
# 2nd command - Project name/Also default project folder name

# 3rd command - Project type

command_list = {
  "destination": sys.argv[1],
  "name": sys.argv[2],
  "type": sys.argv[3]
}

pprint.pprint(sys.argv[1:])
buildOne = Build(command_list, react_pjkt_folders)
buildOne.create()

