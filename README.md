# used_car_final_project

The cleaning process uses the following libraries and modules:
  Libraries:
  - pandas
  - sklearn
  Modules:
  - time
  - zipfile
  - lzma
  - bz2
  - io

To go through the full process of cleaning this dataset -> https://www.kaggle.com/datasets/ananaymital/us-used-cars-dataset/data

run the file: cleaning_planD.ipynb

#note that zip_data.py and cleaning_planC.py were just steps in the thought process to get to planD.

Things to know about cleaning_planD.ipynb
- fit the chunk size to whatever you think your computer will handle in regard to computer ram. It is auto set to deal with 9 GB of available ram.
- you will need to alter the second kernel line 7 to your file path.
- dropped columns are not done in mass as it was a discovery process of more items i did not need so they are spread out in the kernels. Just run straight through after altering the file path.
- the memory kernels are just for my sanity to make sure the dataset is actually getting smaller and i was not wasting time and to double check
- the markdowns at the bottom are checklists of what i did so far at that point.
- kernel 24 - 26 are investigating the transmission for later cleaning; and also to see if transmission_display is necessary or just full names what things stand for. It is actually necessary.
- kernel 27 - 28 is saving the cleaned data then compressing it using the lzma algorithm.
- when using the cleaned zip it will need to be opened back into a csv before using as lzma and pandas are not compatible at the moment.
