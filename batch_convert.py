import os, gimpfu
from gimpfu import *

def convert(filepath, ext="avif", quality=100, lossless=1):
	img = pdb.gimp_file_load(filepath, filepath)
	new_path = "{filepath}.{ext}".format(filepath=filepath.rsplit(".", 1)[0], ext=ext)
	# layer = pdb.gimp_image_merge_visible_layers(img, gimpfu.CLIP_TO_IMAGE)
	layer = pdb.gimp_image_active_drawable(img)
	if ext == 'avif':
		pdb.file_heif_av1_save(img, layer, new_path, new_path, quality, lossless)
	elif ext == 'jxl':
		pdb.file_jpegxl_save(img, layer, new_path, new_path)
	elif ext == 'webp':
		pdb.file_webp_save(img, layer, new_path, new_path)
	else:
		pdb.gimp_file_save(img, layer, new_path, new_path)

def batch_convert(directory, ext="avif", quality=100, lossless=1):
	for root, folders, filenames in os.walk(directory):
		for filename in filenames:
			filepath = os.path.join(root, filename)
			name, current_ext = os.path.splitext(filename)
			current_ext = current_ext.lstrip('.')
			if current_ext not in ["jpg", "png", "gif", "tif"] or current_ext == ext:
				continue
			convert(filepath, ext, quality, lossless)
	
register(
	'batch_convert', # name
	'Batch convert images in a folder to specified file type.', # description
	'Walks through the specified folder and subfolders. Generates new versions of the images in those folders with the specified extension and saves those files alongside their original versions.', # help
	'Tony Klodd', # author
	'Tony Klodd', # copyright
	'2024', # date
	'Batch Convert', # menupath
	None, # image types
	[
		(PF_STRING, "directory", "The path of the root directory you want to scan.", None),
		(PF_STRING, "ext", "The new extension that you want to convert the images to.", "avif"),
		(PF_INT8, "quality", "0 - 100.  0 = worst, 100 = best.", 100),
		(PF_BOOL, "lossless", "0 or 1.  0 = lossy, 1 = lossless.", 1),
	], # params
	[], # results. Format (type, name, description)
	batch_convert, # callback
)

main()
