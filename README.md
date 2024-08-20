# binpatch
The utility for patching binary file with data from another one.

### usage: binpatch.py [-h] [-o OFFSET] [-p PORTION_SIZE] patched_file patch_data_file

#### positional arguments:

  patched_file          
  
    file that will be patched

  patch_data_file       
  
    file with patch data

#### options:
  
  -h, --help            

          show this help message and exit
  
  
  -o OFFSET, --offset OFFSET

          Offset where patch will be applied. 0 by default (mean begining of file).
  
  -p PORTION_SIZE, --portion-size PORTION_SIZE

          Data from patch_data_file will be read by portions. This option specify the portion size in bytes. 1024 by default
