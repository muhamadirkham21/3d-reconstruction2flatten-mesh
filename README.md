<h1 align="center">3D MESH RECONSTRUCTION AND FLATTEN</h1>

* Dependensi 
`pip install -r requirements.txt`

### Main Task
* 3d Reconstruction
* Flattened 3d model
* 3d Model Area Calculation
* 3d Model Weight Aproximation

## 3D-RECONSTRUCTION 

Direktori ini berisi script untuk membuat 3d mesh dengan menggunakan pipeline dari meshroom https://github.com/alicevision/meshroom/. pipeline tersebut memuat 
1. Camera Init
2. Feature Extraction
3. Image Matching
4. Feature Matching
5. Structure From Motion
6. Prepare Dense Scene
7. Depth Map
8. Depth Map Filter
9. Meshing
10. Mesh Filtering
11. Texturing

untuk menjalankannya pergi ke directory 3D-RECONSTRUCTION 

```cd ./3D-RECONSTRUCTION```

Lalu jalankan 

```3d_reconstruction.py --input_folder "path/to/data" --output_folder "path/output/folder"```

data berisi sekumpulan gambar objek, sebagai contoh dapat dilihat pada data/pumpkins


## 3D-2-FLATTEN 
Direktor ini berisi direktori untuk melakukan flatten mesh 3d. Kode bersumber dari https://github.com/GeometryCollective/boundary-first-flattening.
anda bisa melakukan cloning repositori terlebih dahulu kemudian melakukan install dependensi sesuai arahan repositori tersebut 

untuk melakukan flatten 

```cd ./3D-2-FLATTEN/boundary-first-flattening/build```

kemudian jalankan 
```./bff-command-line in.obj out.obj```


## AREA-CALCULATION 
Direktori ini berisi script untuk menghitung area pada mesh, script untuk melakukan isolasi mesh berdasarkan warna tertentu.

untuk melakukan perhitungana area berdasarkna warna gelap, terang, dan biru 

```cd ./AREA-CALCULATION```
kemudian jalankan

```python preprocess.py --input_mesh_path "path/to/input_mesh.obj" --output_mesh_path "path/to/output_mesh.obj"```


output script akan menampilkan luas permukaan mesh warna biru, warna gelap dan warna putih. serta otomatis akan menghilangkan mesh yang berwarna biru dan menyimpannya ke mesh yang baru. 

Untuk melakukan setting parameter warna pada `preproces.py`, ubah kode warna rgb. sebagai contoh (0, 0, 255, 255) untuk kode warna biru. (255, 0, 0, 255) untuk warna merah. berhati-hatilah dengan setting parameter warna tersebut karena sangat sensitif. untuk pengaturan yang lebih baik kami merekomendasikan menggunakan pengaturan warna menggunakan meshlab (https://www.meshlab.net/#download).


## WEIGHT-APROXIMATION

Kami menyediakan dataset 3d model buatan untuk melakukan aproksimasi weight mesh. jika anda ingin menambah dataset, tambahkan data.obj pada folder ./weight-aproximation/data kemudian jalankan 

1. `extract_features.py`
2. `exctract_volumes.py` 

setelah itu file `mesh_data_summary.xlsx` dan `volumes.csv` akan terupdate. merge keduanya dan lakukan proses training model Machine Learning sesuai kebutuhan.

Jika anda ingin melakukan training langsung dengan dataset kami, Buka dan lakukan tuning parameter pada `notebook.ipynb` yang sudah kami sediakan.














