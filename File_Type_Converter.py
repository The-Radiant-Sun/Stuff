import os


def convertFileType(location: str, target: str, result: str):
    print(f"Replacing {target} with {result} in {location.split('/')[-1]}")
    files = os.listdir(location)  # Find all files
    for file in files:
        if '.' in file and file.split('.')[1] == target:  # Identify target file types
            os.rename('/'.join([location, file]), '.'.join(['/'.join([location, file.split('.')[0]]), result]))  # Switch types


def convertFileTypesInFolders(location: str, target: str, result: str):
    convertFileType(location, target, result)  # Convert all files within starting folder
    exploreFolders([], location, target, result)  # Begin recursive statement from folder


def exploreFolders(visited: list[str], location: str, target: str, result: str):
    if location not in visited:
        visited.append(location)  # Ensure no locked exploration loops
        convertFileType(location, target, result)  # Convert files within explored folder
        for root, dirs, files in os.walk(location):
            for name in dirs:
                exploreFolders(visited, root + '/' + name, target, result)  # Start exploring all sub-folders
