from bll import * 
from dto import *
from utils.excel_file_handler import ExcelFileHandler

class CheckDatabase:
    @staticmethod
    def create_all_tables(arr_table):
        for table in arr_table:
            table().create_table()        
            
    @staticmethod
    def drop_all_tables(arr_table):
        for table in arr_table:
            table().drop_table()
            
    @staticmethod
    def clear_all_tables(arr_table):
        for table in arr_table:
            table().clear_table()     
            
    @staticmethod
    def insert_into_all_table():
        UserBLL().insert(UserDTO(1, 'a@gmail.com', '123'))
        TeacherBLL().insert(TeacherDTO(1, 'teacher1', 'a@gmail.com', '123', 1))
        ClassBLL().insert(ClassDTO(1, 1, 1, 'class1', ''))
        StudentBLL().insert(StudentDTO(1, 1, 'student1', 'a@gmail.com', '123', 0, 0, 0, 0))
        AbsenceBLL().insert(AbsenceDTO(1, 1, 'sick1', '2021-01-01'))
        BonusBLL().insert(BonusDTO(1, 1, 1, '2021-01-01', 1))
        CoefficientBLL().insert(CoefficientDTO(1, 1, "coefficient", 1.0, 1))
        ScoreBLL().insert(ScoreDTO(1, 1, 1, 'a', 1.0))
        
    @staticmethod
    def update_from_all_table():
        UserBLL().update(UserDTO(1, 'b@gmail.com', '456'))
        TeacherBLL().update(TeacherDTO(1, 'teacher2', 'b@gmail.com', '456', 1))
        ClassBLL().update(ClassDTO(1, 1, 1, 'class2', ''))
        StudentBLL().update(StudentDTO(1, 1, 'student2', 'b@gmail.com', '456', 0, 0, 0, 0))
        AbsenceBLL().update(AbsenceDTO(1, 1, 'sick2', '2004-01-01'))
        BonusBLL().update(BonusDTO(1, 1, 1, '2004-01-01', 1))
        CoefficientBLL().update(CoefficientDTO(1, 1, "coefficient2", 2.0, 1))
        ScoreBLL().update(ScoreDTO(1, 1, 1, 'b', 2.0))
    
    @staticmethod
    def delete_from_all_table(arr_table):
        for table in arr_table:
            table().delete(1)     
            
    @staticmethod
    def undelete_from_all_table(arr_table):
        for table in arr_table:
            table().undelete(1)    
        
    @staticmethod
    def get_all_before_print_all(arr_table):
        for table in arr_table:
            for i in table().get_all():
                print(i)
                
    @staticmethod
    def get_by_id_before_print_all(arr_table):
        for table in arr_table:
            print(table().get_by_id(1))
            
    @staticmethod
    def check_all(arr_table):
        CheckDatabase.clear_all_tables(arr_table)
        CheckDatabase.drop_all_tables(arr_table)
        CheckDatabase.create_all_tables(arr_table)
        CheckDatabase.insert_into_all_table()
        CheckDatabase.update_from_all_table()
        CheckDatabase.delete_from_all_table(arr_table)
        CheckDatabase.undelete_from_all_table(arr_table)
        CheckDatabase.get_all_before_print_all(arr_table)
        CheckDatabase.get_by_id_before_print_all(arr_table)   
        
class CheckExcel:
    @staticmethod
    def check_all():
        # Tạo thêm sheet mới
        ExcelFileHandler.add_sheet("Sheet2")
        ExcelFileHandler.add_sheet("Sheet3")
        
        # Xóa sheet vừa tạo
        ExcelFileHandler.delete_sheet("Sheet3")

        # Ghi dữ liệu vào một ô trong sheet
        ExcelFileHandler.write_cell("Sheet1", "A1", "Hello World")
        ExcelFileHandler.write_cell("Sheet1", "B1", "Hello World")
        ExcelFileHandler.write_cell("Sheet1", "A2", "Hello World")
        ExcelFileHandler.write_cell("Sheet2", "A1", "Hello World")
        ExcelFileHandler.write_cell("Sheet2", "A2", "Hello World")

        # Đọc dữ liệu từ file Excel
        data = ExcelFileHandler.read_excel("Sheet1")
        if data is not None:
            print("Dữ liệu từ file Excel:")
            print(data)
            
        # Xóa dữ liệu tại một ô
        ExcelFileHandler.delete_cell("Sheet2", "A1")
        
        # Xóa hàng thứ 2 trong sheet "Sheet1"
        ExcelFileHandler.delete_row("Sheet1", 2)

        # Xóa cột thứ 3 trong sheet "Sheet1"
        ExcelFileHandler.delete_column("Sheet1", 2)

    
if __name__ == '__main__':
    arr_table = [AbsenceBLL, BonusBLL, ClassBLL, CoefficientBLL, ScoreBLL, StudentBLL, TeacherBLL, UserBLL]
    CheckDatabase.check_all(arr_table)
    
    CheckExcel.check_all()