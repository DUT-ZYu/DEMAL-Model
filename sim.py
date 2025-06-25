import torch
import matplotlib.pyplot as plt
import numpy as np

# 假设 feature_map1 和 feature_map2 是我们的特征图
# feature_map1 = ...
# feature_map2 = ...

# 计算特征图之间的余弦相似度
cos = torch.nn.CosineSimilarity(dim=1, eps=1e-6)
cos_sim = cos(feature_map1, feature_map2)

# 将 PyTorch 张量转换为 NumPy 数组以进行绘图
cos_sim_np = cos_sim.detach().numpy()

# 创建条形图
plt.bar(np.arange(len(cos_sim_np)), cos_sim_np)
plt.xlabel('特征图索引')
plt.ylabel('余弦相似度')
plt.title('特征图之间的余弦相似度')
plt.show()
