import pandas
from openpyxl import load_workbook
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Lấy thư mục gốc của dự án
excel_path = os.path.join(base_dir, "ClassManager.xlsx")

class ExcelFileHandler:
    @staticmethod
    def read_excel(file_path):
        # Đọc file Excel có sẵn  
        return pandas.read_excel(file_path)
      
    @staticmethod      
    def save_excel(df, file_path):
        # Lưu file Excel đã cập nhật
        df.to_excel(file_path, index=False)
        wb = load_workbook(file_path)
        wb.save(file_path)
        