# model.py

import torch
import torch.nn as nn
import torchvision.models as models

class ResNet18Model(nn.Module):
    """
    ResNet-18 yang dimodifikasi agar cocok untuk:
    - input channels fleksibel (mis. 1 untuk grayscale)
    - gambar kecil (28x28): gunakan conv1 kernel 3x3 + hilangkan maxpool
    - output single logit saat num_classes==2 (untuk BCEWithLogitsLoss)
    """
    def __init__(self, in_channels=1, num_classes=2, pretrained=False):
        super().__init__()
        self.num_classes = num_classes

        # Ambil arsitektur ResNet-18 dasar
        base = models.resnet18(pretrained=pretrained)

        # Sesuaikan conv1 untuk input channels selain 3 (mis. 1 untuk grayscale)
        if in_channels != 3:
            base.conv1 = nn.Conv2d(in_channels, 64, kernel_size=3, stride=1, padding=1, bias=False)
            # Untuk gambar kecil, hilangkan maxpool agar feature map tidak terlalu diperkecil
            base.maxpool = nn.Identity()
        else:
            # Jika tetap 3-kanal tapi gambar kecil, juga ubah stride/pool agar lebih sesuai
            base.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
            base.maxpool = nn.Identity()

        # Sesuaikan classifier akhir: jika biner, keluaran 1 logit (untuk BCEWithLogitsLoss)
        out_features = 1 if num_classes == 2 else num_classes
        base.fc = nn.Linear(base.fc.in_features, out_features)

        self.backbone = base

    def forward(self, x):
        return self.backbone(x)

# --- Bagian untuk pengujian cepat ---
if __name__ == '__main__':
    NUM_CLASSES = 2
    IN_CHANNELS = 1

    print("--- Menguji Model 'ResNet18Model' ---")
    model = ResNet18Model(in_channels=IN_CHANNELS, num_classes=NUM_CLASSES, pretrained=False)
    print("Arsitektur Model:")
    print(model)

    dummy_input = torch.randn(8, IN_CHANNELS, 28, 28)
    output = model(dummy_input)

    print(f"\nUkuran input: {dummy_input.shape}")
    print(f"Ukuran output: {output.shape}")
    print("Pengujian model 'ResNet18Model' berhasil.")