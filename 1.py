import torch
weights_dict = torch.load("F:\姿态识别/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth", map_location='cpu')
print(weights_dict.named_modules())