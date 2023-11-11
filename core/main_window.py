import os
import subprocess

from PySide2.QtWidgets import (
    QFileDialog, QMessageBox, QListWidgetItem,
    QLineEdit, QAbstractItemView, QWidget,
    QVBoxLayout, QLabel
)
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt
from .file_manager import FileManager
from .input_manager import InputManager
from .topology_manager import TopologyManager

class MainWindow:
    def __init__(self):
        # 动态加载.ui文件
        self.ui = QUiLoader().load('statics/main.ui')
        # 禁止调整窗口大小
        self.ui.setFixedSize(self.ui.size())
        # 设置窗口属性，禁止最大化
        self.ui.setWindowFlags(self.ui.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        # 用于存储边信息的列表
        self.edge_info = []
        # 存储文件路径
        self.file_path = None

        # 初始化控制器
        self.input_manager = InputManager(self)
        self.file_manager = FileManager(self, self.input_manager)
        self.topology_manager = TopologyManager(self)

        # 连接相关操作的槽函数
        self.ui.actionImport.triggered.connect(self.file_manager.import_file)
        self.ui.actionExport.triggered.connect(self.file_manager.export)
        self.ui.addButton.clicked.connect(self.input_manager.add_input_field)
        self.ui.delButton.clicked.connect(self.input_manager.del_input_field)
        self.ui.generateButton.clicked.connect(self.topology_manager.generate_draw)

        # 设置输入框为单选模式
        self.ui.inputList.setSelectionMode(QAbstractItemView.SingleSelection)

        # 设置按钮的提示文本
        self.ui.addButton.setToolTip("添加输入框 (Alt + A)")
        self.ui.delButton.setToolTip("删除输入框 (Alt + D)")
        self.ui.generateButton.setToolTip("生成拓扑排序结果 (Alt + Enter)")

        # 创建一个 QWidget 作为容器
        self.photo_container = QWidget()
        self.ui.photoLabel.layout().addWidget(self.photo_container)
        self.ui.photoLabel.setStyleSheet("background-color: white;")

        # 在容器上设置布局
        container_layout = QVBoxLayout()
        self.photo_container.setLayout(container_layout)

        # 将 QLabel 添加到容器中
        self.photo_label = QLabel()
        container_layout.addWidget(self.photo_label)

    def clear_topology_graph(self):
        self.photo_label.clear()  # 清空 QLabel 上的图像
        self.ui.progressBar.setValue(0)  # 重置进度条的值

    def run_cpp(self, file_path):
        try:
            # 获取当前脚本所在目录
            script_directory = os.path.dirname(os.path.abspath(__file__))

            # 构建调用命令
            cpp_executable_path = os.path.join(script_directory, 'TopologicalSort.exe')
            command = f'"{cpp_executable_path}" "{file_path}"'

            # 调用外部程序
            result =  subprocess.run(command, shell=True, stdout=subprocess.PIPE)

            # 返回结果
            return result.stdout

        except Exception as e:
            print("Error during running C++ program:", str(e))
            return "Error: Unable to run C++ program"

    # 在plainTextEdit中显示C++程序的输出
    def display_cpp_output(self, cpp_output):
        try:
            # 将字节串解码为字符串
            cpp_output_str = cpp_output.decode('utf-8')

            # 在plainTextEdit中显示C++程序的输出
            self.ui.plainTextEdit.setPlainText(cpp_output_str)
        except Exception as e:
            print("Error: Unable to display C++ output:", str(e))
            self.ui.plainTextEdit.setPlainText("Error: Unable to display C++ output")

    def export_image(self, export_path):
        pixmap = self.photo_label.pixmap()
        if pixmap:
            pixmap.save(export_path, "PNG")
            QMessageBox.information(self.ui, "导出成功", f"图像已成功导出到：{export_path}")
        else:
            QMessageBox.warning(self.ui, "警告", "没有图像可导出")

    def export_topology(self, export_path):
        try:
            # 获取C++程序的输出
            cpp_output = self.ui.plainTextEdit.toPlainText().encode('utf-8')

            # 写入文件
            with open(export_path, 'wb') as file:
                file.write(cpp_output)

            QMessageBox.information(self.ui, "导出成功", f"拓扑排序结果已成功导出到：{export_path}")
        except Exception as e:
            QMessageBox.critical(self.ui, "错误", f"导出拓扑排序结果时出现错误：{str(e)}")

if __name__ == "__main__":
    # Create the application instance
    import sys
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)

    # Create and show the main window
    mainWindow = MainWindow()
    mainWindow.ui.show()

    # Start the event loop
    sys.exit(app.exec_())
