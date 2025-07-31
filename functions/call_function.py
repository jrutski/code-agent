from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    if verbose:
        print(f"Calling function: {
              function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_conversions = {
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
        "get_files_info": get_files_info
    }

    if function_call_part.name not in function_conversions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    function_to_call = function_conversions[function_call_part.name]

    args_list = {**function_call_part.args,
                 **{"working_directory": "./calculator"}}

    function_result = function_to_call(**args_list)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
