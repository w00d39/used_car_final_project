import zipfile, bz2 #pandas cannot lzma compress
import pandas as pd 

def compress(filename, output_file): #this function compresses the file to the nines
    with zipfile.ZipFile(output_file, 'w', compression=zipfile.ZIP_BZIP2, compresslevel=9) as crash:
        crash.write(filename, arcname='compressed_used_cars_data.csv')

compress('used_cars_data.csv', 'compressed_used_cars_data.zip')