import os

class RegisterMember:
    def __init__(self, manager):
        self.manager = manager
    
    def registerMember(self):
        os.system('cls')
        print('Please input member information\n')
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')
        year_of_birth = input('Year of birth: ')
        #græja virknina bakvið return
        self.manager.model_members.add_member(name,phone,email,year_of_birth)
        os.system('cls')
        print("Member Registered!\n")
        return
