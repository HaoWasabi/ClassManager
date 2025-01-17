import sqlite3
from typing import Optional, List
from dto.score_dto import ScoreDTO
from .base_dal import BaseDAL, logger

class ScoreDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS score (
                    score_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    coefficient_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    score REAL NOT NULL,
                    state INTEGER NOT NULL,
                    FOREIGN KEY(student_id) REFERENCES student(student_id)
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error creating table score: {e}")
        finally:
            self.close_connection()
            
    def insert(self, score: ScoreDTO) -> Optional[int]:
        try:
            self.open_connection()
            self.cursor.execute('''INSERT INTO score (student_id, coefficient_id, name, score, state) VALUES (?, ?, ?, ?, ?)''', (score.get_student_id(), score.get_coefficient_id(), score.get_name(), score.get_score(), score.get_state()))
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            logger.error(f"Error inserting score: {e}")
            return None
        finally:
            self.close_connection()
            
    def update(self, score: ScoreDTO) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE score SET student_id = ?, coefficient_id = ?, name = ?, score = ?, state = ? WHERE score_id = ? AND state = 1''', (score.get_student_id(), score.get_coefficient_id(), score.get_name(), score.get_score(), score.get_state(), score.get_id()))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error updating score: {e}")
            return False
        finally:
            self.close_connection()
            
    def delete(self, score_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE score SET state = 0 WHERE score_id = ? AND state = 1''', (score_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error deleting score: {e}")
            return False
        finally:
            self.close_connection
            
    def undelete(self, score_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE score SET state = 1 WHERE score_id = ? AND state = 0''', (score_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            logger.error(f"Error undeleting score: {e}")
            return False
        finally:
            self.close_connection()
            
    def get_all(self) -> List[ScoreDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM score WHERE state = 1''')
            scores = self.cursor.fetchall()
            return [ScoreDTO(*score) for score in scores]
        except sqlite3.Error as e:
            logger.error(f"Error getting all scores: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_student_id(self, student_id: int) -> List[ScoreDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM score WHERE student_id = ? AND state = 1''', (student_id,))
            scores = self.cursor.fetchall()
            return [ScoreDTO(*score) for score in scores]
        except sqlite3.Error as e:
            logger.error(f"Error getting scores by student id: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_coefficient_id(self, coefficient_id: int) -> List[ScoreDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM score WHERE coefficient_id = ? AND state = 1''', (coefficient_id,))
            scores = self.cursor.fetchall()
            return [ScoreDTO(*score) for score in scores]
        except sqlite3.Error as e:
            logger.error(f"Error getting scores by coefficient id: {e}")
            return []
        finally:
            self.close_connection()
            
    def get_by_student_id_and_coefficient_id(self, student_id: int, coefficient_id: int) -> Optional[ScoreDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM score WHERE student_id = ? AND coefficient_id = ? AND state = 1''', (student_id, coefficient_id))
            score = self.cursor.fetchone()
            return ScoreDTO(*score) if score else None
        except sqlite3.Error as e:
            logger.error(f"Error getting score by student id and coefficient id: {e}")
            return None
        finally:
            self.close_connection()
        
    def get_by_id(self, score_id: int) -> Optional[ScoreDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT * FROM score WHERE score_id = ? AND state = 1''', (score_id,))
            score = self.cursor.fetchone()
            return ScoreDTO(*score) if score else None
        except sqlite3.Error as e:
            logger.error(f"Error getting score by id: {e}")
            return None
        finally:
            self.close_connection()
        