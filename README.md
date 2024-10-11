```
                  __            ______  _______  ___ ___ 
.--------..---.-.|  |--..-----.|      ||     __||   |   |
|        ||  _  ||    < |  -__||   ---||__     ||   |   |
|__|__|__||___._||__|__||_____||______||_______| \_____/  
```

makeCSV is a tool created to support users requiring CSVs to import metadata into [Archivematica](https://www.archivematica.org/en/). This Python script generates UTF8-encoded CSVs that lists the paths of all sub-directories and files within a given directory.

# Installing and Running makeCSV
makeCSV.py can be run from the command line if you have [python3](https://www.python.org/downloads/) installed. To run the script from the command line:

```
python3 makeCSV.py
```

If you don't have python3 on your machine, use one of the packaged files for Mac or Windows under the /dist folder. [You can download the latest package here](https://github.com/scholarsportal/makecsv/tags). 

For Mac, note that the package works only for ARM-based machines. If your Mac uses Intel, run makeCSV using the script above - attempting to run the package will return: ```Bad CPU Type in Executable```.

These self contained package files were generated using PyInstaller:

```
pyinstaller --onefile makeCSV.py
```

Once downloaded, double-click the file to open the program: ```makeCSV.exe``` on Windows or ```makeCSV``` on Mac.


# Using makeCSV
makeCSV can generate the following CSV files and will populate the files with the following information:
- ```metadata.csv```: populates the ```filename``` column with a list of all sub-directories and files within the ```objects``` directory.
- ```rights.csv```: populates the ```file``` column (not a typo!) with a list of all files within the ```objects``` directory and provides column headers for each PREMIS rights element.
- ```source-metadata.csv```: populates the ```metadata``` column with a list of all XML metadata files stored in the ```metadata``` directory. For each entry, the corresponding ```filename``` value is prefilled as ```objects```. Only generated if XML files are found in the ```metadata``` directory.

A ```log.txt``` file will also be created if makeCSV identifies and/or replaces characters that Archivematica cannot handle (e.g., spaces, commas, non-Latin characters).

Once open, makeCSV will provide a series of prompts to determine what and how CSV files should be generated:
1. ```Please enter the directory path```: enter the full path to the top-level directory of your transfer e.g., ```H/Desktop/Permafrost/nameOfTransfer```. The objects that you are preserving must be stored in an ```objects``` sub-directory within this transfer.
2. ```It looks like a metadata folder already exists. Your CSV files will get overwritten. Continue? (y/n)```: This prompt will appear if your transfer already has a ```metadata``` directory. If you do not want existing CSV files (if named metadata.csv, rights.csv, or source-metadata.csv) to be overwritten, enter "n". This will exit the program. Otherwise, enter "y" to proceed.
3. ```Looks like you're doing an XML Import. Generate source-metadata.csv, metadata.csv and rights.csv? (y/n)```: This prompt will only appear if makeCSV finds XML files in a ```metadata``` directory, and will generate all 3 CSV files. If you do not want to generate any CSVs, enter "n" to exit the program. Otherwise, enter "y" to proceed.
4. ```Is this a bagged transfer type (y/n)```: enter "y" if you plan to bag the transfer so that ```data/``` will be appended to filenames as appropriate. Otherwise, enter "n" to proceed.

A notification will appear in the terminal as each CSV file is created. Navigate to the ```metadata``` directory in your transfer to review and edit the files.

Warning messages beginning with ```!!!``` will also appear if makeCSV identifies characters that Archivematica cannot handle while generating the CSVs. These warnings will be collated in a ```log.txt``` file, also stored in the ```metadata``` directory. See Resources for details about Archivematica's requirements.
- In the CSV files, makeCSV will replace blank spaces as well as the following characters with an underscore in folder paths, per Archivematica's requirements (these characters do not need to be replaced in file paths): ```!@#$%^&*()=+[]{};':"<>?\`~```
- Non-Latin characters and characters with accent marks will be flagged but not replaced to ensure transliterations reflect their context appropriately. These should be manually replaced in the CSV and the physical file and/or folder name by the user according to Archivematica's requirements. Note also that non-Latin characters and accent marks in CSV files may not display properly in MS Excel due to limitations in Excel for handling encoding for CSV files. These characters will render properly when CSV files are opened in text editors.

# Resources
For more information about importing metadata into Archivematica, please refer to our [Guide to User-Submitted Metadata in Archivematica](https://learn.scholarsportal.info/all-guides/a-guide-to-user-submitted-metadata-in-archivematica/).
