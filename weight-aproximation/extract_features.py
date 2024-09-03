import pymeshlab
import pandas as pd
import os

# Path folder tempat file .obj berada
folder_path = './data'

# Inisialisasi list untuk menyimpan data
all_data = []

# Loop melalui semua file data001.obj sampai data0041.obj
for i in range(1, 71):  # 1 hingga 41
    file_name = f'data{i:03d}.obj'
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        # Load the mesh
        ms = pymeshlab.MeshSet()
        ms.load_new_mesh(file_path)

        # Compute surface area
        out_dict = ms.get_geometric_measures()
        surface_area = out_dict['surface_area']

        # Compute bounding box
        bbox = ms.current_mesh().bounding_box()
        bbox_size_x = bbox.dim_x()
        bbox_size_y = bbox.dim_y()
        bbox_size_z = bbox.dim_z()

        # Get number of vertices and faces
        num_vertices = ms.current_mesh().vertex_number()
        num_faces = ms.current_mesh().face_number()

        # Compute mean curvature
        ms.compute_curvature_principal_directions_per_vertex()
        mean_curvatures = ms.current_mesh().vertex_scalar_array()
        mean_curvature = mean_curvatures.mean()  # Mean of all vertex mean curvatures

        # Append data to the list
        all_data.append({
            'File Name': file_name,
            'Surface Area': surface_area,
            'Bounding Box X': bbox_size_x,
            'Bounding Box Y': bbox_size_y,
            'Bounding Box Z': bbox_size_z,
            'Number of Vertices': num_vertices,
            'Number of Faces': num_faces,
            'Mean Curvature': mean_curvature
        })
        print('data ke {} telah ter ekstrak'.format(i))

# Convert all data to a DataFrame
df = pd.DataFrame(all_data)

# Save to Excel file
df.to_excel('mesh_data_summary.xlsx', index=False)
