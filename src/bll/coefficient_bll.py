from .singleton import Singleton
from dal.coefficient_dal import CoefficientDAL
from dto.coefficient_dto import CoefficientDTO
from typing import Optional, List

class CoefficientBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__coefficient_dal = CoefficientDAL()
            self._initialized = True
            
    def create_table(self):
        self.__coefficient_dal.create_table()
        
    def insert(self, coefficient: CoefficientDTO) -> Optional[int]:
        return self.__coefficient_dal.insert(coefficient)
    
    def update(self, coefficient: CoefficientDTO) -> bool:
        return self.__coefficient_dal.update(coefficient)
    
    def delete(self, coefficient_id: int) -> bool:
        return self.__coefficient_dal.delete(coefficient_id)
    
    def undelete(self, coefficient_id: int) -> bool:
        return self.__coefficient_dal.undelete(coefficient_id)
    
    def get_all(self) -> List[CoefficientDTO]:
        return self.__coefficient_dal.get_all()
    
    def get_by_creator_id(self, creator_id: int) -> List[CoefficientDTO]:
        return self.__coefficient_dal.get_by_creator_id(creator_id)
    
    def get_by_id(self, coefficient_id: int) -> Optional[CoefficientDTO]:
        return self.__coefficient_dal.get_by_id(coefficient_id)
    
    