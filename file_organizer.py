import fleep
import filetype
import os
import pathlib

DOWNLOADS_DIR = "/Users/manojponagandla/Downloads"
DESKTOP_DIR = "/Users/manojponagandla/Desktop"


class FileOrganizer:
    def __init__(self, directories):
        self.directories = directories
        self.iter = None
    # TODO: Get all the files list from all the directories

    def retrieve_files_directories(self):
        paths_list = []
        for directory in self.directories:
            self.iter = pathlib.Path(directory)
            directories = self.iter.iterdir()
            for dir in directories:
                paths_list.append(dir)
                # if not dir.is_dir():
                #     # type = filetype.guess(dir)
                #     # print(f"{dir} -{' dir' if dir.is_dir() else ' file'} - {type}")
                #     with open(dir, "rb") as file:
                #         info = fleep.get(file.read(128))
                #         #print(f"{dir} -{' dir' if dir.is_dir() else ' file'} - {info.type}")
                # else: print(f"{dir} - dir")

        return paths_list

    # TODO: Loop through each file to determine the file types
    # TODO: Move each file to the respective folder
    # TODO: Documents/Tidy/Month/Week/FileType/name_MMDDYYYY.type



    def cleanup(self):
        files = self.retrieve_files_directories()
        for file in files:
            print(file)

if __name__ == '__main__':
    file_organizer = FileOrganizer([DESKTOP_DIR])
    file_organizer.cleanup()