from .singleton import Singleton
from dal.student_dal import StudentDAL
from dto.student_dto import StudentDTO
from typing import Optional, List

class StudentBLL(Singleton): 
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__student_dal = StudentDAL()
            self._initialized = True
            
    def create_table(self):
        self.__student_dal.create_table()
        
    def insert(self, student: StudentDTO) -> Optional[int]:
        return self.__student_dal.insert(student)
    
    def update(self, student: StudentDTO) -> bool:
        return self.__student_dal.update(student)
    
    def delete(self, student_id: int) -> bool:
        return self.__student_dal.delete(student_id)
    
    def undelete(self, student_id: int) -> bool:
        return self.__student_dal.undelete(student_id)
    
    def get_all(self) -> List[StudentDTO]:
        return self.__student_dal.get_all()
    
    def get_by_class_id(self, class_id: int) -> List[StudentDTO]:
        return self.__student_dal.get_by_class_id(class_id)
                                                  
    def get_by_id(self, student_id: int) -> Optional[StudentDTO]:
        return self.__student_dal.get_by_id(student_id)
    