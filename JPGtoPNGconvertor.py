import sys
import os
import glob
from pathlib import Path
 
from PIL import Image

def get_from_to_folders(from_to_dir): # get arguments
	# total arguments
	n = len(sys.argv)
	if n != 3:
		print("Wrong list of parameters!")
		return -1
	from_to_dir[0] = sys.argv[1]
	from_to_dir[1] = sys.argv[2]
	
	return 0

def get_jpg_file_list_by_type(from_dir, f_type):
	return glob.glob(from_dir + r"/*." + f_type)

def create_dir(directory_name):
	try:
	    os.mkdir(directory_name)
	    print(f"Directory '{directory_name}' created successfully.")
	except FileExistsError:
	    print(f"Directory '{directory_name}' already exists.")
	except PermissionError:
	    print(f"Permission denied: Unable to create '{directory_name}'.")
	except Exception as e:
	    print(f"An error occurred: {e}")

ftdir = ['', '']
if get_from_to_folders(ftdir) == 0:
	for files in get_jpg_file_list_by_type(ftdir[0], 'jpg'):
		img = Image.open(files)
		if img.size[0] > 400:
			img.thumbnail((400, 400))
		file = Path(files).stem
		if not os.path.exists(ftdir[1]):
			create_dir(ftdir[1])

		img.save(r"./" + ftdir[1] + r"/" + file + ".png", 'png')


