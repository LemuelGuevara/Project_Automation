#!/usr/bin/python3
import os
import sys

gitCommands = [
    "git init",
    "touch README.md",
    "git add .",
    ("git commit -m Initial_Commit"),
    "hub create",
    "git push -u origin master",
    "code ."
]

class Automation:
    def __init__(self, projectName, rootPath):
        self.projectName = projectName
        self.rootPath = rootPath
        self.gitInit = gitCommands

    def createProject(self):
        self.projectName = os.path.join(self.rootPath, self.projectName)

        try:
            os.mkdir(self.projectName)

            return self.initProject()

        except Exception:
            print("Project already exists.")
            sys.exit()

    def initProject(self):
        os.chdir(self.projectName)

        for command in self.gitInit:
            os.system(command)


if __name__ == "__main__":
    root = "/mnt/c/Users/Lemue/Desktop/Python_Projects"
    usrInput = str(sys.argv[1])

    auto = Automation(usrInput, root)
    auto.createProject()

