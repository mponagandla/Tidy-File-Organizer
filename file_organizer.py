import filetype
import os
import pathlib

DOWNLOADS_DIR = "/Users/manojponagandla/Downloads"
DESKTOP_DIR = "/Users/manojponagandla/Desktop"


class FileOrganizer:
    def __init__(self, directories):
        self.directories = directories
        self.iter = None
        self.fileMap = {}

    def retrieve_files_directories(self):
        file_paths_list = []
        for directory in self.directories:
            self.iter = pathlib.Path(directory)
            directories = self.iter.iterdir()
            for dir in directories:
                file_paths_list.append(dir)
                if not dir.is_dir():
                    with open(dir, "rb") as file:
                        info = filetype.guess(dir)
                        if info is not None:
                            self.fileMap[os.path.basename(dir)] = {
                                "current_dir": dir.absolute(),
                                "file_type": info.MIME
                            }
                        else:
                            self.fileMap[dir] = 'None'
                else:
                    self.fileMap[dir] = 'Directory'

        return file_paths_list
    # TODO: Move each file to the respective folder
    # TODO: Documents/Tidy/Month/Week/FileType/name_MMDDYYYY.type

    def cleanup(self):
        files = self.retrieve_files_directories()


if __name__ == '__main__':
    file_organizer = FileOrganizer([DOWNLOADS_DIR])
    file_organizer.cleanup()
    for key in file_organizer.fileMap:
        print(key, " ", file_organizer.fileMap[key])
