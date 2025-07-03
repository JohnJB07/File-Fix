import json, pprint
class Options():
    def cmds():
        """
        :returns: command list  
        :param: None
        """
        with open("config.json", "r") as file:
            dictionary = json.load(file)
            print("COMMANDS:")    
            for items in dictionary["Commands"]:
                pprint.pprint(items)