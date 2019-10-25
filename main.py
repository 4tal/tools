import sys
import os

#TODO: implement automatic setup.
#TODO: get the path of my folder.
#TODO: add configuration file.
#TODO: Hierarchical getters and setups.


commands = {
        "update": 'cd ~/Code/jack/tools ;git add .;git commit -m "automatic commit";git push',
        "sleep": 'pmset sleepnow'
    }

options = {
    "pipenv": [
        "pipenv install",
        "pipenv install --skip-lock",
        "pipenv install <package>",
        "pipenv update <package>",
        "pipenv --rm"
        ],
    "git": [
        "git reset --hard <commit>",
        "git stats",
        "git add <file/.>"
    ],
    "vim": [
        ':wq -> save and exit',
        ':q! -> exit without save'
    ],
    "linux": "",
    "postgres":"IPFS Pinning"
    }

setups = {
    "git":["git init"],
    "ssh":{
        "generate":["""ssh-keygen -t rsa -C 'idan.4tal@gmail.com'"""]
    }
}


def main():
    if len(sys.argv) == 1:
        for option in options:
            print(f'{option}')
        return
    
    if sys.argv[1]=='setup':
        for setup in setups:
            print(f'{setup}')
        return

    if sys.argv[1]=='command':
        for command in commands:
            print(f'{command}')
        choosen_command = str(input("Choose command.\n"))
        os.system(commands[choosen_command])
        return
    
    if len(sys.argv)==2:
        for option in options[sys.argv[1]]:
            print(option)
    
main()
