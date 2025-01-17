from datetime import datetime

class DateTimeConverter:
    @staticmethod
    def current_datetime_to_string():
        """Chuyển thời gian hiện tại sang dạng chuỗi "dd-mm-yyyy"."""
        now = datetime.now()
        return now.strftime("%d-%m-%Y")

    @staticmethod
    def string_to_datetime(date_string):
        """Chuyển chuỗi "dd-mm-yyyy" sang đối tượng datetime."""
        try:
            return datetime.strptime(date_string, "%d-%m-%Y")
        except ValueError:
            raise ValueError(f"Chuỗi ngày giờ không hợp lệ: {date_string}. Định dạng yêu cầu: dd-mm-yyyy.")

    @staticmethod
    def is_valid_date(date_string):
        """Kiểm tra xem chuỗi ngày giờ có hợp lệ theo định dạng "dd-mm-yyyy" không."""
        try:
            datetime.strptime(date_string, "%d-%m-%Y")
            return True
        except ValueError:
            return False
