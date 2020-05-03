#!/usr/bin/env python3
#!/usr/bin/bash
import subprocess
import os 
import sys
import stat
from pathlib import Path

class Automation: 
    directoryCreated = False
    error_17 = False
    delimter = "-"*100
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
              "Press [4] to create subdirectory:",
              ]

    def showDelimter(self):
        print(self.delimter)

    def createDirectory(self): #Creates a directory under the root path
        self.showDelimter()
        print(os.listdir(self.root))
        self.directoryName = input(self.delimter + "\n" + self.prompts[0])
        try:
            if not os.path.exists(self.directoryName): #Checks if the directory exits or not
                self.directoryName = os.path.join(self.root + self.directoryName)
                os.mkdir(self.directoryName) 
                os.chdir(self.directoryName)
                self.directoryCreated = True
                print(self.prompts[2] + "\n" + self.directoryName + "\n" + self.delimter)
                self.gitInit()
        
        except OSError as e: #Shows if the dirertory exists
            if e.errno == 17:
                print(self.delimter + "\nDirectory is made already.\n" + self.delimter + "\n")
                error_17 = True

    def gitInit(self):
        self.fileName = os.path.join(self.directoryName, "autoGit.sh")
        os.system('touch README.md')
        open(self.fileName, "a+").write("#!/usr/bin/sh \ngit init\ngit add README.md\ngit commit -m Added\nhub create\ngit push -u origin master")
        self.f = Path(self.fileName)
        self.f.chmod(self.f.stat().st_mode | stat.S_IXUSR)
        os.system(self.fileName)
        
    def createFile(self): #Creates a file at a given directory
        self.fileName = input(self.delimter + "\n" + self.prompts[1])
        self.fileName = os.path.join(self.directoryName, self.fileName + self.extension)
        
        if not os.path.exists(self.fileName):
            open(self.fileName, 'a').close()
            subprocess.Popen([self.vsCodePath, self.directoryName, self.fileName])  
            print(self.fileName)

        else:
            os.path.exists(self.fileName)
            print("File is already created.\n" + self.delimter)
            self.createFile()
    
    # def createSubDirFile(self):
    #     self.subdirFile = input(self.prompts[4])
    #     self.directoryName = os.path.join(self.root, self.subdirFile)

class Main(Automation): #Initializes the script and shows the choices
    def initMain(self): 
        self.cur_input = input((self.prompts[5]) + '/' + (self.prompts[6]))
        if self.cur_input == "1":
            self.createDirectory()
            self.createFile()
    
        elif self.cur_input == "2":
            self.showDelimter()
            print(os.listdir(self.root))
            self.curDirectoy = input(self.delimter + "\n" + self.prompts[4])
            self.directoryName = os.path.join(self.root, self.curDirectoy)
            
            if os.path.exists(self.directoryName):
                self.checkSubDirsAndFiles()
                self.createFile()
                sys.exit()
            else:
                self.initMain()
        else: 
            self.cur_input != "1" or "2"
            self.initMain()

    def checkSubDirsAndFiles(self): #Checks for sudirectories and files of the directory
        for self.curDirectoy in os.listdir(self.directoryName):
            self.curDirectoy = os.path.join(self.directoryName, self.curDirectoy)
            print(self.curDirectoy)
            
            # if not os.path.isdir(self.curDirectoy):
            #     self.createFile()
            # else:
            #     self.createSubDirFile()

if __name__ == "__main__":
   project = Automation()
   main = Main()
   main.initMain()

            
            

   

   
