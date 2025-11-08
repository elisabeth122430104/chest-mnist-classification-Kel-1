Nama: Elisabeth Tampubolon
NIM: 122430104

Perubahan hasil eksperimen CNN menggunakan model ResNet-18
- Pada file datareader.py ditambahan augmentasi rotating dapat dilihat pada kodingan dibawah
- Menyiapkan transformasi citra untuk training dan validasi, di mana data training diberi augmentasi seperti rotasi acak ±15° dan flip horizontal di datareader.py untuk menambah variasi dan mencegah overfitting. Sedangkan data validasi hanya di-resize, dikonversi ke tensor, dan dinormalisasi agar evaluasi performa model tetap konsisten.

Perubahan Model
- model yang dipakai adalah ResNet-18 dan
- dimodifikasi agar bisa menerima gambar dengan jumlah channel fleksibel (misal 1 untuk grayscale), ukuran kecil (28x28), dan menghasilkan 1 logit untuk klasifikasi biner. 
- Input fleksibel: in_channels bisa diatur, misal 1 untuk grayscale atau 3 untuk RGB.
- Gambar kecil: Kernel conv1 diubah menjadi 3x3 dan maxpool awal dihilangkan agar feature map tidak terlalu kecil.
- Output biner: Jika num_classes==2, classifier akhir menghasilkan 1 logit untuk digunakan dengan BCEWithLogitsLoss.
- Pretrained opsional: Bisa menggunakan ResNet-18 pretrained atau dilatih dari awal (pretrained=False).
- Forward pass: Input diteruskan ke self.backbone yang merupakan ResNet-18 hasil modifikasi.
- Testing cepat: Bagian __main__ membuat dummy input dan menampilkan ukuran input/output serta arsitektur untuk memastikan model bekerja.

Perubahan train.py
- perubahan yang dilakukan pada epochs bach_size, learning_rate
- jumlah epochs yang dipakai adalah 15
- nilai bach_size yang dipakai 15
- angka learning_rate yang digunakan adalah 0,0003
- Training accuracy meningkat pesat: Dari 69% di epoch 1 hingga sekitar 98% di epoch 15, menunjukkan model sangat cepat belajar data training.
- Validation accuracy stabil tinggi: Val acc mulai 66%, lalu naik hingga sekitar 80–81% di beberapa epoch, menunjukkan model bisa generalisasi cukup baik pada data validasi.
- Overfitting mulai muncul: Training acc terus naik mendekati 100% sementara val loss kadang naik (misal epoch 8–9 dan 11), menandakan model mulai menghafal data training.
- Pengaruh batch size kecil (15): Batch lebih kecil membuat model belajar lebih “stochastic”, yang bisa membantu generalisasi tapi training lebih lambat per epoch.
- Learning rate 0.0003 cukup stabil: Tidak terlalu besar sehingga loss val tidak “melompat-lompat” secara ekstrim, dan model tetap konvergen.
- Epochs 15 efektif: Terlalu sedikit epoch → model belum optimal; terlalu banyak epoch → overfitting meningkat. Di sini 15 epoch terlihat memberikan trade-off bagus antara training dan val accuracy.
- Augmentasi rotation membantu: Dengan augmentasi rotasi, model belajar fitur lebih bervariasi dan val accuracy lebih tinggi (~80%) dibanding percobaan tanpa augmentasi.
- beberapa kali sempat mencoba mengganti nilai epocshs yang dinaikkan (30), kemudian batch dinaikkan (32) dan learning rate (0,0001) diturunkan. Namun validasi akurasi semakin rendah sekitar 74% akurasinya

Hasil Akurasi
Epoch [1/15] | Train Loss: 0.5908 | Train Acc: 69.38% | Val Loss: 0.7286 | Val Acc: 66.57% 
Epoch [2/15] | Train Loss: 0.4540 | Train Acc: 78.01% | Val Loss: 0.4741 | Val Acc: 76.10% 
Epoch [3/15] | Train Loss: 0.3691 | Train Acc: 84.22% | Val Loss: 0.4501 | Val Acc: 78.89% 
Epoch [4/15] | Train Loss: 0.2797 | Train Acc: 87.94% | Val Loss: 0.4373 | Val Acc: 78.01% 
Epoch [5/15] | Train Loss: 0.2349 | Train Acc: 90.11% | Val Loss: 0.4378 | Val Acc: 80.50% 
Epoch [6/15] | Train Loss: 0.1751 | Train Acc: 92.84% | Val Loss: 0.5846 | Val Acc: 78.59% 
Epoch [7/15] | Train Loss: 0.1564 | Train Acc: 94.06% | Val Loss: 0.5340 | Val Acc: 80.06% 
Epoch [8/15] | Train Loss: 0.0999 | Train Acc: 96.62% | Val Loss: 0.8225 | Val Acc: 75.22% 
Epoch [9/15] | Train Loss: 0.0745 | Train Acc: 97.31% | Val Loss: 0.9838 | Val Acc: 77.42% 
Epoch [10/15] | Train Loss: 0.0851 | Train Acc: 96.70% | Val Loss: 0.7580 | Val Acc: 80.50% 
Epoch [11/15] | Train Loss: 0.0652 | Train Acc: 97.70% | Val Loss: 1.1292 | Val Acc: 74.05% 
Epoch [12/15] | Train Loss: 0.0629 | Train Acc: 98.01% | Val Loss: 0.6990 | Val Acc: 81.38% 
Epoch [13/15] | Train Loss: 0.0541 | Train Acc: 98.35% | Val Loss: 0.7040 | Val Acc: 78.15% 
Epoch [14/15] | Train Loss: 0.0480 | Train Acc: 98.14% | Val Loss: 0.7160 | Val Acc: 80.94% 
Epoch [15/15] | Train Loss: 0.0502 | Train Acc: 98.27% | Val Loss: 0.7959 | Val Acc: 79.91%

Akurasi terbaik
Epoch [12/15] | Train Loss: 0.0629 | Train Acc: 98.01% | Val Loss: 0.6990 | Val Acc: 81.38%