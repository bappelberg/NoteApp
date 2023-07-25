def show_notes(file_path):
    try:
        with open(file_path, 'r') as file:
            notes = file.readlines()
            if notes:
                print('Your notes:')
                for index, note in enumerate(notes, 1):
                    print(f'{index}. {note.strip()}')
            else:
                print('No notes found.')
    except FileNotFoundError:
        print('File does not exist or could not be found.')


def add_note(file_path):
    note = input('Write your note: ')
    if not note:
        print('Cannot add an empty note.')
        return
    try:
        with open(file_path, 'a') as file:
            file.write(note + '\n')
            print('Note was successfully added')
    except FileNotFoundError:
        print('File does not exists or could not be found.')


def update_note(file_path):
    show_notes(file_path)
    try:
        with open(file_path, 'r') as file:
            notes = file.readlines()
            if not notes:
                return

        choice = int(input('Enter the id number of the note you want to update: '))
        if 1 <= choice <= len(notes):
            new_note = input('Write the new note: ')
            if not new_note:
                print('Cannot update to an empty note.')
                return
            notes[choice - 1] = new_note + '\n'
            with open(file_path, 'w') as file:
                file.writelines(notes)
                print('Note has been updated.')
        else:
            print('Invalid choice.')
    except ValueError:
        print('Invalid input. Please enter a valid number.')
    except FileNotFoundError:
        print('File does not exist or could not be found.')


def delete_note(file_path):
    show_notes(file_path)

    try:
        with open(file_path, 'r') as file:
            notes = file.readlines()
            if not notes:
                return
            index = int(input('Enter the id number of the note you want to delete: '))
            if 1 <= index <= len(notes):
                notes.pop(index - 1)
                with open(file_path, 'w') as file:
                    file.writelines(notes)
                print('Note deleted successfully.')
            else:
                print('Invalid ID number. Please enter a valid number.')
    except ValueError:
        print('Invalid input. Please enter a valid number.')
    except FileNotFoundError:
        print('File does not exist or could not be found.')

