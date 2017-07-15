megpack
=======

(Un)Packer for .meg files used in Petroglyph games.


### Setup

```
sudo python3 setup.py install
```


### File Format Documentation

Courtesy of http://modtools.petrolution.net/docs/MegFileFormat:

```
Each Mega File begins with a header, followed by the Filename Table, the File Table and finally, the file data. All fields are in little-endian format.


Header:
  +0000h  numFilenames  uint32   ; Number of filenames in the Filename Table
  +0004h  numFiles      uint32   ; Number of files in the File Table

Filename Table record:
  +0000h  length        uint16   ; Length of the filename, in characters
  +0004h  name          length   ; The ASCII filename

File Table record:
  +0000h  crc           uint32   ; CRC-32 of the filename
  +0004h  index         uint32   ; Index of this record in the table
  +0008h  size          uint32   ; Size of the file, in bytes
  +000Ch  start         uint32   ; Start of the file, in bytes , from the start of the Mega File
  +0010h  name          uint32   ; Index in the Filename Table of the filename
```


### Usage

```
megpack

Usage:
    megpack pack [-f] <sourcefolder> <targetfile>
    megpack unpack [-f] <sourcefile> <targetfolder>
    megpack (-h | --help)
    megpack (-v | --version)

Commands:
    pack    Pack the contents of a folder into a .meg file
    unpack  Unpack a .meg file into a folder

Options:
    -f --force      Overwrite files that already exist.
    -h --help       Show usage information and exit.
    -v --version    Print the version number and exit.
```
