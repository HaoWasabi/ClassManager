from .singleton import Singleton
from dal.user_dal import UserDAL
from dto.user_dto import UserDTO
from typing import Optional, List

class UserBLL(Singleton):
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__user_dal = UserDAL()
            self._initialized = True
            
    def create_table(self):
        self.__user_dal.create_table()
        
    def insert(self, user: UserDTO) -> Optional[int]:
        return self.__user_dal.insert(user)
    
    def update(self, user: UserDTO) -> bool:
        return self.__user_dal.update(user)
    
    def delete(self, user_id: int) -> bool:
        return self.__user_dal.delete(user_id)
    
    def undelete(self, user_id: int) -> bool:
        return self.__user_dal.undelete(user_id)
    
    def get_all(self) -> List[UserDTO]:
        return self.__user_dal.get_all()
    
    def get_by_email(self, email: str) -> Optional[UserDTO]:
        return self.__user_dal.get_by_email(email)
    
    def get_by_id(self, user_id: int) -> Optional[UserDTO]:
        return self.__user_dal.get_by_id(user_id)