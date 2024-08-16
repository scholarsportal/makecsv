import os
import csv
import re
import sys

def find_special_characters(text, log):
    # Define a regular expression pattern to match special characters
    special_chars = re.findall(r'[^a-zA-Z0-9\\/]', text)
    
    if special_chars:
        writer = csv.writer(log)
        msg = "Special characters found [" + ''.join(special_chars) + "] in " + text
        print("!!! " + msg)
        writer.writerow([msg])

def find_non_latin(text, log):
    # Regular expression to match any non-Latin character
    non_latin = re.findall(r'[^\u0000-\u007F\u0080-\u00FF]', text)
    
    if non_latin:
        writer = csv.writer(log)
        msg = "Non Latin characters found [" + ''.join(non_latin) + "] in " + text
        print("!!! " + msg)
        writer.writerow([msg])

def list_directory_contents(directory):
    try:
        # Get the list of files and directories
        while True:
          try:
            if not os.path.exists(directory+'/objects'):
              print("Your files need to be placed within a folder named 'objects' first.")
              directory = input("Please enter the directory path again: ").strip()
            else:
              break
          except ValueError as e:
              print(f"An error occurred: {e}")

        # Prepare the CSV file
        if not os.path.exists(directory+'/metadata'): 
          os.mkdir(directory+'/metadata')
        else:
          while True:
            try:
              overwrite = input("It looks like a metadata folder already exists and will get overwritten. Continue? (y/n)")
              if overwrite == 'y':
                 break
              else:
                print("Okay bye!")
                sys.exit()
            except ValueError as e:
                print(f"An error occurred: {e}")

                        
        meta_file = os.path.join(directory+'/metadata', "metadata.csv")
        rights_file = os.path.join(directory+'/metadata', "rights.csv")
        log_file = os.path.join(directory+'/metadata', "log.txt")

        while True:
          try:
              bagged = input("Is this a bagged transfer type (y/n): ")
              if bagged == 'y' or bagged == 'n':
                break
              else:
                print("You need to actually type either 'y' for yes or 'n' for no")   
          except ValueError as e:
              print(f"An error occurred: {e}")
        
        with open(meta_file, mode='w', newline='', encoding='utf-8') as file1, \
          open(rights_file, mode='w', newline='', encoding='utf-8') as file2, \
          open(log_file, mode='w', newline='', encoding='utf-8') as logfile:
            
            writer1 = csv.writer(file1)
            writer1.writerow(["filename"])

            writer2 = csv.writer(file2)
            writer2.writerow([
               "file",
               "basis",
               "status",
               "jurisdiction",
               "determination_date",
               "start_date",
               "end_date",
               "grant_act",
               "grant_restriction"
               ])

            # Walk through the directory tree
            for root, dirs, files in os.walk(directory, topdown=True):
                dirs.sort()
                files.sort()
                # Write directories
                for dir_name in dirs:
                    full_path = os.path.join(root, dir_name)
                    relative_path = os.path.relpath(full_path, directory)
                    if not relative_path.startswith("metadata"):
                      find_special_characters(relative_path, logfile)
                      find_non_latin(relative_path, logfile)
                      clean_text = re.sub(r'[^a-zA-Z0-9\\/]', '_', relative_path)   
                      writer1.writerow([clean_text])

                # Write files
                for file_name in files:
                    full_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(full_path, directory)
                    # Skip the metadata file that's generated
                    if not relative_path.startswith("metadata"):
                      # Skip any hidden files like .DS_Store
                      if not file_name.startswith('.'):
                        find_non_latin(relative_path, logfile)
                        if bagged == 'yes': 
                          writer1.writerow(['data/'+relative_path])
                          writer2.writerow(['data/'+relative_path])
                        else:
                          writer1.writerow([relative_path])
                          writer2.writerow([relative_path])

        print(f"metadata.csv and rights.csv files have been created successfully.")
        
        if os.path.getsize(directory+'/metadata/log.txt') == 0:
          os.remove(directory+'/metadata/log.txt')

        while True:
          try:
              another = input("Would you like to process another directory? (y/n): ")
              if another == 'y' or another == 'n':
                if another == 'y':
                  main()
                else:
                  print("Okay bye!")
                  sys.exit()
              else:
                print("You need to actually type either 'y' for yes or 'n' for no")   
          except ValueError as e:
              print(f"An error occurred: {e}")


    except FileNotFoundError:
        print("The directory path you provided does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("""\
            _        ___ _____   __
 _ __  __ _| |_____ / __/ __\ \ / /
| '  \/ _` | / / -_) (__\__ \\\ V / 
|_|_|_\__,_|_\_\___|\___|___/ \_/                                    

              """)
    directory = input("Please enter the directory path: ").strip()
    list_directory_contents(directory)

if __name__ == "__main__":
    main()