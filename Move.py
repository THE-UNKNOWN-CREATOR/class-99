import shutil

s = input("Tell Me The Source: ")
src = "C:/Users/bops/Desktop/" + s

d = input("Tell Me The Destination: ")
dest = "C:/Users/bops/Desktop/" + d

shutil.move(src, dest)