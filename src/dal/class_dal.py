import sqlite3
from typing import Optional, List
from dto.class_dto import ClassDTO
from .base_dal import BaseDAL, logger

class ClassDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS class (
                    class_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    creator_id TEXT NOT NULL,
                    teacher_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    state INTEGER NOT NULL,
                    FOREIGN KEY (creator_id) REFERENCES user(user_id),
                    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error creating table class: {e}")
        finally:
            self.close_connection()
            
    def drop_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''DROP TABLE IF EXISTS class''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error dropping table class: {e}")
        finally:
            self.close_connection()
            
    def clear_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''DELETE FROM class''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error clearing table class: {e}")
        finally:
            self.close_connection()
            
    def insert(self, class_: ClassDTO) -> Optional[int]:
        try:
            self.open_connection()
            self.cursor.execute('''INSERT INTO class (creator_id, teacher_id, name, description, state) VALUES (?, ?, ?, ?, ?)''', (class_.get_creator_id(), class_.get_teacher_id(), class_.get_name(), class_.get_description(), class_.get_state()))
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error inserting class: {e}")
            return None
        finally:
            self.close_connection()
            
    def update(self, class_: ClassDTO) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE class SET creator_id = ?, teacher_id = ?, name = ?, description = ?, state = ? WHERE class_id = ? AND state = 1''', (class_.get_creator_id(), class_.get_teacher_id(), class_.get_name(), class_.get_description(), class_.get_state(), class_.get_class_id()))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error updating class: {e}")
            return False
        finally:
            self.close_connection()
            
            
    def delete(self, class_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE class SET state = 0 WHERE class_id = ? AND state = 1''', (class_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting class: {e}")
            return False
        finally:
            self.close_connection()
            
            
    def undelete(self, class_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE class SET state = 1 WHERE class_id = ? AND state = 0''', (class_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error undeleting class: {e}")
            return False
        finally:
            self.close_connection()
            
    def get_all(self) -> List[ClassDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT class_id, creator_id, teacher_id, name, description, state FROM class WHERE state = 1''')
            return [ClassDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting all classes: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_id(self, class_id: int) -> Optional[ClassDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT class_id, creator_id, teacher_id, name, description, state FROM class WHERE class_id = ? AND state = 1''', (class_id,))
            return ClassDTO(*self.cursor.fetchone())
        except sqlite3.Error as e:
            logger.error(f"Error getting class by class_id: {e}")
            return None
        finally:
            self.close_connection()
            
    def get_by_creator_id(self, creator_id: int) -> List[ClassDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT class_id, creator_id, teacher_id, name, description, state FROM class WHERE creator_id = ? AND state = 1''', (creator_id,))
            return [ClassDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting classes by creator id: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_teacher_id(self, teacher_id: int) -> List[ClassDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT class_id, creator_id, teacher_id, name, description, state FROM class WHERE teacher_id = ? AND state = 1''', (teacher_id,))
            return [ClassDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting classes by teacher id: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_creator_id_and_teacher_id(self, creator_id: int, teacher_id: int) -> List[ClassDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT class_id, creator_id, teacher_id, name, description, state FROM class WHERE creator_id = ? AND teacher_id = ? AND state = 1''', (creator_id, teacher_id))
            return [ClassDTO(*row) for row in self.cursor.fetchall()]
        except sqlite3.Error as e:
            logger.error(f"Error getting classes by creator and teacher id: {e}")
            return []
        finally:
            self.close_connection()