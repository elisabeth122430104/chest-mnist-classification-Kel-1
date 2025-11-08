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
- jumlah epochs yang dipakai adalah 13
- nilai bach_size yang dipakai 30
- angka learning_rate yang digunakan adalah 0,0003