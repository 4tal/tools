import sys
import os

#TODO: implement automatic setup.
#TODO: get the path of my folder.
#TODO: add configuration file.
#TODO: Hierarchical getters and setups.


commands = {
        "git push": ['cd ~/Code/jack/tools ;git add .;git commit -m "automatic commit";git push']
    }

options = {
    "pipenv": [
        "pipenv install <package>",
        "pipenv update <package>",
        "pipenv install"
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
    "linux": ""
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
        choosen_command = str(input("Choose command."))
        for command in commands[choosen_command]:
            os.system(command)
        return
    
    
main()
