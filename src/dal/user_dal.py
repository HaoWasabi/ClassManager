import sqlite3
from typing import Optional, List
from dto.user_dto import UserDTO
from .base_dal import BaseDAL, logger

class UserDAL(BaseDAL):
    def __init__(self):
        super().__init__()
        
    def create_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    state INTEGER NOT NULL
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as error:
            logger.error(f'Error creating table user: {error}')
            raise error
        finally:
            self.close_connection()

    def drop_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''DROP TABLE IF EXISTS user''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error dropping table user: {e}")
        finally:
            self.close_connection()
            
    def clear_table(self):
        try:
            self.open_connection()
            self.cursor.execute('''DELETE FROM user''')
            self.connection.commit()
        except sqlite3.Error as e:
            logger.error(f"Error clearing table user: {e}")
        finally:
            self.close_connection()
            
    def insert(self, user: UserDTO) -> Optional[int]:
        try:
            self.open_connection()
            self.cursor.execute('''INSERT INTO user (email, password, state) VALUES (?, ?, ?)''', (user.get_email(), user.get_password(), user.get_state()))
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as error:
            logger.error(f'Error inserting user: {error}')
            raise error
        finally:
            self.close_connection()
            
    def update(self, user: UserDTO) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE user SET email = ?, password = ?, state = ? WHERE user_id = ? AND state = 1''', (user.get_email(), user.get_password(), user.get_state(), user.get_user_id()))
            self.connection.commit()
            return True
        except sqlite3.Error as error:
            logger.error(f'Error updating user: {error}')
            raise error
        finally:
            self.close_connection()
            
    def delete(self, user_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE user SET state = 0 WHERE user_id = ? AND state = 1''', (user_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as error:
            logger.error(f'Error deleting user: {error}')
            raise error
        finally:
            self.close_connection()
            
    def undelete(self, user_id: int) -> bool:
        try:
            self.open_connection()
            self.cursor.execute('''UPDATE user SET state = 1 WHERE user_id = ? AND state = 0''', (user_id,))
            self.connection.commit()
            return True
        except sqlite3.Error as error:
            logger.error(f'Error deleting user: {error}')
            raise error
        finally:
            self.close_connection()
            
    def get_all(self) -> List[UserDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT user_id, email, password, state FROM user WHERE state = 1''')
            users = [UserDTO(*row) for row in self.cursor.fetchall()]
            return users
        except sqlite3.Error as error:
            logger.error(f'Error getting all users: {error}')
            raise error
        finally:
            self.close_connection()
            
    def get_by_email(self, email: str) -> Optional[UserDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT user_id, email, password, state FROM user WHERE email = ? AND state = 1''', (email,))
            user = self.cursor.fetchone()
            return UserDTO(*user) if user else None
        except sqlite3.Error as error:
            logger.error(f'Error getting user by email: {error}')
            raise error
        finally:
            self.close_connection()
            
    def get_by_id(self, user_id: int) -> Optional[UserDTO]:
        try:
            self.open_connection()
            self.cursor.execute('''SELECT user_id, email, password, state FROM user WHERE user_id = ? AND state = 1''', (user_id,))
            user = self.cursor.fetchone()
            return UserDTO(*user) if user else None
        except sqlite3.Error as error:
            logger.error(f'Error getting user by id: {error}')
            raise error
        finally:
            self.close_connection()