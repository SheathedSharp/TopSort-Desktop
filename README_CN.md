# Desktop-portable-topological-sorting-application

## 运行环境
- OS：Mac
- IDE：VSCode
- 解释器：python v3.9
- 外部库： PySide2 v5.15.2.1、networkx v2.5.1、matplotlib v3.3.4
- GUI工具：QtDesigner

## 项目层级

```commandline
TopologicalSort_app
├─build(打包好的软件)
├─core (核心算法)
├─data (读入的文件信息)
├─dist （发布软件的各个版本）
├─docs （所有文档信息）
├─statics （静态资源）
```



## 快速部署
- 首先需要创建一个虚拟环境，输入命令`mamba create -n "your-env-name" python=3.9`，创建一个名为"your-env-name"的虚拟环境
- 激活刚刚创建的虚拟环境，输入命令`conda activate "your-env-name"`
- 安装外部依赖，输入命令`mamba install --file requirements.txt`

## 使用指南
- 使用先前创建好的环境，运行主文件`python main.py`

![](https://pic.imgdb.cn/item/66936984d9c307b7e95ee99d.png)

- 选择需要导入的文件，或者手动输入一定格式的数据，进行添加

![](https://pic.imgdb.cn/item/66936987d9c307b7e95eed68.png)


- 完成数据数据后点击`generate`按钮后将会进行拓扑排序

![](https://pic.imgdb.cn/item/66936987d9c307b7e95eede8.png)


- 左下方将会输出拓扑排序的结果，右边将会展示拓扑图
- 可以选择导出拓扑结果(.txt)也可以选择导出拓扑图(.png)

![](https://pic.imgdb.cn/item/66936989d9c307b7e95eefdf.png)

![](https://pic.imgdb.cn/item/66936989d9c307b7e95ef050.png)