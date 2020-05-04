#!/usr/bin/env python3
#!/usr/bin/bash
import subprocess
import os 
import sys

class Automation: 
    directoryCreated = False
    error_17 = False
    delimeter = "-"*80
    extension = ".py"
    root = "/home/lemule/Documents/Python_Projects/"
    vsCodePath = "/usr/bin/subl"
    prompts = [
              "Create Directory: ",
              "Create File: ",
              "*Directory is made*",
              "File Created.",
              "Choose Directory: ",
              "Press [1] to create directory",
              "Press [2] to create file: ",
              ]

    def createDirectory(self): 
        print(self.delimeter, os.listdir(self.root), sep= "\n")
        self.directoryName = os.path.join(self.root, input(self.prompts[0]))
        
        try:
            if not os.path.exists(self.directoryName):
                os.mkdir(self.directoryName), print(self.prompts[2], self.directoryName)
                self.directoryCreated = True
                os.chdir(self.directoryName), os.system("/usr/bin/autoGit.sh")
        
        except OSError as e:
            if e.errno == 17:
                print("Directory is made already.")
                error_17 = True
        
    def createFile(self): 
        self.fileName = input(self.prompts[1])
        self.fileName = os.path.join(self.directoryName, self.fileName + self.extension)
        
        if not os.path.exists(self.fileName):  
            open(self.fileName, 'a').close()
            subprocess.Popen([self.vsCodePath, self.directoryName, self.fileName])
            print(self.prompts[3], self.fileName, sep="\n")
            sys.exit()

        else:
            os.path.exists(self.fileName)
            print("File is already created.")
            self.createFile()

    def createFileInExistingDir(self):
        self.directoryName = os.path.join(self.root, input(self.prompts[4]))
        
        if os.path.exists(self.directoryName):
            print(os.listdir(self.directoryName))
            self.createFile()
            sys.exit()

        else:
            self.createFileInExistingDir()

class Main(Automation): 
    def initMain(self): 
        self.cur_input = input(self.prompts[5] + "/" + self.prompts[6])
        
        if self.cur_input == "1":
            self.createDirectory()
            self.createFile()
    
        elif self.cur_input == "2":
            print(self.delimeter, os.listdir(self.root))
            self.createFileInExistingDir()
    
        else: 
            self.cur_input != "1" or "2"
            self.initMain()


if __name__ == "__main__":
   project = Automation()
   main = Main()
   main.initMain()

            
            

   

   
