# List Based Python File Copier

A script to copy files from their respective source location (s) to the desired target location (t). Where each s and t locations are stored as separate lists of paths, each path in a separate line, in sources.txt and targets.txt respectively. The script will NOT overwrite any existing files. The script will write the results to a `logfile.log`.

## Why
I had a massive list of files that were sorted (badly) based on dates but they weren't in the format (e.g., `/1990-1910/19901231-001.jpg`) in which I needed to use them. I exported the list of paths to a spreadsheet, figured out the date from the nomenclature used and built the desired path I needed (i.e., `/1990/12/31/001.jpg`). With these two lists of sources and target locations I was able to move all 500k files while writing this documentation.

## How to Use
This script assumes some basic knowledge of python and execution of scripts from command line.

1. Be sure to customize the script. This includes:
    * `sources_file`. The list of file paths you want to copy.
    * `source_path_prefix`. Use this to modify the source path. Useful if using relative paths.
    * `targets_file`. The location path where you intend to move them to.
    * `target_path_prefix`. Use this to modify the target path. Useful if using relative paths.
2. Check your source and target files (see examples below for help)
3. From the terminal execute the script `python list-based-python-file-copier.py`
4. Check the log file for progress and results.

## Example Lists
In the examples below, the paths from sources will be matched one by one to the target paths and each of the files will be moved to their respective destination. Notice that this can result in a file being moved to a different sublocation or to even have their name changed.

### sources.txt
```
./source-folder/my-file-1.jpg
./source-folder/possible-sub-folder/my-file-2.jpg
./source-folder/possible-sub/sub-folder/my-file-3.jpg
```

To these sources I could add a prefix such as `/Volume/USB001/` to indicate that my source folder is in the external volume by that name.

### targets.txt
```
./target-folder/01/my-file-1.jpg
./target-folder/02/my-file-2-renamed.jpg
./target-folder/03/my-file-3.jpg
```

To these targets I could add a prefix such as `/Users/myusername/Documents/` to indicate that I want to copy the files to my Documents folder.
