import zipfile

# Specify the file names, and asks users input here:
str(input('Name of file 1:'))
file1 = "zophie.jpg" #names are define "hardcoded" for fuction
str(input("Name of files 2:"))
file2 = "ScotsWhaHae.mp3"

#archive name assigned.         
archive_name = "Compressed_Files.zip"

# Creates the new zip archive
with zipfile.ZipFile(archive_name, 'w', compression=zipfile.ZIP_DEFLATED) as myzip:#zip the files and compresses them 'w' writes them into the archive file. 

#Adds the first file
    myzip.write(file1)
    print(f"Added {file1} to the archive.")#prints success of files aadded to the archive

#Adds the second file
    myzip.write(file2)
    print(f"Added {file2} to the archive.")#sucess of file added to the archive

    print(f"Archive '{archive_name}' created!")#Prints the creation of the archive worked!

