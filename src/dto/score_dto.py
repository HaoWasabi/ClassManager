class ScoreDTO:
    def __init__(self, score_id: int, student_id: int, coefficient_id: int, name: str, score: float, state: int):
        self.__score_id = score_id
        self.__student_id = student_id
        self.__coefficient_id = coefficient_id
        self.__name = name
        self.__score = score
        self.__state = state
    
    def __str__(self):
        return f"ScoreDTO(score_id={self.__score_id}, student_id={self.__student_id}, coefficient_id={self.__coefficient_id}, name={self.__name}, score={self.__score}, state={self.__state})"
    
    def get_score_id(self):
        return self.__score_id
    
    def get_student_id(self):
        return self.__student_id
    
    def get_coefficient_id(self):
        return self.__coefficient_id
    
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def get_state(self):
        return self.__state
    
    def set_score_id(self, score_id: int):
        self.__score_id = score_id
        
    def set_student_id(self, student_id: int):
        self.__student_id = student_id
        
    def set_coefficient_id(self, coefficient_id: int):
        self.__coefficient_id = coefficient_id
        
    def set_name(self, name: str):
        self.__name = name
            
    def set_score(self, score: float):
        self.__score = score
        
    def set_state(self, state: int):
        self.__state = state
        