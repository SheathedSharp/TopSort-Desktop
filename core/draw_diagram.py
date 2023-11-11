import networkx as nx
import matplotlib.pyplot as plt
import tempfile

def draw_directed_graph(edges, figsize=(3, 3)):
    try:
        # 创建一个有向图对象
        G = nx.DiGraph()

        # 添加有向边
        for data in edges:
            data = data.strip('<>')
            source, target = data.split(',')
            G.add_edge(source, target)

        # 设置图片的大小
        plt.figure(figsize=figsize)

        # 绘制有向图
        pos = nx.spring_layout(G)

        # Adjust node positions for labels to be around the nodes
        pos_labels = {node: (x, y + 0.01) for node, (x, y) in pos.items()}

        nx.draw(G, pos, with_labels=False, node_color='g', node_size=200, arrows=True)

        # Draw labels separately with adjusted positions
        nx.draw_networkx_labels(G, pos_labels, font_size=10)

        # 保存图形到临时文件
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
            plt.savefig(tmpfile, format="png", bbox_inches="tight")

        # 返回临时文件的路径
        return tmpfile.name

    except Exception as e:
        print(f"生成图时出现错误：{str(e)}")
