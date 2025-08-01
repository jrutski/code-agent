from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


if __name__ == "__main__":
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py")
    ]

    for item in test_cases:
        working_dir, file_path, *rest = item
        args = rest[0] if rest else []
        print(f"Result for {file_path}:")
        result = run_python_file(working_dir, file_path, args)
        print(result)
        print()

# if __name__ == "__main__":
#    test_cases = [
#        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
#        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
#        ("calculator", "/tmp/temp.txt", "this should not be allowed")
#    ]
#
#    for working_dir, file_path, content in test_cases:
#        print(f"Result for {file_path}:")
#        result = write_file(working_dir, file_path, content)
#        print(result)
#        print()

# print(get_file_content("calculator", "lorem.txt"))

# if __name__ == "__main__":
#    test_cases = [
#        ("calculator", "main.py"),
#        ("calculator", "pkg/calculator.py"),
#        ("calculator", "/bin/cat"),
#        ("calculator", "pkg/does_not_exist.py")
#    ]
#
#    for working_dir, file_path in test_cases:
#        print(f"Result for {file_path}:")
#        result = get_file_content(working_dir, file_path)
#        print(result)
#        print()

#
# if __name__ == "__main__":
#    test_cases = [
#        ("current directory", "calculator", "."),
#        ("'pkg' directory", "calculator", "pkg"),
#        ("'/bin' directory", "calculator", "/bin"),
#        ("'../' directory", "calculator", "../")
#    ]
#
#    for description, working_dir, directory in test_cases:
#        print(f"Result for {description}:")
#        result = get_files_info(working_dir, directory)
#        print(result)
#        print()
