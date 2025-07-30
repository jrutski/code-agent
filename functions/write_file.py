import os
from google.genai import types


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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes python file contents as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write the contents to, relative to the working directory. This parameter is required. If the file exists, it will be overwritten",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file. This parameter is required."
            ),
        },
        required=["file_path", "content"],
    ),
)
