import cv2
import numpy as np
# 读取图像
img = cv2.imread("3.png", 1)

# 将图像转换到HSV颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 增加饱和度（将S通道的值增加40%）
s_channel = hsv[:, :, 1]
s_channel = np.clip(s_channel * 1.4, 0, 255)  # 1.4表示增加40%
hsv[:, :, 1] = s_channel.astype(np.uint8)

# 将图像转换回BGR颜色空间
result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 保存结果图像
cv2.imwrite("33.png", result)
# 显示结果
# cv2.imshow("Increased Saturation", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
