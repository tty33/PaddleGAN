English | [简体中文](./README.md)
## 假定使用notebook ！！

## Download Dataset
This script could download several dataset for paired images for image2image translation task.
`[cityscapes|facades|edges2handbags|edges2shoes|maps]`
```
!cd PaddleGAN/script/ && bash pix2pix_download.sh cityscapes
```
## cityscapes dataset preprocess

```
python script/preprecess.py
```

## Train
```
python -u tools/main.py --config-file configs/cyclegan-cityscapes.yaml
```

continue train from last checkpoint
```
python -u tools/main.py --config-file configs/cyclegan-cityscapes.yaml --resume your_checkpoint_path
```

multiple gpus train:
```
CUDA_VISIBLE_DEVICES=0,1 python -m paddle.distributed.launch tools/main.py --config-file configs/pix2pix-cityscapes.yaml
```

## Evaluate
```
python tools/main.py --config-file configs/cyclegan-cityscapes.yaml --evaluate-only --load your_weight_path
```
