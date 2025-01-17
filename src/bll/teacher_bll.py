from .singleton import Singleton
from dal.teacher_dal import TeacherDAL
from dto.teacher_dto import TeacherDTO
from typing import Optional, List

class TeacherBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__teacher_dal = TeacherDAL()
            self._initialized = True
            
    def create_table(self):
        self.__teacher_dal.create_table()
        
    def insert(self, teacher: TeacherDTO) -> Optional[int]:
        return self.__teacher_dal.insert(teacher)
    
    def update(self, teacher: TeacherDTO) -> bool:
        return self.__teacher_dal.update(teacher)
    
    def delete(self, teacher_id: int) -> bool:
        return self.__teacher_dal.delete(teacher_id)
    
    def undelete(self, teacher_id: int) -> bool:
        return self.__teacher_dal.undelete(teacher_id)
    
    def get_all(self) -> List[TeacherDTO]:
        return self.__teacher_dal.get_all()
    
    def get_by_id(self, teacher_id: int) -> Optional[TeacherDTO]:
        return self.__teacher_dal.get_by_id(teacher_id)