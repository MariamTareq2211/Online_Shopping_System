class User:
    def __init__(self,name, phone,email,gender,role,username,password):
        self.set_Name(name)
        self.set_Phone(phone)
        self.set_Email(email)
        self.set_Gender(gender)
        self.set_Role(role)
        self.set_Username(username)
        self.set_Password(password)

## Setters & Getters
    def set_Name(self,name):
        self.__Name = name
    def get_Name(self):
        return self.__Name
    
    def set_Phone(self,phone):
        self.__Phone = phone
    def get_Phone(self):
        return self.__Phone
    
    def set_Email(self,email):
        self.__Email = email
    def get_Email(self):
        return self.__Email
    
    def set_Gender(self,gender):
        self.__Gender = gender
    def get_Gender(self):
        return self.__Gender 

    def set_Role(self,role):
        self.__Role = role
    def get_Role(self):
        return self.__Role 
    
    def set_Username(self,username):
        self.__Username = username
    def get_Username(self):
        return self.__Username
    
    def set_Password(self,password):
        self.__Password = password
    def get_Password(self):
        return self.__Password
    
    def display_profile(self):
        print(f"""
                Name: {self.get_Name()}
                Phone Number: {self.get_Phone()}
                Email: {self.get_Email()}
                """)
