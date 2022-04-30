"""
List Based Python File Copier
A script to copy files from their respective source location (s) to the desired 
target location (t). Where each s and t locations are stored as separate lists
of paths, each path in a separate line, in sources.txt and targets.txt respectively.
The script will write the results to a logfile.log.
The script will NOT overwrite any existing files.
By cballenar
"""
import os
import shutil

# let's make sure we log everything that happens here
import logging
Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)
logger = logging.getLogger()

# Ok, let's continue with the script, set your variables
sources_file = "sources.txt"   # change as needed
source_path_prefix = ""       # /path/to/my/original-files/

targets_file = "targets.txt"   # change as needed
target_path_prefix = ""       # /path/to/where-they-go/

# opening both the files in reading modes
with open(sources_file) as sources, open(targets_file) as targets:
    # iter over both files simultaneously
    for (source_line, target_line) in zip(sources, targets):
        # get respective content, strip it, and prefix it
        source_path = source_path_prefix + source_line.strip()
        destination_path = target_path_prefix + target_line.strip()
        # print contents for logging
        logger.error("Copying from:{} to:{}.".format(source_path,destination_path))
        # check for directory and create if necessary
        try:
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        except Exception as e:
            logger.error(e)
        # test if the dest file exists, if false
        if not os.path.exists(destination_path):
            # copy file to its final destination
            try:
                shutil.copyfile(source_path, destination_path)
                logger.error("Success!")
            except Exception as e:
                logger.error(e)
        # else log an error
        else:
            logger.error("File already exist, copy aborted.")
