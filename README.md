# NoteApp
The NoteApp is a simple command-line note-taking application implemented in Python. It allows users to create, view, update, and delete notes stored in a text file. The application follows a modular structure, with separate files for different functionalities.

How to Use

Clone the repository:

bash
Copy code
git clone <repository_url>
Navigate to the cloned repository:

bash
Copy code
cd NoteApp
Install Python (if not already installed).

Run the application:

css
Copy code
python main.py
The application will prompt you to enter the absolute file path of the notes file or press Enter to use the default location ("notes.txt") for storing the notes.

Once the application starts, you'll see the main menu with the following options:

Show notes
Add note
Update note
Remove note
Quit
Choose the desired option by entering the corresponding number (1, 2, 3, 4, or 5) and follow the prompts to perform the respective action.

NotesManager Functions

show_notes(file_path): Displays all existing notes in the specified file.
add_note(file_path): Adds a new note to the specified file.
update_note(file_path): Updates an existing note in the specified file.
delete_note(file_path): Deletes a note from the specified file.
Menu Function

print_menu(): Prints the main menu options for the user.
File Handler Function

get_file_path(): Gets the absolute file path of the notes file from the user or uses the default location ("notes.txt") if no path is provided.
Contributing
Contributions to this project are welcome! If you have any bug fixes, feature suggestions, or improvements, feel free to create a pull request or open an issue in the repository.

Author

Name: Benjamin Appelberg
GitHub: https://github.com/bappelberg/NoteApp/

Feel free to customize the README file with your project-specific details and update the contact information with your own. This README serves as the documentation and landing page for your NoteApp project, providing essential information to users and potential contributors.
