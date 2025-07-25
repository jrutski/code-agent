from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


# print(get_file_content("calculator", "lorem.txt"))

if __name__ == "__main__":
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py")
    ]

    for working_dir, file_path in test_cases:
        print(f"Result for {file_path}:")
        result = get_file_content(working_dir, file_path)
        print(result)
        print()

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
