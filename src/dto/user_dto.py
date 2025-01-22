class UserDTO:
    def __init__(self, user_id: int, email: str, password: str, state: int = 1):
        self.__user_id = user_id
        self.__email = email
        self.__password = password
        self.__state = state
        
    def __str__(self):
        return f"UserDTO(user_id={self.__user_id}, email={self.__email}, password={self.__password}, state={self.__state})"
    
    def get_user_id(self):
        return self.__user_id
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    
    def get_state(self):
        return self.__state
    
    def set_user_id(self, user_id: int):
        self.__user_id = user_id
        
    def set_email(self, email: str):
        self.__email = email
        
    def set_password(self, password: str):
        self.__password = password
        
    def set_state(self, state: int):
        self.__state = state