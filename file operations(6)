import os 
import sys
def display_files():
    print("Enter path to traverse: ")
    root_dir = input()
    if os.path.exists(root_dir):
        dir_count = 0
        file_count = 0
        for dir_name, sub_dir_list, file_list in os.walk(root_dir):
            print(f"Found directory: {dir_name} \n")
            if os.path.normpath(root_dir) != os.path.normpath(dir_name):
                dir_count += 1
            for each_file_name in file_list:
                file_count += 1
                print(f"File name(s) {each_file_name} \n")
        print(f"Number of subdirectories are {dir_count} \n")
        print(f"Number of files are {file_count} \n")
        display_menu()
    else:
        print("Entered path doesn't exist")
        display_menu()
def copy_contents_to_file():
    source_file = input("Enter the Source file name: ")
    print("\n")
    destination_file = input("Enter the Destination file name: ")
    print("\n")
    try:
        with open(source_file) as in_file, open(destination_file, "w") as out_file:
            list_of_lines = in_file.readlines()
            for i in range(0, len(list_of_lines)):
                if i % 2 != 0:
                    out_file.write(list_of_lines[i])
    except IOError:
        print("Error in file names")
        print("File contents at odd lines copied to destination file \n")
    display_menu()
def display_menu():
    print("Enter your choice")
    print("Press 1 --> Display files and directories for a given path and their count")
    print("Press 2 --> Copy the contents present at odd lines to another file")
    print("Press 3 --> Exit the program")
    choice = int(input())
    if choice == 1:
        display_files()
    elif choice == 2:
        copy_contents_to_file()
    else:
        sys.exit()
if __name__ == "__main__":
    display_menu()
