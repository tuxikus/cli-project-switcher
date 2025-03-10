#!/usr/bin/env python3

from pathlib import Path

PROJECT_FILE = Path.home() / ".config" / "cli-project-switcher" / "projects"

def check_project_file():
    if not PROJECT_FILE.is_file():
        raise FileNotFoundError()

def read_projects():
    content = ""
    
    with open(PROJECT_FILE, "r") as f:
        content = f.read()

    return content.split("\n")[:-1]

def main():
    check_project_file()
    
    projects = read_projects()

    for project in projects:
        # bash does not recognize ~ in a script
        print(project.replace("~", str(Path.home())).strip())

if __name__ == "__main__":
    main()
