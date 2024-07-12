# GIMP Batch File Conversion Plugin

This plugin adds a function in GIMP that can be called on a folder on your computer.  When called, it walks through the specified folder and subfolders and generates new versions of the jpg, png, gif, and tif images in those folders with the specified extension and saves those files alongside their original versions.

## Installation

Put the batch_convert.py inside a corresponding folder in your GIMP plugins folder, such as 
```
<gimp installation folder>/lib/gimp/2.0/plug-ins/batch_convert/batch_convert.py
```

## Usage

Open GIMP.  Navigate to Filters -> Python-Fu -> Console.  Click Browse and search for "batch_convert", or enter this into the console:

```
pdb.python_fu_batch_convert("<path to directory to be converted>", "avif|jxl|webp", 100, 0|1)
```

## Parameters

* **directory**: String.  The directory of the root folder you want to walk through whose images you want to convert.  Should use forward slashes.
* **ext**: String.  The new extension you want to convert the images to.  Should be one of avif, jxl, or webp.
* **quality**: Positive Integer between 0 and 100.  0 is worst quality, 100 is best quality.  Applies only to avif.
* **lossless**: Boolean.  0 or 1.  0 is lossy.  1 is lossless.  Applies only to avif.

## Troubleshooting

* Make sure you use forward slashes and not backslashes in your folder path.
