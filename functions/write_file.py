import os


def write_file(working_directory, file_path, content):
    full_working = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(
        os.path.join(working_directory, file_path))

    if not full_file_path.startswith(full_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
