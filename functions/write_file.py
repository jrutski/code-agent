import os


def write_file(working_directory, file_path, content):
    full_working = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(
        os.path.join(working_directory, file_path))

    if not full_file_path.startswith(full_working):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(os.path.dirname(full_file_path)):
        # write path doesn't exist, create it
        try:
            os.makedirs(os.path.dirname(full_file_path))
        except Exception as e:
            return f'Error: Creating path "{full_file_path}": {e}'

    try:
        with open(full_file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: unable to write file "{file_path}": {e}'
