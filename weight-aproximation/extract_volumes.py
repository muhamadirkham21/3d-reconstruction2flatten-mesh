import trimesh
import os
import csv

# Folder yang berisi file .obj
data_folder = './data'
# File CSV untuk menyimpan hasil
csv_file = 'volumes.csv'

# Membuka file CSV untuk menulis hasil
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Menulis header CSV
    writer.writerow(['Filename', 'Volume_pitch_0.01', 'Volume_pitch_0.001'])

    # Iterasi melalui setiap file .obj di folder
    for filename in os.listdir(data_folder):
        if filename.endswith('.obj'):
            file_path = os.path.join(data_folder, filename)
            print(f'Processing {file_path}')

            # Muat mesh
            mesh = trimesh.load_mesh(file_path)

            # Voxelize mesh dengan pitch 0.01
            voxelized_pitch_0_01 = mesh.voxelized(pitch=0.01)
            volume_pitch_0_01 = voxelized_pitch_0_01.volume

            # Voxelize mesh dengan pitch 0.0015
            voxelized_pitch_0_0015 = mesh.voxelized(pitch=0.0023)
            volume_pitch_0_0015 = voxelized_pitch_0_0015.volume

            # Menulis hasil ke file CSV
            writer.writerow([filename, volume_pitch_0_01, volume_pitch_0_0015])

print('Volume calculation completed and saved to CSV.')
