import sqlite3
from typing import Optional, List
from dto.teacher_dto import TeacherDTO
from .base_dal import BaseDAL, logger

class TeacherDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS teacher (
                    teacher_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    state INTEGER NOT NULL
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f'Error creating teacher table: {e}')
        finally:
            self.close_connection()
            
    def insert(self, teacher: TeacherDTO) -> Optional[int]:
        try:
            self.open_connection()
            self.cursor.execute(
                '''
                INSERT INTO teacher (name, email, phone, state) VALUES (?, ?, ?, ?);
                ''',
                (teacher.get_name(), teacher.get_email(), teacher.get_phone(), teacher.get_state())
            )
            self.connection.commit()
            return teacher.get_teacher_id()
        except sqlite3.Error as e:
            logger.error(f'Error inserting Teacher: {e}')
            return None
        finally:
            self.close_connection()
            
    def update(self, teacher: TeacherDTO) -> bool:
        try:
            self.open_connection()
            self.cursor.execute(
                '''
                UPDATE teacher SET name = ?, email = ?, phone = ?, state = ? WHERE teacher_id = ? AND state = 1;
                ''',
                (teacher.get_name(), teacher.get_email(), teacher.get_phone(), teacher.get_state(), teacher.get_teacher_id())
            )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f'Error updating Teacher: {e}')
            return False
        finally:
            self.close_connection()
            
    def delete(self, teacher_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute(
                '''
                UPDATE teacher SET state = 0 WHERE teacher_id = ? AND state = 1;
                ''',
                (teacher_id,)
            )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f'Error deleting Teacher: {e}')
            return False
        finally:
            self.close_connection()
            
    def undelete(self, teacher_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute(
                '''
                UPDATE teacher SET state = 1 WHERE teacher_id = ? AND state = 0;
                ''',
                (teacher_id,)
            )
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f'Error undeleting Teacher: {e}')
            return False
        finally:
            self.close_connection()
            
    def get_all(self) -> List[TeacherDTO]:
        try:
            self.open_connection()
            self.cursor.execute(
                '''
                SELECT * FROM teacher WHERE state = 1;
                '''
            )
            return [TeacherDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f'Error getting all Teachers: {e}')
            return []
        finally:
            self.close_connection()
            
    def get_by_id(self, teacher_id: int) -> Optional[TeacherDTO]:
        try:
            self.open_connection()
            self.cursor.execute(
                '''
                SELECT * FROM teacher WHERE teacher_id = ? AND state = 1;
                ''',
                (teacher_id,)
            )
            return TeacherDTO(*self.cursor.fetchone())
        except sqlite3.Error as e:
            logger.error(f'Error getting teacher by ID: {e}')
            return None
        finally:
            self.close_connection()
            