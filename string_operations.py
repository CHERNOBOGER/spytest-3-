def get_string_length(s: str) -> int:
    return len(s)

def save_string_to_file(s: str, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write(s)