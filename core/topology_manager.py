from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QMessageBox

from .draw_diagram import draw_directed_graph

class TopologyManager:
    def __init__(self, main_window):
        self.main_window = main_window
    def generate_draw(self):
        try:
            if not self.main_window.file_path:
                QMessageBox.warning(self.main_window.ui, "警告", "未选择任何文件")
                return

            # 获取所有输入框的值
            input_items = [self.main_window.ui.inputList.itemWidget(self.main_window.ui.inputList.item(i)).text()
                           for i in range(self.main_window.ui.inputList.count())]

            # 将边信息更新为当前输入框中的值
            self.main_window.edge_info = input_items

            # 调用绘图函数并获取图形文件路径
            graph_image_path = draw_directed_graph(input_items)

            if graph_image_path:
                # 将图形文件设置为QLabel的图像
                pixmap = QPixmap(graph_image_path)
                self.main_window.photo_label.setPixmap(pixmap)
                self.main_window.ui.progressBar.setValue(100)

            # 更新文件中的边信息（覆盖原文件）
            with open(self.main_window.file_path, 'w', encoding='utf-8') as file:
                file.write('\n'.join(input_items))

            # 重新调用C++程序并更新输出
            cpp_output = self.main_window.run_cpp(self.main_window.file_path)
            self.main_window.display_cpp_output(cpp_output)

        except Exception as e:
            print("Error during generate_draw:", str(e))
