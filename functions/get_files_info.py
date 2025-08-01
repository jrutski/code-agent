import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    full_working = os.path.abspath(working_directory)
    full_directory = os.path.abspath(
        os.path.join(working_directory, directory))

    if not full_directory.startswith(full_working):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_directory):
        return f'Error: "{directory}" is not a directory'

    try:
        ret_lines = []
        for file in os.listdir(full_directory):
            ret_str = ""

            size = os.path.getsize(os.path.join(full_directory, file))
            dir = os.path.isdir(os.path.join(full_directory, file))
            ret_str += f"{file}: file_size={size} bytes, is_dir={dir}"
            ret_lines.append(ret_str)
        return "\n".join(ret_lines)
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
