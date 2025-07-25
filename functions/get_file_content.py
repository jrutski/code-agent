import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    # if file path outside working dir
    full_working = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(
        os.path.join(working_directory, file_path))

    if not full_file_path.startswith(full_working):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # if file path is not a file
    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(full_file_path) > MAX_CHARS:
                file_content_string += f'[...File {
                    file_path} truncated at {MAX_CHARS} characters]'
        return file_content_string
    except Exception as e:
        return f'Error reading file "{full_file_path}": {e}'
