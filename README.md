<h1 align="center">3D MESH RECONSTRUCTION AND FLATTEN</h1>

* Dependensi 
pip install -r requirements.txt

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

```python compute_area_blue.py /path/to/your/mesh.obj --dark_threshold 6 --tolerance 157```

anda bisa melakukan perubahan parameter dark_threshold, tolerance dan warna yang ingin dihitung.

untuk melakukan isolasi mesh supaya warna tertentu saja yang hanya di tampilkan 

jalankan 
```python mesh_isolation.py /path/to/your/mesh.obj /path/to/save/processed_mesh.obj --tolerance 50```













