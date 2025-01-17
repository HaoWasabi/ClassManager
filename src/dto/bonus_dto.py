class BonusDTO:
    def __init__(self, bonus_id: int, student_id: int, amount: int, date: str, state: int):
        self.__bonus_id = bonus_id
        self.__student_id = student_id
        self.__amount = amount
        self.__date = date
        self.__state = state
        
    def __str__(self):
        return f"BonusDTO(bonus_id={self.__bonus_id}, student_id={self.__student_id}, amount={self.__amount}, date={self.__date})"
    
    def get_bonus_id(self):
        return self.__bonus_id
    
    def get_student_id(self):
        return self.__student_id
    
    def get_date(self):
        return self.__date
    
    def get_amount(self):
        return self.__amount
    
    def get_state(self):
        return self.__state
    
    def set_bonus_id(self, bonus_id: int):
        self.__bonus_id = bonus_id
        
    def set_student_id(self, student_id: int):
        self.__student_id = student_id
        
    def set_date(self, date: str):
        self.__date = date
        
    def set_amount(self, amount: int):
        self.__amount = amount
        
    def set_state(self, state: int):
        self.__state = state
        
        