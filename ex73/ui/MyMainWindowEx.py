from chapter5.ex73.libs.my_module import solve_quadratic
from chapter5.ex73.ui.MyMainWindow import Ui_MainWindow


class MyMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.solve)

    def solve(self):
        try:
            # 1. Đọc dữ liệu hệ số a, b, c từ giao diện
            a = float(self.enterALineEdit.text())
            b = float(self.enterBLineEdit.text())
            c = float(self.enterCLineEdit.text())

            # 2. Gọi hàm giải phương trình từ module trong libs
            result = solve_quadratic(a, b, c)

            # 3. Hiển thị kết quả ra ô kết quả trên UI
            self.resultLineEdit.setText(str(result))

        except ValueError:
            self.resultLineEdit.setText("Vui lòng nhập đúng số cho a, b, c!")