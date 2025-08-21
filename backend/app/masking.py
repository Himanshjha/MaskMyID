import cv2
from PIL import Image
import numpy as np

def mask_pii(image, pii_boxes):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    for box in pii_boxes:
        pts = np.array(box).astype(int)
        x_min = min(pts[:, 0])
        y_min = min(pts[:, 1])
        x_max = max(pts[:, 0])
        y_max = max(pts[:, 1])
        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 0), -1)  # black box

    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
