import sqlite3
from typing import Optional, List
from dto.coefficient_dto import CoefficientDTO
from .base_dal import BaseDAL, logger

class CoefficientDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS coefficient (
                    coefficent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    creator_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    value REAL NOT NULL,
                    state INTEGER NOT NULL,
                    FOREIGN KEY(creator_id) REFERENCES user(user_id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error creating table coefficient: {e}")
        finally:
            self.close_connection()
            
    def insert(self, coefficient: CoefficientDTO) -> Optional[int]:
        try:
            self.open_connection()
            self.cursor.execute('''INSERT INTO coefficient (creator_id, name, value, state) VALUES (?, ?, ?, ?)''', (coefficient.get_creator_id(), coefficient.get_name(), coefficient.get_value(), coefficient.get_state()))
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error inserting coefficient: {e}")
            return None
        finally:
            self.close_connection()
            
    def update(self, coefficient: CoefficientDTO) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE coefficient SET creator_id = ?, name = ?, value = ?, state = ? WHERE coefficent_id = ? AND state = 1''', (coefficient.get_creator_id(), coefficient.get_name(), coefficient.get_value(), coefficient.get_state(), coefficient.get_coefficient_id()))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error updating coefficient: {e}")
            return False
        finally:
            self.close_connection()
            
    def delete(self, coefficient_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE coefficient SET state = 0 WHERE coefficent_id = ? AND state = 1''', (coefficient_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting coefficient: {e}")
            return False
        finally:
            self.close_connection
            
    def undelete(self, coefficient_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE coefficient SET state = 1 WHERE coefficent_id = ? AND state = 0''', (coefficient_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error undeleting coefficient: {e}")
            return False
        finally:
            self.close_connection()
            
    def get_all(self) -> List[CoefficientDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM coefficient WHERE state = 1''')
            coefficients = self.cursor.fetchall()
            return [CoefficientDTO(*coefficient) for coefficient in coefficients]
        except sqlite3.Error as e:
            logger.error(f"Error getting all coefficients: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_creator_id(self, creator_id: int) -> List[CoefficientDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM coefficient WHERE creator_id = ? AND state = 1''', (creator_id,))
            coefficients = self.cursor.fetchall()
            return [CoefficientDTO(*coefficient) for coefficient in coefficients]
        except sqlite3.Error as e:
            logger.error(f"Error getting coefficients by creator id: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_id(self, coefficient_id: int) -> Optional[CoefficientDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM coefficient WHERE coefficent_id = ? AND state = 1''', (coefficient_id,))
            coefficient = self.cursor.fetchone()
            return CoefficientDTO(*coefficient) if coefficient else None
        except sqlite3.Error as e:
            logger.error(f"Error getting coefficient by id: {e}")
            return None
        finally:
            self.close_connection()
            
            
        