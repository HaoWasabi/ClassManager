from .singleton import Singleton
from dal.bonus_dal import BonusDAL
from dto.bonus_dto import BonusDTO
from typing import Optional, List

class BonusBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__bonus_dal = BonusDAL()
            self._initialized = True
            
    def create_table(self):
        self.__bonus_dal.create_table()
            
    def insert(self, bonus: BonusDTO) -> Optional[int]:
        return self.__bonus_dal.insert(bonus)
    
    def update(self, bonus: BonusDTO) -> bool:
        return self.__bonus_dal.update(bonus)
    
    def delete(self, bonus_id: int) -> bool:
        return self.__bonus_dal.delete(bonus_id)
    
    def undelete(self, bonus_id: int) -> bool:
        return self.__bonus_dal.undelete(bonus_id)
    
    def get_all(self) -> List[BonusDTO]:
        return self.__bonus_dal.get_all()
    
    def get_by_id(self, bonus_id: int) -> Optional[BonusDTO]:
        return self.__bonus_dal.get_by_id(bonus_id)
    
    def get_by_student_id(self, student_id: int) -> List[BonusDTO]:
        return self.__bonus_dal.get_by_student_id(student_id)
    
    def get_by_date(self, date: str) -> List[BonusDTO]:
        return self.__bonus_dal.get_by_date(date)
    
    def get_by_student_id_and_date(self, student_id: int, date: str) -> List[BonusDTO]:
        return self.__bonus_dal.get_by_student_id_and_date(student_id, date)
    
    