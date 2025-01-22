from .singleton import Singleton
from dal.absence_dal import AbsenceDAL
from dto.absence_dto import AbsenceDTO
from typing import Optional, List

class AbsenceBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__absence_dal = AbsenceDAL()
            self._initialized = True
            
    def create_table(self):
        self.__absence_dal.create_table()
            
    def drop_table(self):
        self.__absence_dal.drop_table()
        
    def clear_table(self):
        self.__absence_dal.clear_table()
        
    def insert(self, absence: AbsenceDTO) -> Optional[int]:
        return self.__absence_dal.insert(absence)
    
    def update(self, absence: AbsenceDTO) -> bool:
        return self.__absence_dal.update(absence)
    
    def delete(self, absence_id: int) -> bool:
        return self.__absence_dal.delete(absence_id)
    
    def undelete(self, absence_id: int) -> bool:
        return self.__absence_dal.undelete(absence_id)
    
    def get_all(self) -> List[AbsenceDTO]:
        return self.__absence_dal.get_all()
    
    def get_by_id(self, absence_id: int) -> Optional[AbsenceDTO]:
        return self.__absence_dal.get_by_id(absence_id)
    
    def get_by_student_id(self, student_id: int) -> List[AbsenceDTO]:
        return self.__absence_dal.get_by_student_id(student_id)
    
    def get_by_date(self, date: str) -> List[AbsenceDTO]:
        return self.__absence_dal.get_by_date(date)
    
    def get_by_student_id_and_date(self, student_id: int, date: str) -> List[AbsenceDTO]:
        return self.__absence_dal.get_by_student_id_and_date(student_id, date)
    
