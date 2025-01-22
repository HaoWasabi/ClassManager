from .singleton import Singleton
from dal.score_dal import ScoreDAL
from dto.score_dto import ScoreDTO
from typing import Optional, List

class ScoreBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__score_dal = ScoreDAL()
            self._initialized = True
            
    def create_table(self):
        self.__score_dal.create_table()
        
    def drop_table(self):
        self.__score_dal.drop_table()
        
    def clear_table(self):
        self.__score_dal.clear_table()
            
    def insert(self, score: ScoreDTO) -> Optional[int]:
        return self.__score_dal.insert(score)
    
    def update(self, score: ScoreDTO) -> bool:
        return self.__score_dal.update(score)
    
    def delete(self, score_id: int) -> bool:
        return self.__score_dal.delete(score_id)
    
    def undelete(self, score_id: int) -> bool:
        return self.__score_dal.undelete(score_id)
    
    def get_all(self) -> List[ScoreDTO]:
        return self.__score_dal.get_all()
    
    def get_by_id(self, score_id: int) -> Optional[ScoreDTO]:
        return self.__score_dal.get_by_id(score_id)
    
    def get_by_coefficient_id(self, coefficient_id: int) -> List[ScoreDTO]:
        return self.__score_dal.get_by_coefficient_id(coefficient_id)
    
    def get_by_student_id(self, student_id: int) -> List[ScoreDTO]:
        return self.__score_dal.get_by_student_id(student_id)
    
    def get_by_student_id_and_coefficient_id(self, student_id: int, coefficient_id: int) -> List[ScoreDTO]:
        return self.__score_dal.get_by_student_id_and_coefficient_id(student_id, coefficient_id)