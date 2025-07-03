import os

class Drive():
    def getCurrentDrive():
        """
        :returns str of current drive:
        """
        return os.getcwd()

    def changeDir():
        """
        :returns change drive of os:\n
        :param drive_name: str
        """
        try:
            drive = input("Input drive name, leave as blank for default (C:)\nInput here: ")
            os.chdir(drive)
            print(f"Changed directory to: {os.getcwd()}")
        except Exception as e:
            print("Error could not change directory.", e)