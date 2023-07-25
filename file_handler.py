def get_file_path():
    file_path = input("Enter the absolute file path of the notes file (or press Enter for default location): ")
    if not file_path:
        file_path = "notes.txt"
    return file_path
