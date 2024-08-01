"""
3D Mesh Processing Script using PyMeshLab

This script processes a 3D mesh by:
1. Calculating the total surface area.
2. Calculating the surface area of blue-colored parts of the mesh.
3. Removing blue-colored parts of the mesh.
4. Calculating the surface area of dark and white-colored parts of the mesh.
5. Saving the processed mesh to a file.

Author: irkham@koda.so
"""

import pymeshlab

def process_mesh(input_mesh_path, output_mesh_path):
    ms = pymeshlab.MeshSet()

    # Load the mesh from the file
    ms.load_new_mesh(input_mesh_path)

    # Display total surface area
    out_dict = ms.get_geometric_measures()
    print('Luas permukaan mesh: {} ft'.format(out_dict['surface_area']))

    try:
        # Display surface area of the blue-colored parts of the mesh
        ms.compute_selection_by_color_per_face(color=pymeshlab.Color(0, 0, 255, 255), colorspace=1, inclusive=False, percentrh=1.000000, percentgs=0.110000, percentbv=1.000000)
        blue_mesh = ms.get_area_and_perimeter_of_selection()['selected_surface_area']
        print('Luas permukaan mesh berwarna biru: {}'.format(blue_mesh))
    except Exception as e:
        print(f"Tidak ada mesh yang berwarna biru atau mendekati biru \n Gunakan filter warna yang lain")
        blue_mesh = 0

    # Remove the blue-colored parts of the mesh
    ms.meshing_remove_selected_vertices_and_faces()
    print()
    print('---------------------------------------------------------------')
    print('Mesh berwarna biru telah dihilangkan')

    # Display the new total surface area
    new_mesh_dict = ms.get_geometric_measures()
    print('Luas permukaan mesh sekarang: {}'.format(new_mesh_dict['surface_area']))

    try:
        # Calculate the surface area of dark-colored parts of the mesh
        print()
        print('---------------------------------------------------------------')
        print('Menghitung mesh yang berwarna gelap')
        ms.compute_selection_by_color_per_face(colorspace=1, percentrh=1.000000, percentgs=0.310000, percentbv=1.000000)
        black_mesh = ms.get_area_and_perimeter_of_selection()['selected_surface_area']
        print('Luas permukaan mesh yang berwarna gelap: {}'.format(black_mesh))

        # Calculate the surface area of white-colored parts of the mesh
        ms.apply_selection_inverse()
        white_mesh = ms.get_area_and_perimeter_of_selection()['selected_surface_area']
        print('Luas permukaan mesh yang berwarna putih: {}'.format(white_mesh))

    except Exception as e:
        print(f"Tidak ada mesh yang berwarna gelap")
        black_mesh = 0
        white_mesh = ms.get_geometric_measures()
        print('Luas permukaan mesh yang berwarna putih: {}'.format(white_mesh))

    # Save the processed mesh to a file
    print()
    print('------------------------------------------------------------------')
    print('Menyimpan mesh setelah dihilangkan mesh berwarna biru...')
    ms.save_current_mesh(file_name=output_mesh_path)
    print('Mesh {} telah tersimpan!'.format(output_mesh_path))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="3D Mesh Processing Script using PyMeshLab")
    parser.add_argument('--input_mesh_path', type=str, required=True, help="Path to the input mesh file")
    parser.add_argument('--output_mesh_path', type=str, required=True, help="Path to save the processed mesh file")

    args = parser.parse_args()
    process_mesh(args.input_mesh_path, args.output_mesh_path)
