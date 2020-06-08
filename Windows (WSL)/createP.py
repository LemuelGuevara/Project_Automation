#!/usr/bin/python3
import os
import sys
import subprocess

class Automation:
    gitCommands = [
        "git init",
        "touch README.md",
        "git add .",
        ("git commit -m Added"),
        "hub create",
        "git push -u origin master"
        "code ."
        ]

    root = "/mnt/c/Users/Lemue/Desktop/Python_Projects"

    def getProject(self):
        """Gets the project name from the user"""

        self.projectName = input("Create Project: ")
        return self.setProjectPath(self.projectName)

    def setProjectPath(self, project):
        """Sets the path of the project"""
        return (os.path.join(self.root, self.projectName))
        
        if not os.path.exists(self.setProjectPath(1)):
            return self.makeProject()
        
    def makeProject(self):
        """Checks if the project already exists"""

        try:
            os.mkdir(self.setProjectPath(1))
            subprocess.Popen([self.txtEditorPath, self.setProjectPath(1)])
            
            return self.makeReadmeAndFile()

        except Exception:
            print("Project already exists.")
            return self.getProject(), self.makeProject()

    def makeReadmeAndFile(self):    
        """Initializes a git repo along with a hub and some startup files"""

        os.chdir(self.setProjectPath(1))
        for command in self.gitCommands:
            os.system(command)

if __name__ == "__main__":
    auto = Automation()
    auto.getProject()
    auto.makeProject()
