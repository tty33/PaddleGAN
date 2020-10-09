import cv2
from tqdm import tqdm
import os
os.makedirs('data/cityscapes/trainA',exist_ok=True)
os.makedirs('data/cityscapes/trainB',exist_ok=True)

for img_path in tqdm(os.listdir('data/cityscapes/train')):
    img = cv2.imread(os.path.join('data/cityscapes/train',img_path))
    A = img[:, :256, :]
    B = img[:, 256:, :]
    cv2.imwrite(f'data/cityscapes/trainA/{img_path}',A)
    cv2.imwrite(f'data/cityscapes/trainB/{img_path}',B)