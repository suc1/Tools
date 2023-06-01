import os
import re

def convert_variable_name(variable_name):
    parts = variable_name.split('_')
    new_parts = [parts[0]] + [part.capitalize() for part in parts[1:]]
    return 'binding.' + ''.join(new_parts)

def process_file(file_path):
    file_name, file_ext = os.path.splitext(file_path)
    new_file_path = file_name + '1' + file_ext

    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to find and replace variable names
    pattern = r'[a-z]+_[a-z0-9_]*'
    new_variable_name = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), content)
    # new_variable_name = 'binding.' + new_variable_name

    with open(new_file_path, 'w') as new_file:
        new_file.write(new_variable_name)

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.kt'):
                file_path = os.path.join(root, file)
                process_file(file_path)

def main_path():
    directory = input('Pls input start path:')
    process_directory(directory)
    print('Done')

def main_file():
    fileName = input('Pls input file name:')
    process_file(fileName)
    print('Done')

if __name__ == '__main__':
    main_file()