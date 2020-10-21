import sys
import os
import markdown

def load_markdowns(root = '_posts'):
    markdowns = []
    for path, dirs, files in os.walk(root):
        for file in files:
            if file.endswith(".md") or file.endswith(".markdown"):
                filePath = getPath(path, file)
                with open(filePath, 'r', encoding="UTF-8") as f:
                    fileString = f.read()
                    md = markdown.markdown(fileString)
                    markdowns.append(md)
    
    return markdowns
def load_images(path = "./assets/images"):
    print(os.listdir(path))
    
def getPath(path, file):
    newPath = '/'.join(path.split("\\"))
    return f"{newPath}/{file}"

load_images()

# mds = load_markdowns()
# for md in mds:
#     print(md)

