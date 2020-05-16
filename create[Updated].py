<<<<<<< HEAD

=======
>>>>>>> 824b07637d0d8f3d9abd2f7d4e83d4d53aa896b7
import os
import sys
import subprocess

class Automation:
    gitCommands = [
        "touch README.md",
        "touch main.py",
        "git init",
        "git add .",
        ("git commit -m Added"),
        "hub create",
        "git push -u origin master"
        ]
    root = "/mnt/c/Users/Lemue/Desktop/Python_Projects"
    txtEditorPath = "/mnt/c/Users/Lemue/AppData/Local/Programs/Microsoft VS Code/bin/code"
    prompt = "Create Project: "

    def getProject(self):
        """Gets the project name from the user"""

        self.projectName = input(self.prompt)
        return self.setProjectPath(self.projectName)

    def setProjectPath(self, projectName):
        """Sets the path of the project"""
        return (os.path.join(self.root, self.projectName))
        
        if not os.path.exists(self.setProjectPath(1)):
            return self.makeProject()
        
    def makeProject(self):
        """Checks if the project already exists"""

        try:
            os.mkdir(self.setProjectPath(1))
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
<<<<<<< HEAD
    auto.makeProject()
=======
    auto.makeProject()
>>>>>>> 824b07637d0d8f3d9abd2f7d4e83d4d53aa896b7
