class AbsenceDTO:
    def __init__(self, absence_id: int, student_id: int, reason: str, date: str, state: int):
        self.__absence_id = absence_id
        self.__student_id = student_id
        self.__reason = reason
        self.__date = date
        self.__state = state
        
    def __str__(self):
        return f"AbsenceDTO(absence_id={self.__absence_id}, student_id={self.__student_id}, reason={self.__reason}, date={self.__date}, state={self.__state})"
    
    def get_absence_id(self):
        return self.__absence_id
    
    def get_student_id(self):
        return self.__student_id
    
    def get_date(self):
        return self.__date
    
    def get_reason(self):
        return self.__reason
    
    def get_state(self):
        return self.__state
    
    def set_absence_id(self, absence_id: int):
        self.__absence_id = absence_id
        
    def set_student_id(self, student_id: int):
        self.__student_id = student_id
        
    def set_date(self, date: str):
        self.__date = date
        
    def set_reason(self, reason: str):
        self.__reason = reason
        
    def set_state(self, state: int):
        self.__state = state