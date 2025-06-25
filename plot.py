import matplotlib.pyplot as plt
import numpy as np
# 这是你的数据
y = np.array([-0.043, -0.007])
x = np.array(['w/o SM', 'w SM'])

# 创建一个新的图形
fig, ax = plt.subplots(figsize=(5,4))
ax.set_ylim(-0.1, 0)
# 设置背景颜色
ax.set_facecolor('lightblue')

# 画出条形图
bars = ax.bar(x, y, width=0.2,edgecolor='whitesmoke',color='whitesmoke')

# 添加标题和标签

ax.set_ylabel('Style similarity (-1~0)↑')
# 在条形图顶部添加对应的y值
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height,
            f'{height:.3f}', ha='center', va='bottom')
# 添加网格线
ax.grid(True, color='white', linestyle='--', linewidth=1)
# 设置x轴的刻度
ax.set_xticks(range(len(x)))
# 隐藏x轴和y轴的线
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# 保存为 PDF 文件
plt.savefig('Atten.svg',dpi=600,format="svg")
# 显示图形
plt.show()