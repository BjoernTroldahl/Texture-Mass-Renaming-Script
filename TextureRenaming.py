#Python script for automating texture naming conventions for specified file extensions
import os

def rename_textures(directory):
    #Iterate through each file in the specified directory
    for filename in os.listdir(directory):
        #Check if the filename has a .png extension (can be changed to any other file extension)
        if filename.endswith('.png'):
            #Generate a new name by adding a prefix
            new_name = 'PREFIX_' + filename

            #Rename the file using the generated new name
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

#Call the function to rename textures in a specified directory
#Replace 'your_directory_path' with the actual path to the directory containing the textures
rename_textures(r'your_directory_path')
