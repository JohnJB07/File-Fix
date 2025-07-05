import os, json

class Directory:
    def getJsonDirectory() -> str:
        """
        Return Json File Location\n
        :param: None
        """
        # Mind Boggling shit
        try:
            return os.path.join(os.path.dirname(os.path.realpath(__file__)), "package.json") 
        except FileNotFoundError:
            print("JSON file not found")
    
    def openJsonFile():
        """
        Opens the JSON file\n
        :param: None
        """
        print("Loading JSON...")
        json_file = str(Directory.getJsonDirectory())
        with open(json_file, "r") as file:
            json_dict = json.load(file)

        if json_dict != None:
            print("Successfully loaded JSON.")
            return json_dict
        else:
            print("JSON File could not be loaded.")
            return None

    def getCurrentDirectory() -> str:
        """
        Returns the current directory\n
        :param: None
        """
        return os.getcwd()

    def changeDirectory(token: str):
        """
        Takes a token string and changes the directory based on the token given\n
        :returns None:\n
        :param: :token: str
        """
        if os.path.isdir(token):
            try:
                os.chdir(token)
                print(f"Changed directory to: {Directory.getCurrentDirectory()}")
            except (TypeError, OSError) as e:
                print("Error: ", e) 

    def makeDirectory(token: str):
        """
        Creates a directory at current directory, will also check if the directory exists
        if yes, directory will not be created.\n
        :param: :token: -str
        """
        full_dir = os.path.join(Directory.getCurrentDirectory(), token)
        if os.path.exists(full_dir):
            print("Directory already exists.")
        else:
            os.mkdir(full_dir)
            print(f"Successfully created directory at: {full_dir}")

    def organizeDirectory(token: dict):
        pass
