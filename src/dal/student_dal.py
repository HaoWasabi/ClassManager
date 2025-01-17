import sqlite3
from typing import Optional, List
from dto.student_dto import StudentDTO
from .base_dal import BaseDAL, logger

class StudentDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS student (
                    student_id INTEGER PRIMARY KEY,
                    class_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    bonus_summary INTEGER,
                    absence_summary INTEGER,
                    final_score REAL,
                    role INTEGER NOT NULL,
                    state INTEGER NOT NULL,
                    FOREIGN KEY(class_id) REFERENCES class(class_id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error creating table student: {e}")
        finally:
            self.close_connection()
            
    def insert(self, student: StudentDTO) -> Optional[int]:
        try:
            self.open_connection()
            self.cursor.execute('''INSERT INTO student (class_id, name, email, phone, bonus_summary, absence_summary, final_score, role, state) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (student.get_class_id(), student.get_name(), student.get_email(), student.get_phone(), student.get_bonus_summary(), student.get_absence_summary(), student.get_final_score(), student.get_role(), student.get_state()))
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error inserting student: {e}")
            return None
        finally:
            self.close_connection()
            
    def update(self, student: StudentDTO) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE student SET class_id = ?, name = ?, email = ?, phone = ?, bonus_summary = ?, absence_summary = ?, final_score = ?, role = ?, state = ? WHERE student_id = ? AND state = 1''', (student.get_class_id(), student.get_name(), student.get_email(), student.get_phone(), student.get_bonus_summary(), student.get_absence_summary(), student.get_final_score(), student.get_role(), student.get_state(), student.get_student_id()))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error updating student: {e}")
            return False
        finally:
            self.close_connection()
            
    def delete(self, student_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE student SET state = 0 WHERE student_id = ? AND state = 1''', (student_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting student: {e}")
            return False
        finally:
            self.close_connection()
            
    def undelete(self, student_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE student SET state = 1 WHERE student_id = ? AND state = 0''', (student_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error undeleting student: {e}")
            return False
        finally:
            self.close_connection()
            
    def get_all(self) -> List[StudentDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM student WHERE state = 1''')
            return [StudentDTO(*student) for student in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting all students: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_class_id(self, class_id: int) -> List[StudentDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM student WHERE class_id = ? AND state = 1''', (class_id,))
            return [StudentDTO(*student) for student in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting students by class id: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_id(self, student_id: int) -> Optional[StudentDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM student WHERE student_id = ? AND state = 1''', (student_id,))
            return StudentDTO(*self.cursor.fetchone())
        except sqlite3.Error as e:
            logger.error(f"Error getting student by id: {e}")
            return None
        finally:
            self.close_connection()