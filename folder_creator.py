import os
import shutil


def new_folder(folder_name):
    """
    A function using os and shutil to create folders.
    Added functionality to delete folder if name already taken.

    :param folder_name: The name of the folder being created.
    :return: New created folder and test file.
    """
    try:
        os.mkdir(folder_name)
        print('New folder created.')

        file_path = os.path.join(folder_name)
        print(f"Constructed file path: {file_path}")

        root, ext = os.path.splitext(file_path)
        print(f'Root of the file path: {root}')
        print(f'Extension of the file path: {ext}')
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
        delete_folder(folder_name)


def delete_folder(folder_name):
    """
    Function to potentially delete similarly named folder.

    :param folder_name: folder to be deleted.
    :return: Deleted folder.
    """
    delet = input("""Would you like to delete this folder, yes or no?
    """)
    while delet:
        if delet == "yes":
            shutil.rmtree(folder_name)
            print('test_dir deleted')
            break
        elif delet == "no":
            print(f"{folder_name} will be kept.")
            break
        else:
            print("not a valid response")
            delet = input("""Would you like to delete this folder, yes or no?
    """)


def user_mover(source_folder):
    destination_folder = "temporary_folder"

    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
        print(f"Temporary folder '{destination_folder}' created.")

    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        shutil.move(file_path, destination_folder)
        print(f"Moved file '{file_path}' to '{destination_folder}'.")


def parse_log_file(source_file, target_directory):
    errors_file = os.path.join(target_directory, "errors.log")
    warnings_file = os.path.join(target_directory, "warnings.log")

    with open(source_file, 'r') as log_file, open(errors_file, 'w') as errors, open(warnings_file, 'w') as warnings:
        for line in log_file:
            if "ERROR" in line:
                errors.write(line)
            elif "WARNING" in line:
                warnings.write(line)


def sort_folders(folder):
    logs = os.path.join(folder, "logs")
    mail = os.path.join(folder, "mail")
    text = os.path.join(folder, "text")

    if not os.path.exists(logs):
        os.mkdir(logs)
    if not os.path.exists(mail):
        os.mkdir(mail)
    if not os.path.exists(text):
        os.mkdir(text)

    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if file_name.endswith(".log"):
            shutil.move(file_path, logs)
        elif file_name.endswith(".txt"):
            shutil.move(file_path, text)
        elif file_name.endswith(".mail"):
            shutil.move(file_path, mail)


# Usage example
# new_folder("test_folder")
# user_mover("user2")
# sort_folders("user2")
# parse_log_file("log2.log", "user2")
