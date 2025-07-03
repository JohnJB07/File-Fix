# Imports
import drive, logo, options, os

class Main():
    def __init__(self):
        self.exit = False
        self.userInput()

    # Handle user input for file organizer
    def userInput(self):

        # Print logo at start of program
        logo.Logo.printLogo()
        while not self.exit:
            print("-------------------------------------------------")
            self.user = input("Input here: ").lower()

            # If input is exit
            if self.user == "exit" or self.user == "0":
                self.exit = True

            # If input is cmds
            elif self.user == "cmds":
                if os.path.curdir == "C:\\file_fix\src":
                    options.Options.cmds()
                else:
                    os.chdir("C:\\file_fix\src")
                    options.Options.cmds()
                
            # If input is cd (Change Directory)
            elif self.user == "cd":
                drive.Drive.changeDir()

            # If input is get_cwd (Get Current Working Directory)
            elif self.user == "get_cwd":
                print(f"Working Directory: {drive.Drive.getCurrentDrive()}")

            # If input is organize (WIP)
            elif self.user == "organize":
                start_directory = "D:"
                try:
                    for file_path, names, files in os.walk(start_directory):
                        for filename in files:
                            full_path = os.path.join(file_path, filename)
                            print(f"File: {full_path}")
                    self.exit = True
                except FileNotFoundError:
                    print(f"Error: Directory '{start_directory}' not found.")
            else:
                pass

if __name__ == "__main__":
    Main()