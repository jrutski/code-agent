from google import genai
from google.genai import types
from dotenv import load_dotenv
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function
from config import MAX_ITER
import os
import sys


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    i = 0
    while True:
        i += 1
        if i > MAX_ITER:
            print("Maximum iterations reached.")
            sys.exit(1)

        try:
            result = generate_content(client, messages, verbose)
            if result is not None:
                print(result)
                break
        except Exception as e:
            print(f'Error: from LLM generate content: {e}')


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt),
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {
              response.usage_metadata.candidates_token_count}")

    if response.candidates:
        for candidate in response.candidates:
            function_response = candidate.content
            messages.append(function_response)

    if not response.function_calls:
        return response.text

    func_responses = []

    for function_call_part in response.function_calls:
        func_return = call_function(function_call_part, verbose)
        if (
            not func_return.parts
            or not func_return.parts[0].function_response
        ):
            raise Exception("Fatal error, no response")
        if verbose:
            print(
                f"-> {func_return.parts[0].function_response.response['result']}")
        func_responses.append(func_return.parts[0])

    if not func_responses:
        raise Exception("Error: no responses generated")

    messages.append(types.Content(role="tool", parts=func_responses))


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


if __name__ == "__main__":
    main()
