import open3d as o3d
import numpy as np
import argparse

# Memeriksa setiap wajah dan melihat apakah warnanya sesuai dengan target_color dalam toleransi tertentu
def is_color_within_tolerance(color, target, tolerance):
    return np.all(np.abs(color - target) <= tolerance)

def main(args):
    # Memuat mesh dari file
    mesh = o3d.io.read_triangle_mesh(args.input_file)

    # Memeriksa apakah mesh memiliki warna wajah
    if not mesh.has_triangle_material_ids():
        print("No face colors found in the mesh.")
    else:
        # Mengambil warna wajah
        triangle_colors = np.asarray(mesh.triangle_material_ids)

        # Definisi warna yang ingin dihapus
        target_color = np.array([0, 0, 255])  # Warna biru
        tolerance = args.tolerance  # Toleransi untuk warna biru

        # Mengidentifikasi indeks wajah yang perlu dihapus
        faces_to_delete = [i for i, color in enumerate(triangle_colors) if is_color_within_tolerance(color, target_color, tolerance)]

        # Membuat array indeks yang perlu dipertahankan
        all_faces = np.arange(len(triangle_colors))
        faces_to_keep = np.setdiff1d(all_faces, faces_to_delete)

        # Membuat mesh baru dengan hanya wajah yang ingin dipertahankan
        new_mesh = mesh.select_by_index(faces_to_keep, invert=False)

        # Menyimpan mesh yang telah diproses
        o3d.io.write_triangle_mesh(args.output_file, new_mesh)

        # Visualisasi mesh yang telah diproses
        o3d.visualization.draw_geometries([new_mesh])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Menghapus wajah dari mesh berdasarkan warna")
    parser.add_argument('input_file', type=str, help='Path ke file mesh (obj)')
    parser.add_argument('output_file', type=str, help='Path untuk menyimpan mesh yang diproses')
    parser.add_argument('--tolerance', type=int, default=50, help='Toleransi untuk warna biru')

    args = parser.parse_args()
    main(args)
