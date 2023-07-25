from notes_manager import show_notes, add_note, update_note, delete_note
from menu import print_menu
from file_handler import get_file_path


def main():
    file_path = get_file_path()
    print('Welcome to NoteApp')
    while True:
        print_menu()
        choice = input('Enter your choice (1/2/3/4/5): ')
        if choice == '1':
            show_notes(file_path)
        elif choice == '2':
            add_note(file_path)
        elif choice == '3':
            update_note(file_path)
        elif choice == '4':
            delete_note(file_path)
        elif choice == '5':
            print('Quitting...')
            break


if __name__ == '__main__':
    main()
