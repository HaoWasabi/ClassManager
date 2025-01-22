import sqlite3
from typing import Optional, List
from dto.bonus_dto import BonusDTO
from .base_dal import BaseDAL, logger

class BonusDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bonus (
                bonus_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                amount INTEGER NOT NULL,
                date TEXT NOT NULL,
                state INTEGER NOT NULL,
                FOREIGN KEY(student_id) REFERENCES student(student_id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error creating table bonus: {e}")
        finally:
            self.close_connection()
            
    def drop_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''DROP TABLE IF EXISTS bonus''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error dropping table bonus: {e}")
        finally:
            self.close_connection()
            
    def clear_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''DELETE FROM bonus''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error clearing table bonus: {e}")
        finally:
            self.close_connection()
            
    def insert(self, bonus: BonusDTO) -> Optional[int]:
        try:
            self.open_connection()
            self.cursor.execute('''INSERT INTO bonus (student_id, amount, date, state) VALUES (?, ?, ?, ?)''', (bonus.get_student_id(), bonus.get_amount(), bonus.get_date(), bonus.get_state()))
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error inserting bonus: {e}")
            return None
        finally:
            self.close_connection()
            
    def update(self, bonus: BonusDTO) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE bonus SET student_id = ?, amount = ?, date = ?, state = ? WHERE bonus_id = ? AND state = 1''', (bonus.get_student_id(), bonus.get_amount(), bonus.get_date(), bonus.get_state(), bonus.get_bonus_id()))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error updating bonus: {e}")
            return False
        finally:
            self.close_connection()
            
    def delete(self, bonus_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE bonus SET state = 0 WHERE bonus_id = ? AND state = 1''', (bonus_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting bonus: {e}")
            return False
        finally:
            self.close_connection()
            
    def undelete(self, bonus_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE bonus SET state = 1 WHERE bonus_id = ? AND state = 0''', (bonus_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error undeleting bonus: {e}")
            return False
        finally:
            self.close_connection()
            
    def get_all(self) -> List[BonusDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM bonus WHERE state = 1''')
            rows = self.cursor.fetchall()
            return [BonusDTO(*row) for row in rows]
        except sqlite3.Error as e:
            logger.error(f"Error getting bonuses: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_student_id(self, student_id: int) -> List[BonusDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM bonus WHERE student_id = ? AND state = 1''', (student_id,))
            rows = self.cursor.fetchall()
            return [BonusDTO(*row) for row in rows]
        except sqlite3.Error as e:
            logger.error(f"Error getting bonuses: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_date(self, date: str) -> List[BonusDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM bonus WHERE date = ? AND state = 1''', (date,))
            rows = self.cursor.fetchall()
            return [BonusDTO(*row) for row in rows]
        except sqlite3.Error as e:
            logger.error(f"Error getting bonuses: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_amount(self, amount: int) -> List[BonusDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM bonus WHERE amount = ? AND state = 1''', (amount,))
            rows = self.cursor.fetchall()
            return [BonusDTO(*row) for row in rows]
        except sqlite3.Error as e:
            logger.error(f"Error getting bonuses: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_student_id_and_date(self, student_id: int, date: str) -> List[BonusDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM bonus WHERE student_id = ? AND date = ? AND state = 1''', (student_id, date))
            rows = self.cursor.fetchall()
            return [BonusDTO(*row) for row in rows]
        except sqlite3.Error as e:
            logger.error(f"Error getting bonuses: {e}")
            return []
        finally:
            self.close_connection()
        
    def get_by_id(self, bonus_id: int) -> Optional[BonusDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM bonus WHERE bonus_id = ? AND state = 1''', (bonus_id,))
            row = self.cursor.fetchone()
            return BonusDTO(*row) if row else None
        except sqlite3.Error as e:
            logger.error(f"Error getting bonus: {e}")
            return None
        finally:
            self.close_connection()
            