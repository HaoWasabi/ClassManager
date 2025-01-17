class ClassDTO:
    def __init__(self, class_id: int, creator_id: int, teacher_id: int, name: str, description: str, state: int):
        self.__class_id = class_id
        self.__creator_id = creator_id
        self.__teacher_id = teacher_id
        self.__name = name
        self.__description = description
        self.__state = state
        
    def __str__(self):
        return f"ClassDTO(class_id={self.__class_id}, creator_id={self.__creator_id}, teacher_id={self.__teacher_id}, name={self.__name}, description={self.__description}, state={self.__state})"
    
    def get_class_id(self):
        return self.__class_id
    
    def get_creator_id(self):
        return self.__creator_id
    
    def get_teacher_id(self):
        return self.__teacher_id
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_state(self):
        return self.__state
    
    def set_class_id(self, class_id: int):
        self.__class_id = class_id
        
    def set_creator_id(self, creator_id: int):
        self.__creator_id = creator_id
        
    def set_teacher_id(self, teacher_id: int):
        self.__teacher_id = teacher_id
        
    def set_name(self, name: str):
        self.__name = name
        
    def set_description(self, description: str):
        self.__description = description
        
    def set_state(self, state: int):
        self.__state = state
        