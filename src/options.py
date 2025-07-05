import directory
class Print:
    @staticmethod
    def returnLogo() -> None:
        """
        returns the logo
        """
        print(" _____ _____ __    _____    _____ _____ _____ _____ _____ _____ _____ _____ _____ ")
        print("|   __|     |  |  |   __|  |     | __  |   __|  _  |   | |     |__   |   __| __  |")
        print("|   __|-   -|  |__|   __|  |  |  |    -|  |  |     | | | |-   -|   __|   __|    -|")
        print("|__|  |_____|_____|_____|  |_____|__|__|_____|__|__|_|___|_____|_____|_____|__|__|")
        print("Type 'cmds' for list of commands. ")
        print("Type 'exit' or 'break' to exit. ")

    @staticmethod
    def printLine() -> None:
        """
        Just prints a line..
        """
        print("-------------------------------------------------")

    @staticmethod
    def printCommands(token: dict):
        """
        Prints the commands for the program\n
        :param: :token: dict
        """
        print("\n")
        Print.printLine()
        print("COMMAND LIST")
        for k, v in token["CMDS"].items():
            if k == "Note":
                print(v)
                print(f"Current Directory: {directory.Directory.getCurrentDirectory()}")
            else:
                print(f"{k} - {v}")
        Print.printLine()
        print("\n")
        