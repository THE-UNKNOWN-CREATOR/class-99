import os
import shutil

dest = "C:/Users/bops/Desktop/Python/Classes/Prog1/words.txt"
source = "C:/Users/bops/Desktop/Python/Classes/Prog1/New"
shutil.move(source, dest)
print(os.listdir(dest))

#dirs = os.listdir()
#print(dirs)
#print(os.path.splitext("C:/Users/bops/Desktop/Python/Classes/Prog1/OS.py"))
#if os.path.exists("C:/Users/bops/Desktop/Python/Classes/Prog1"):
#    print("yes")
#print(os.getcwd())
#os.mkdir("C:/Users/bops/Desktop/Python/Classes/Prog1/New")