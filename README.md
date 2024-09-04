```
                  __            ______  _______  ___ ___ 
.--------..---.-.|  |--..-----.|      ||     __||   |   |
|        ||  _  ||    < |  -__||   ---||__     ||   |   |
|__|__|__||___._||__|__||_____||______||_______| \_____/  
```

makeCSV is a Python script developed to generate a list of paths of all sub-directories and files within a given directory. This tool was created to support users who are importing descriptive metadata via CSV into Archivematica.

You can either run the script from your command line: 

```
python3 makeCSV.py
```

Or use one of the following packaged files under the /dist folder, which don't require having Python installed on your machine.

These self contained files were generated using [PyInstaller](https://pyinstaller.org/en/stable/installation.html), like so:

```
pyinstaller --onefile makeCSV.py
```

For more information about importing metadata into Archivematic, please refer to our guide:

[https://learn.scholarsportal.info/all-guides/a-guide-to-user-submitted-metadata-in-archivematica/](https://learn.scholarsportal.info/all-guides/a-guide-to-user-submitted-metadata-in-archivematica/)