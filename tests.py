from functions.get_files_info import get_files_info


if __name__ == "__main__":
    test_cases = [
        ("current directory", "calculator", "."),
        ("'pkg' directory", "calculator", "pkg"),
        ("'/bin' directory", "calculator", "/bin"),
        ("'../' directory", "calculator", "../")
    ]

    for description, working_dir, directory in test_cases:
        print(f"Result for {description}:")
        result = get_files_info(working_dir, directory)
        print(result)
        print()
