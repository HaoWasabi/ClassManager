class CoefficientDTO:
    def __init__(self, coefficient_id: int, creator_id: int, name: str, value: float, state: int):
        self.__coefficient_id = coefficient_id
        self.__creator_id = creator_id
        self.__name = name
        self.__value = value
        self.__state = state
        
    def __str__(self):
        return f"CoefficientDTO(coefficient_id={self.__coefficient_id}, creator={self.__creator_id}, name={self.__name}, value={self.__value}, state={self.__state} )"
 
    def get_coefficient_id(self):
        return self.__coefficient_id
     
    def get_creator_id(self):
        return self.__creator_id
    
    def get_name(self):
        return self.__name
    
    def get_value(self):
        return self.__value
    
    def get_state(self):
        return self.__state
    
    def set_coefficient_id(self, coefficient_id: int):
        self.__coefficient_id = coefficient_id
    
    def set_creator_id(self, creator_id: int):
        self.__creator_id = creator_id
    
    def set_name(self, name: str):
        self.__name = name
        
    def set_value(self, value: float):
        self.__value = value
        
    def set_state(self, state: int):
        self.__state = state 
        