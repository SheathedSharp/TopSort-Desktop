from PySide2.QtCore import Qt
from PySide2.QtWidgets import QListWidgetItem, QLineEdit, QAbstractItemView

class InputManager:
    def __init__(self, main_window):
        self.main_window = main_window

    def fill_input_boxes(self, file_content):
        # 清空现有输入框的内容
        self.main_window.ui.inputList.clear()
        data_list = file_content.split('\n')  # 按换行符分割数据
        for data in data_list:
            data = data.strip()
            if data:
                # 提取源节点和目标节点
                source, target = data.split(',')
                source = source.strip()
                target = target.strip()

                # 创建适当的输入格式
                input_item = QListWidgetItem()
                input_line_edit = QLineEdit(f"{source},{target}")
                input_line_edit.setAlignment(Qt.AlignCenter)
                self.main_window.ui.inputList.addItem(input_item)
                self.main_window.ui.inputList.setItemWidget(input_item, input_line_edit)

    def add_input_field(self):
        input_item = QListWidgetItem()
        input_line_edit = QLineEdit('<start,end>')
        input_line_edit.setAlignment(Qt.AlignCenter)  # 设置文本居中对齐
        self.main_window.ui.inputList.addItem(input_item)
        self.main_window.ui.inputList.setItemWidget(input_item, input_line_edit)

        # 将边信息添加到列表中
        self.main_window.edge_info.append('<start,end>')

    def del_input_field(self):
        selected_items = self.main_window.ui.inputList.selectedItems()
        for item in selected_items:
            index = self.main_window.ui.inputList.row(item)
            self.main_window.ui.inputList.takeItem(index)

            # 从列表中删除对应的边信息
            if index < len(self.main_window.edge_info):
                del self.main_window.edge_info[index]