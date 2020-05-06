import os
import shutil


def create_folders(directories, directory_path):
    """
    Create the folders in <directory_path> where the files will be moved to.
    :param directories: dictionary containing the names of the sorted folders and the extensions that correspond to those folders.
    :param directory_path: string of the path to the directory to be sorted.
    """
    for key in directories:
        if key not in os.listdir(directory_path):
            os.mkdir(directory_path + '/' + key)
    if "MISCELLANEA" not in os.listdir(directory_path):
        os.mkdir(directory_path + '/' + "MISCELLANEA")


def organize_folders(directories, directory_path):
    """
    Organizes the files in the specified folder into folders.
    :param directories: dictionary containing the names of the sorted folders and the extensions that correspond to those folders.
    :param directory_path: string of the path to the directory to be sorted.
    """
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + '/' + file):
            src_path = directory_path + '/' + file
            for key in directories:
                extension = directories[key]
                if file.endswith(extension):
                    dest_path = os.path.join(directory_path, key, file)
                    shutil.move(src_path, dest_path)
                    break


def organize_remaining_files(directory_path):
    """
    Assigns the file that don't have a corresponding folder to the <MISCELLANEA> directory.
    :param directory_path: string of the path to the directory to be sorted.
    """
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + '/' + file):
            src_path = directory_path + '/' + file
            dest_path = os.path.join(directory_path, "MISCELLANEA", file)
            shutil.move(src_path, dest_path)


if __name__ == '__main__':
    print("Folder fast selection (type the number instead of the path): ")
    # change the following lines for shortcut suggestion
    print(" 1 - First shortcut")
    print(" 2 - Second shortcut")
    # ======== end of shortcut suggestion ========
    user_input = input("Folder to sort (full path or from list): ")
    # change the following lines for pre-selected folders
    if user_input == '1':
        directory_path = "path to first folder"
    elif user_input == '2':
        directory_path = "path to second folder"    # ==== shortcuts end here ====
    else:
        directory_path = user_input
    directories = {
        "HTML": (".html5", ".html", ".htm", ".xhtml", ".css"),
        "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".heif"),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf",
                      ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"),
        "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma", ".flac", ".mid"),
        "TEXT": (".txt", ".in", ".out", ".ini"),
        "GRAPHICS": (".ai", ".psd", ".svg", ".eps", ".ttf", ".otf", ".abr"),
        "CODING": (".py", ".cpp", ".c", ".java", ".json", ".md"),
        "PDF": ".pdf",
        "EXE": ".exe",
        "MISCELLANEA": ""
    }
    create_folders(directories, directory_path)
    organize_folders(directories, directory_path)
    organize_remaining_files(directory_path)
    print("Done!")
