#!/usr/bin/env python3

from pathlib import Path

PROJECT_CONFIG_FILE = Path.home() / ".config" / "cli-project-switcher" / "projects"

def check_project_config_file():
    if not PROJECT_CONFIG_FILE.is_file():
        raise FileNotFoundError()

def read_projects():
    with open(PROJECT_CONFIG_FILE, "r") as f:
        content = f.read()

    return content.split("\n")[:-1]

def main():
    try:
        check_project_config_file()
    except:
        print("~/.config/cli-project-switcher/config not found")
        exit(1)

    for project in read_projects():
        # bash does not recognize ~ in a script
        print(project.replace("~", str(Path.home())).strip())

if __name__ == "__main__":
    main()
