import zipfile
import sys

name = "Anton"
zipfilename = "demo.zip"
zipPath = ""
script = ""

str = ""

Path = []


def is_equal(parts, path):
    equal = True
    for i in range(len(path)):
        if path[i] != parts[i]:
            equal = False
    if len(path) != len(parts) - 1:
        equal = False
    return equal

def cmd_ls():
    with zipfile.ZipFile(zipfilename) as myzip:
        files = myzip.namelist()
        for file in files:
            parts = file.split('/')
            if is_equal(parts, Path):
                print ('/'.join(parts[len(Path)::]))


def cmd_cd():
    global Path
    with zipfile.ZipFile(zipfilename) as myzip:
        if token[1] == '..' :
            Path.pop()
        elif token[1] == '\\':
            Path.clear()
        else :
            Path.append(token[1])


def cmd_mv():
    with zipfile.ZipFile(zipfilename, mode='a') as myzip:
        myzip.write(token[1], token[2], compress_type=None, compresslevel=None)


def cmd_cat():
    with zipfile.ZipFile(zipfilename) as myzip:
        with myzip.open(token[1]) as myfile:
            textlines = myfile.readlines()
            n = len(textlines)
            for i in range(n):
                print(textlines[i])


def cmd_tac():
    with zipfile.ZipFile(zipfilename) as myzip:
        with myzip.open(token[1]) as myfile:
            textlines = myfile.readlines()
            n = len(textlines)
            for i in range(n):
                print(textlines[n - i - 1])


def Interpret():
    global token
    token = str.split()
    if (len(token) > 0):
        match (token[0]):
            case "ls":
                cmd_ls()
            case "cd":
                cmd_cd()
            case "mv":
                cmd_mv()
            case "cat":
                cmd_cat()
            case "tac":
                cmd_tac()
            case _:
                print("Error")


def Params():
    i = 1
    global name
    global zipfilename
    global script
    while i < len(sys.argv):
        match(sys.argv[i]):
            case "-name":
                name = sys.argv[i+1]
                i = i + 2
            case "-zip":
                zipfilename = sys.argv[i+1]
                i = i + 2
            case "-script":
                script = sys.argv[i+1]
                i = i + 2
            case _: print ("Unknown parameter")

Params()
if (script != ""):
    filescript = open(script, "r")
    lines = filescript.readlines()
    for line in lines:
        str = line.strip()
        Interpret()
        print(name + "@" + '/'.join(Path) + ">")
    filescript.close

while str != "exit":

    print(name + "@" + '/'.join(Path) + ">")
    str = input()
    Interpret()
