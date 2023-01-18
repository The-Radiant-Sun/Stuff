import os


def alterFile(location: str, target_string: str, result: str):
    file_lines = open(location, mode="r", errors="replace").readlines()  # Create copy of file lines before rewrite
    file = open(location, mode="w+", errors="replace")
    memory = ' ' * len(target_string)  # Allocate space for character substitution

    for x, line in enumerate(file_lines):
        new_line = ""
        for char in line:
            new_line += char
            memory = memory[1:] + char  # Add the new character to the end of the memory string while removing the first
            if memory == target_string:
                new_line = new_line[:len(new_line) - len(memory)] + result  # Replace the segment of the line
        try:
            file.write(new_line + "\n")
            file.flush()
        except Exception:
            pass


def identifyFiles(location: str, target_file: str, target_string: str, result: str):
    fileList = []
    files = os.listdir(location)  # Find all files
    for file in files:
        if '.' in file and file.split('.')[1] == target_file:  # Identify target file types
            fileList.append(file)
    return fileList


def convertFileTypesInFolders(location: str, target_file: str, target_string: str, result: str):
    identifyFiles(location, target_file, target_string, result)  # Convert all files within starting folder
    exploreFolders([], location, target_file, target_string, result)  # Begin recursive statement from folder


def exploreFolders(visited: list[str], location: str, target_file: str, target_string: str, result: str):
    if location not in visited:
        visited.append(location)  # Ensure no locked exploration loops
        identifyFiles(location, target_file, target_string, result)  # Convert files within explored folder
        for root, dirs, files in os.walk(location):
            for name in dirs:
                exploreFolders(visited, root + '/' + name, target_file, target_string, result)  # Start exploring all sub-folders
