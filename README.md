# Tile assembler
----
A quick program that uses tiles exported from applications such as game maps, and stitches them together into one high resolution image

## Installation
1. Download the source code for the project
2. Install pip package "pillow"
3. Run application

## Usage

### Use command line arguments
- `-h` or `--help`
    Displays usage guide
- `-p` or `--path`
    Path to the folder containing the images (default: ./images/)
- `-f` or `--file_name`
    Regex to match the file name (default: ^([\\d]*)_([\\d]*))

### Run without command line arguments
The application will ask if the user would like to change any of the options or use the default one.