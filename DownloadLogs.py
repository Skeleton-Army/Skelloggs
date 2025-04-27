import adbutils
import sys
import os

def PrintHelp():
    print("Usage: python DownloadLogs.py [OPTIONS...]")
    print("Options: ")
    print("-ip      the ip address of the Robot")
    print("-port    the adb port of the Robot. if not specified will be \"5555\"")
    print("-local   Local directory to save the logs in")
    print("-remote  Remote Direcotry with the log files")
    print("-src     same as \"-remote\"")
    print("-dst     same as \"-local\"")


def ParseAurguments():
    global RobotIP 
    global RobotPort
    global Local
    global Remote
    RobotIP = ""
    RobotPort = 5555
    Local = ""
    Remote = ""
    try:
        for i in range(1, len(sys.argv)):
            match sys.argv[i]:
                case "-ip":
                    RobotIP = sys.argv[1+i]
                case "-port":
                    RobotPort = int(sys.argv[1+i])
                case "-local":
                    Local = sys.argv[1+i]
                case "-remote":
                    Remote = sys.argv[1+i]
                case "-help":
                    PrintHelp()
                case "-h":
                    PrintHelp()
                case "-src":
                    Remote = sys.argv[1+i]
                case "-dst":
                    Local = sys.argv[1+i]
    except:
        pass
    if len(sys.argv) == 1:
        PrintHelp()
    else:
        if sys.argv[1] != "-h" or "-help":
            if RobotIP == "" or Local == "" or Remote == "":
                print("Not all required arguments have been passed!\nExiting..")
                sys.exit(1)
                if os.path.exists(Local) and os.path.isdir(Local):
                    print(Local + " Doenst exist or isnt a directory!\nExiting...")
                    sys.exit(2)
ParseAurguments()
print("IP: " + RobotIP + " Port: " + str(RobotPort) + " Local: " + Local + " Remote: " + Remote)