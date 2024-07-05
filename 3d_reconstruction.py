"""
Created on Sat Apr 11 15:04:23 2020
@author: jamesa
"""

import os
import pathlib
import argparse

def main(input_folder, output_folder):
    print("\nLaunching 3D-Reconstruction application\n")

    # Folder paths
    currentDir = os.getcwd()  # work directory
    print("Locating input images...\n")
    inputFiles = os.path.join(currentDir, "input")  # folder in work directory with the input images
    outputFiles = os.path.join(currentDir, "output")  # folder in work directory with output files
    meshroomFolder = os.path.join(currentDir, "meshroom")  # folder in work directory with all meshroom files

    # Creating all directories
    os.makedirs(currentDir, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(inputFiles, exist_ok=True)
    os.makedirs(outputFiles, exist_ok=True)
    os.makedirs(meshroomFolder, exist_ok=True)

    # Change to work directory
    os.chdir(currentDir)

    # Make copy of input image files from the input folder to the input folder of work directory
    print("\nCopying input images to work directory...\n")
    os.system(f'cp -arv {input_folder}/* {inputFiles}')

    # Check if meshroom is already installed. If not, download and install meshroom
    meshroom_files = pathlib.Path(os.path.join(currentDir, "meshroom/Meshroom-2019.2.0"))
    if not meshroom_files.exists():
        print("\nMeshroom not found.\nInstalling Meshroom...")
        os.system('wget -N https://github.com/alicevision/meshroom/releases/download/v2019.2.0/Meshroom-2019.2.0-linux.tar.gz')
        os.system(f'tar xzf Meshroom-2019.2.0-linux.tar.gz -C {meshroomFolder}')
        os.system(f'mv -v {currentDir}/meshroom/Meshroom-2019.2.0/* {meshroomFolder}')
    else:
        print("\nMeshroom is already installed. Skipping a new installation...")

    # Execute Meshroom
    startMeshroom = os.path.join(meshroomFolder, "meshroom_photogrammetry")
    os.system(f'{startMeshroom} --input {inputFiles} --output {outputFiles}')

    # Copy Output from work directory to the output folder
    print("\nMoving output files to output folder...\n")
    os.system(f'cp -arv {outputFiles}/* {output_folder}')

    # Remove the input and output folder in work directory
    print("\nRemoving all temporary files...\n")
    os.system(f'rm -Rv {inputFiles}')
    os.system(f'rm -Rv {outputFiles}')

    print('#########################################################################################################################################################################################################')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="3D Reconstruction Script")
    parser.add_argument('--input_folder', type=str, required=True, help="Path to the input folder containing images")
    parser.add_argument('--output_folder', type=str, required=True, help="Path to the output folder to store results")
    args = parser.parse_args()

    main(args.input_folder, args.output_folder)

