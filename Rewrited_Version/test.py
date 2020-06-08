import sys
import os

root = "/mnt/c/Users/Lemue/Desktop/Python_Projects"
projectName = str(sys.argv[1])

def createProject():
    try:
        projectPath = os.path.join(root, str(projectName))
        os.mkdir(projectPath)
    
    except Exception:
        print("Project Already Exists")
        sys.exit()