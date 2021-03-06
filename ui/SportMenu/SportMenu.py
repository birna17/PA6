import os

class SportMenu:
    def __init__(self,manager):
        self.manager = manager

    def sportMenu(self):
        sport_menu_selection = ""
        while sport_menu_selection != "9":
            print("1. Register new Sport")
            print("2. Remove Sport")
            print("3. List of all Sports")
            print("4. Detailed Info of Sport")
            print("5. Create a Group for Sport")
            print("9. Go Back")
            sport_menu_selection = input()
            os.system('cls')
            if sport_menu_selection == "1":
                self.manager.gotoClass("registersport")
            elif sport_menu_selection == "2":
                self.manager.gotoClass("removesport")
            elif sport_menu_selection == "3":
                self.manager.gotoClass("listofsports")
            elif sport_menu_selection == "4":
                self.manager.gotoClass("sportmembers")
            elif sport_menu_selection == "5":
                self.manager.gotoClass("groupsport")
            elif sport_menu_selection == "9":
                self.manager.gotoClass("mainmenu")