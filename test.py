#!/usr/bin/env python3
#!/usr/bin/bash
import subprocess
import os 
import sys

class Automation:
    directoryCreated = False
    error_17 = False
    delimter = "-"*60
    extension = ".py"
    root = "/home/lemule/Documents/Python_Projects/"
    vsCodePath = "/usr/bin/code"
    prompts = [
              "Create Directory: ",
              "Create File: ",
              "*Directory is made*",
              "File Created.",
              "Choose Directory: ",
              "Press [1] to create directory",
              "Press [2] to create file: ",
              ]

    def showDelimter(self):
        print(self.delimter)

    def createDirectory(self):
        self.showDelimter()
        self.directoryName = input(self.prompts[0])
        try:
            if not os.path.exists(self.directoryName):
                self.directoryName = os.path.join(self.root + self.directoryName)
                os.mkdir(self.directoryName)
                self.directoryCreated = True
                print(self.prompts[2] + "\n" + self.directoryName)
        except OSError as e:
            if e.errno == 17:
                self.showDelimter()
                print("Directory is made already.")
                error_17 = True
                self.showDelimter()
                self.showChoice()

    def createFile(self):
        self.showDelimter()
        self.fileName = input(self.prompts[1])
        self.fileName = self.fileName + self.extension
        self.fileName = os.path.join(self.directoryName, self.fileName)
        self.checkPath()
        sys.exit()

    def checkPath(self):
        if not os.path.exists(self.fileName):
            open(self.fileName, 'a').close()
            subprocess.Popen([self.vsCodePath, self.directoryName, self.fileName])  
            print(self.fileName)

        else:
            os.path.exists(self.fileName)
            print("File is already created.")
            self.showDelimter()
            self.createFile()

    def createSubDirFile(self):
        self.subdirFile = input(self.prompts[4])
        self.subdirFile  = os.path.join(self.root, self.subdirFile)
        self.directoryName = os.listdir(self.subdirFile)

class Main(Automation):
    def showChoice(self):
        self.cur_input = input((self.prompts[5]) + '/' + (self.prompts[6]))
        if self.cur_input == "1":
            self.createDirectory()
            self.createFile()
    
        elif self.cur_input == "2":
            self.showDelimter()
            self.directoryName = os.listdir(self.root)
            print(self.directoryName)
            self.showDelimter()
            self.curDirectoy = input(self.prompts[4])
            self.directoryName = os.path.join(self.root, self.curDirectoy)
            if os.path.exists(self.directoryName):
                self.checkSubDirsAndFiles()
                self.createFile()
                sys.exit()
            else:
                self.showChoice()
        else: 
            self.cur_input != "1" or "2"
            self.showChoice()

    def checkSubDirsAndFiles(self):
        for self.curDirectoy in os.listdir(self.directoryName):
            self.curDirectoy = os.path.join(self.root, self.directoryName, self.curDirectoy)
            print(self.curDirectoy)
            
            # if not os.path.isdir(self.curDirectoy):
            #     self.createFile()
            # else:
            #     self.createSubDirFile()

if __name__ == "__main__":
   project = Automation()
   main = Main()
   main.showChoice()

            
            

   

   
