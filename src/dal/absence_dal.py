import sqlite3
from typing import Optional, List
from dto.absence_dto import AbsenceDTO
from .base_dal import BaseDAL, logger

class AbsenceDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS absence (
                    absence_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    reason TEXT,
                    date TEXT NOT NULL,
                    state INTEGER NOT NULL,
                    FOREIGN KEY(student_id) REFERENCES student(student_id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error creating table absence: {e}")
        finally:
            self.close_connection()
            
    def insert(self, absence: AbsenceDTO) -> Optional[int]:
        try:
            self.open_connection()
            self.cursor.execute('''INSERT INTO absence (student_id, reason, date, state) VALUES (?, ?, ?, ?)''', (absence.get_student_id(), absence.get_reason(), absence.get_date(), absence.get_state()))
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error inserting absence: {e}")
            return None
        finally:
            self.close_connection()
            
    def update(self, absence: AbsenceDTO) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE absence SET student_id = ?, reason = ?, date = ?, state = ? WHERE absence_id = ? AND state = 1''', (absence.get_student_id(), absence.get_reason(), absence.get_date(), absence.get_state(), absence.get_absence_id()))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error updating absence: {e}")
            return False
        finally:
            self.close_connection()
            
    def delete(self, absence_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE absence SET state = 0 WHERE absence_id = ? AND state = 1''', (absence_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting absence: {e}")
            return False
        finally:
            self.close_connection()
            
    def undelete(self, absence_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE absence SET state = 1 WHERE absence_id = ? AND state = 0''', (absence_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error undeleting absence: {e}")
            return False
        finally:
            self.close_connection()
            
    def get_all(self) -> List[AbsenceDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT absence_id, student_id, reason, date, state FROM absence WHERE state = 1''')
            return [AbsenceDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting all absences: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_id(self, absence_id: int) -> Optional[AbsenceDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT absence_id, student_id, reason, date, state FROM absence WHERE absence_id = ? AND state = 1''', (absence_id,))
            return AbsenceDTO(*self.cursor.fetchone())
        except sqlite3.Error as e:
            logger.error(f"Error getting absence by absence_id: {e}")
            return None
        finally:
            self.close_connection()
            
    def get_by_student_id(self, student_id: int) -> List[AbsenceDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT absence_id, student_id, reason, date, state FROM absence WHERE student_id = ? AND state = 1''', (student_id,))
            return [AbsenceDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting absences by student id: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_date(self, date: str) -> List[AbsenceDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT absence_id, student_id, reason, date, state FROM absence WHERE date = ? AND state = 1''', (date,))
            return [AbsenceDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting absences by date: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_student_id_and_date(self, student_id: int, date: str) -> List[AbsenceDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT absence_id, student_id, reason, date, state FROM absence WHERE student_id = ? AND date = ? AND state = 1''', (student_id, date))
            return [AbsenceDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting absences by student id and date: {e}")
            return []
        finally:
            self.close_connection()
            