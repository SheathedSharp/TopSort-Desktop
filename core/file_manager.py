from PySide2.QtWidgets import QFileDialog, QMessageBox
class FileManager:
    def __init__(self, main_window, input_manager):
        self.main_window = main_window
        self.input_manager = input_manager

    def import_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self.main_window.ui, "选择要导入的文件", "", "文本文件 (*.txt);;所有文件 (*)", options=options)

        if file_path:
            try:
                self.main_window.clear_topology_graph()  # 清空拓扑排序图
                self.main_window.file_path = file_path

                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()

                    # 调用C++文件并获取结果
                    cpp_output = self.main_window.run_cpp(file_path)
                    # 将结果显示在plainTextEdit上
                    self.main_window.display_cpp_output(cpp_output)
                    self.input_manager.fill_input_boxes(file_content)

            except Exception as e:
                QMessageBox.critical(self.main_window.ui, "错误", f"导入文件时出现错误：{str(e)}")
        else:
            QMessageBox.warning(self.main_window.ui, "警告", "未选择任何文件")

    def export(self):
        options = QFileDialog.Options()
        export_option, _ = QFileDialog.getSaveFileName(self.main_window.ui, "选择导出路径", "",
                                                       "Images (*.png);;Text Files (*.txt)", options=options)

        if export_option:
            if export_option.endswith(".png"):
                # 导出图片
                self.main_window.export_image(export_option)
            elif export_option.endswith(".txt"):
                # 导出拓扑排序结果
                self.main_window.export_topology(export_option)
            else:
                QMessageBox.warning(self.main_window.ui, "警告", "不支持的导出格式")

