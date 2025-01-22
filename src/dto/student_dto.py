class StudentDTO:
    def __init__(self, student_id: int, class_id: int, name: str, email: str, phone: str, bonus_summary: int, absence_summary: int, final_score: float, role: int, state: int = 1):
        self.__student_id = student_id
        self.__class_id = class_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__bonus_summary = bonus_summary
        self.__absence_summary = absence_summary
        self.__final_score = final_score
        self.__role = role
        self.__state = state
        
    def __str__(self):
        return f"StudentDTO(student_id={self.__student_id}, class_id={self.__class_id}, name={self.__name}, email={self.__email}, phone={self.__phone}, bonus_summary={self.__bonus_summary}, absence_summary={self.__absence_summary}, final_score={self.__final_score}, role={self.__role}, state={self.__state})"
    
    def get_student_id(self):
        return self.__student_id
    
    def get_class_id(self):
        return self.__class_id
    
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    
    def get_bonus_summary(self):
        return self.__bonus_summary
    
    def get_absence_summary(self):
        return self.__absence_summary
    
    def get_final_score(self):
        return self.__final_score
    
    def get_role(self):
        return self.__role
    
    def get_state(self):
        return self.__state
    
    def set_student_id(self, student_id: int):
        self.__student_id = student_id
        
    def set_class_id(self, class_id: int):
        self.__class_id = class_id
        
    def set_name(self, name: str):
        self.__name = name
        
    def set_email(self, email: str):
        self.__email = email
        
    def set_phone(self, phone: str):
        self.__phone = phone
        
    def set_bonus_summary(self, bonus_summary: int):
        self.__bonus_summary = bonus_summary
        
    def set_absence_summary(self, absence_summary: int):
        self.__absence_summary = absence_summary
        
    def set_final_score(self, final_score: float):
        self.__final_score = final_score
        
    def set_role(self, role: int):
        self.__role = role
        
    def set_state(self, state: int):
        self.__state = state
        