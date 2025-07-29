import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    full_working = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(
        os.path.join(working_directory, file_path))

    if not full_file_path.startswith(full_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.lower().endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cmd = ['python3', file_path] + args
        print(f'Working: {full_working}')
        result = subprocess.run(
            cmd,
            cwd=full_working,
            capture_output=True,
            timeout=30,
            text=True
        )

        output = result.stdout.strip()
        error = result.stderr.strip()

        if not output and not error:
            return "No output produced"
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        return f'STDOUT: {output}, STDERR: {error}'

    except Exception as e:
        return f"Error: executing Python file: {e}"
