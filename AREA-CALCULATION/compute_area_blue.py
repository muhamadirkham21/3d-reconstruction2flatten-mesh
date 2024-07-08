import trimesh
import numpy as np
import argparse

# Fungsi untuk mengklasifikasi warna
def classify_color(rgb, blue_color, tolerance, dark_threshold):
    if np.all(np.abs(rgb - blue_color) <= tolerance):
        return 'blue'
    elif np.all(rgb > dark_threshold):
        return 'white'
    else:
        return 'dark'

# Fungsi utama
def main(args):
    # Memuat mesh dari file obj
    mesh = trimesh.load(args.input_file)

    # Memeriksa apakah mesh memiliki warna wajah
    if not mesh.visual.face_colors.any():
        print("No face colors found in the mesh.")
    else:
        # Mengambil warna wajah
        face_colors = np.array(mesh.visual.face_colors[:, :3])  # Hanya mengambil RGB, mengabaikan alpha

        # Definisi warna dan threshold
        dark_threshold = args.dark_threshold
        blue_color = np.array([0, 0, 255])
        tolerance = args.tolerance  # Toleransi untuk warna biru

        # Klasifikasi setiap warna wajah dalam mesh
        classifications = np.array([classify_color(color, blue_color, tolerance, dark_threshold) for color in face_colors])

        # Menghitung luas permukaan total
        total_surface_area = mesh.area

        # Menghitung luas permukaan wajah gelap
        dark_face_areas = mesh.area_faces[classifications == 'dark']
        total_dark_area = dark_face_areas.sum()

        # Menghitung luas permukaan wajah putih
        white_face_areas = mesh.area_faces[classifications == 'white']
        total_white_area = white_face_areas.sum()

        # Menghitung luas permukaan wajah biru atau mendekati biru
        blue_face_areas = mesh.area_faces[classifications == 'blue']
        total_blue_area = blue_face_areas.sum()

        # Mencetak hasil
        print(f"Luas permukaan total dari mesh: {total_surface_area}")
        print(f"Luas permukaan faces gelap: {total_dark_area}")
        print(f"Luas permukaan faces putih: {total_white_area}")
        print(f"Luas permukaan faces biru atau mendekati biru: {total_blue_area}")
        print(f"Jumlah luas permukaan faces gelap, putih, dan biru: {total_dark_area + total_white_area + total_blue_area}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Menghitung luas permukaan mesh berdasarkan warna wajah")
    parser.add_argument('input_file', type=str, help='Path ke file mesh (obj)')
    parser.add_argument('--dark_threshold', type=int, default=6, help='Threshold untuk menentukan warna gelap')
    parser.add_argument('--tolerance', type=int, default=157, help='Toleransi untuk warna biru')

    args = parser.parse_args()
    main(args)
