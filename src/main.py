from bll import * 

def create_all_tables():
    for table in [AbsenceBLL, BonusBLL, ClassBLL, CoefficientBLL, ScoreBLL, StudentBLL, TeacherBLL, UserBLL]:
        table().create_table()
        
if __name__ == '__main__':
    create_all_tables()