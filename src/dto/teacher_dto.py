class TeacherDTO:
    def __init__(self, teacher_id: int, name: str, email: str, phone: str, state: int = 1):
        self.__teacher_id = teacher_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__state = state
        
    def __str__(self):
        return f"TeacherDTO(teacher_id={self.__teacher_id}, name={self.__name}, email={self.__email}, phone={self.__phone}, state={self.__state})"
    
    def get_teacher_id(self):
        return self.__teacher_id
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_state(self):
        return self.__state
    
    def set_teacher_id(self, teacher_id: int):
        self.__teacher_id = teacher_id
        
    def set_name(self, name: str):
        self.__name = name
        
    def set_email(self, email: str):
        self.__email = email
        
    def set_phone(self, phone: str):
        self.__phone = phone
        
    def set_state(self, state: int):
        self.__state = state