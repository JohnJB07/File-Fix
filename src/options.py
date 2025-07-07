import directory
class Print:
    @staticmethod
    def returnLogo() -> None:
        """
        returns the logo
        """
        
        print("   __ _ _                      _             ")
        print("  / _|_| | ___ _ __ ___   __ _| | _____ _ __ ")
        print(" | |_| | |/ _ \ '_ ` _ \ / _` | |/ / _ \ '__|")
        print(" |  _| | |  __/ | | | | | (_| |   <  __/ |   ")
        print(" |_| |_|_|\___|_| |_| |_|\__,_|_|\_\___|_|   ")
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
        
