from .singleton import Singleton
from dal.class_dal import ClassDAL
from dto.class_dto import ClassDTO
from typing import Optional, List

class ClassBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__class_dal = ClassDAL()
            self._initialized = True
            
    def create_table(self):
        self.__class_dal.create_table()
        
    def drop_table(self):
        self.__class_dal.drop_table()
        
    def clear_table(self):
        self.__class_dal.clear_table()
        
    def insert(self, class_: ClassDTO) -> Optional[int]:
        return self.__class_dal.insert(class_)
    
    def update(self, class_: ClassDTO) -> bool:
        return self.__class_dal.update(class_)
    
    def delete(self, class_id: int) -> bool:
        return self.__class_dal.delete(class_id)
    
    def undelete(self, class_id: int) -> bool:
        return self.__class_dal.undelete(class_id)
    
    def get_all(self) -> List[ClassDTO]:
        return self.__class_dal.get_all()
    
    def get_by_id(self, class_id: int) -> Optional[ClassDTO]:
        return self.__class_dal.get_by_id(class_id)
    
    def get_by_creator_id(self, creator_id: int) -> List[ClassDTO]:
        return self.__class_dal.get_by_creator_id(creator_id)
    
    def get_by_teacher_id(self, teacher_id: int) -> List[ClassDTO]:
        return self.__class_dal.get_by_teacher_id(teacher_id)
    
    def get_by_creator_id_and_teacher_id(self, creator_id: int, teacher_id: int) -> List[ClassDTO]:
        return self.__class_dal.get_by_creator_id_and_teacher_id(creator_id, teacher_id)