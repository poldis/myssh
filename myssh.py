from subprocess import Popen

def getServer(resolvable):
	# add shortcuts
    match resolvable:
        case _:
            return resolvable


server = input("Target (shortcut/address): ")
server = getServer(server)
if server == "":
	print("No target specified")
	exit()

user = input("Username: ")
if user == "":
    user = "root"

port = input("Port: ")
if port == "":
    port = "22"

# execute ssh from batch file
p = Popen(r"C:\Users\poldi\Documents\programming\python\myssh\myssh.bat "+server+" "+user+" "+port, cwd=r"C:\Users\poldi\Documents\programming\python\myssh")
p.communicate()