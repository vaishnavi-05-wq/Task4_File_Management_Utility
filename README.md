File Management Utility

A practical Python-based File Management Utility developed as part of the Skyrovix Internship.

The application provides a simple Command Line Interface (CLI) for performing common file and folder management operations such as listing, creating, copying, moving, renaming, deleting, searching, and viewing file information.

Project Objective

The objective of this project is to develop a complete working File Management Utility using Python development concepts.

The project focuses on:

Python modules

File and folder handling

Input validation

Data processing

Error handling

Recursive file searching

File information processing

Command Line Interface (CLI)

Automated unit testing

Project documentation

Features

The File Management Utility provides the following features:

List files and folders

Create new folders

Copy files

Move files

Rename files

Delete files with confirmation

Search files and folders recursively

Display file information

Input validation

Error handling

Automated unit testing

Project Structure

Task4_File_Management_Utility/
│
├── src/
│   └── file_manager.py
│
├── tests/
│   └── test_file_manager.py
│
├── workspace/
│
├── README.md
├── requirements.txt
└── .gitignore

File Description

src/file_manager.py

This is the main application file. It contains the complete File Management Utility and implements:

Path validation

File validation

Directory validation

File listing

Folder creation

File copying

File moving

File renaming

File deletion

Recursive searching

File information

User input handling

CLI menu

Error handling

tests/test_file_manager.py

Contains automated unit tests for the File Management Utility. The test suite verifies the main file-management operations as well as invalid input handling.

workspace/

A safe testing workspace used for manual file operations.

README.md

Contains the complete project documentation.

requirements.txt

Contains dependency information. This project uses only Python standard-library modules and does not require external packages.

.gitignore

Contains files and folders that should not be uploaded to GitHub, such as Python cache files and local environment files.

Technologies Used

Python 3

pathlib

shutil

unittest

Command Line Interface (CLI)

Git

GitHub

Python Modules Used

pathlib

Used for:

Creating and handling paths

Checking file and directory existence

Creating directories

Renaming files

Deleting files

Recursive searching

Getting file information

shutil

Used for:

Copying files

Moving files

unittest

The built-in unittest module is used for automated testing.

Installation

Step 1: Verify Python

Open PowerShell or Command Prompt and run:

python --version

Python 3 is required.

Step 2: Open the Project Directory

Navigate to the project directory:

cd Task4_File_Management_Utility

Step 3: Install Dependencies

No external dependencies are required because the project uses only Python standard-library modules.

Running the Application

Run the following command from the project root directory:

python .\src\file_manager.py

The application displays the following menu:

==================================================
       FILE MANAGEMENT UTILITY
==================================================
1. List Files
2. Create Folder
3. Copy File
4. Move File
5. Rename File
6. Delete File
7. Search Files
8. File Information
9. Exit
==================================================
Enter your choice:

Available Operations

1. List Files

Displays all files and folders present inside a selected directory.

Example:

Enter your choice: 1
Enter directory path: workspace

If the directory is empty, the application displays:

Directory is empty.

2. Create Folder

Creates a new folder at the specified location.

Example:

Enter your choice: 2
Enter new folder path: workspace\test_folder

Expected output:

Folder created successfully: workspace\test_folder

3. Copy File

Copies an existing file to another location.

Example:

Enter your choice: 3
Enter source file path: workspace\demo.txt
Enter destination path: workspace\test_folder

Expected output:

File copied successfully to: workspace\test_folder\demo.txt

4. Move File

Moves an existing file from one location to another.

Example:

Enter your choice: 4
Enter source file path: workspace\demo.txt
Enter destination path: workspace\moved_files

Expected output:

File moved successfully to: workspace\moved_files\demo.txt

5. Rename File

Changes the name of an existing file.

Example:

Enter your choice: 5
Enter file path: workspace\moved_files\demo.txt
Enter new file name: renamed_demo.txt

Expected output:

File renamed successfully to: workspace\moved_files\renamed_demo.txt

6. Delete File

Deletes a file after requesting confirmation.

Example:

Enter your choice: 6
Enter file path to delete: workspace\moved_files\renamed_demo.txt

The application asks:

Are you sure you want to delete 'renamed_demo.txt'? (yes/no):

The file is deleted only when the user enters:

yes

If any other response is entered, the operation is cancelled.

7. Search Files

Searches files and folders recursively.

Example:

Enter your choice: 7
Enter directory to search: workspace
Enter file/folder name to search: renamed

The search is case-insensitive and includes subdirectories.

8. File Information

Displays:

File name

Full file path

File size in bytes

File extension

Example:

Enter your choice: 8
Enter file path: workspace\example.txt

Input Validation

The application validates:

Empty paths

Non-existing paths

File paths

Directory paths

Empty search text

Empty file names

Invalid rename names

Existing destination files

Invalid menu choices

Example:

Error: Path cannot be empty.

Error Handling

The application handles common file-system errors including:

FileNotFoundError

FileExistsError

NotADirectoryError

ValueError

OSError

Errors are displayed to the user instead of causing the application to terminate unexpectedly.

Safe Delete Operation

The delete operation requires explicit confirmation.

Example:

Are you sure you want to delete 'example.txt'? (yes/no):

Only yes confirms deletion.

Example cancellation:

Delete operation cancelled.

Recursive Search

The search feature uses recursive directory traversal.

It searches:

The selected directory

Subdirectories

Nested folders

Files

Folders

The search is case-insensitive.

Automated Testing

The project includes automated unit tests using Python's built-in unittest framework.

Run:

python -m unittest discover -s tests -v

The test suite covers:

File listing

Folder creation

File copying

File moving

File renaming

File deletion

File searching

Case-insensitive searching

File information

Invalid path handling

Empty search input

Empty path input

Test Result

Ran 12 tests

OK

All 12 automated tests passed successfully.

Manual Testing

The application was manually tested using the workspace directory.

The following operations were verified:

List files

Create folder

Create a test file

Copy file

Move file

Rename file

Search file

View file information

Delete file

Delete confirmation

Exit application

Testing was performed inside the project workspace to avoid modifying important personal files.

Example Testing Workflow

Create Test Folder
       |
       v
Create Test File
       |
       v
List Files
       |
       v
Copy File
       |
       v
Move File
       |
       v
Rename File
       |
       v
Search File
       |
       v
View File Information
       |
       v
Delete File
       |
       v
Confirm Deletion

Project Architecture

The project follows a modular structure:

                    User
                      |
                      v
                 CLI Menu
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
     File          Folder         Search
   Operations     Operations     Operations
        |             |             |
        +-------------+-------------+
                      |
                      v
                Validation
                      |
                      v
                Error Handling
                      |
                      v
                 File System

The application separates operations into individual functions, making the code easier to understand, test, maintain, and extend.

Advantages

Simple command-line interface

Beginner-friendly design

Uses Python standard library

No external dependencies

Input validation

Error handling

Recursive searching

File information display

Safe delete confirmation

Automated unit testing

Modular code structure

Easy to extend

Practical real-world use case

Limitations

The current version:

Is a command-line application

Does not provide a graphical user interface

Deletes files but does not delete directories

Does not maintain operation history

Does not provide an undo feature

Does not provide advanced file filtering

Does not provide cloud storage integration

Does not include file preview functionality

Future Improvements

Possible future improvements include:

Graphical User Interface using Tkinter

Batch file operations

File filtering by extension

File sorting by size

File sorting by modification date

Operation history

Undo functionality

Directory deletion with confirmation

File compression

File extraction

Duplicate file detection

Logging system

Progress indicators

File preview

Advanced search filters

Cloud storage integration

Learning Outcomes

This project helped practice:

Python functions

Python modules

pathlib

shutil

File handling

Directory handling

Path manipulation

Recursive directory traversal

Data processing

Input validation

Exception handling

Command-line applications

Unit testing

Project organization

Git

GitHub

Technical documentation

Internship Information

Internship: Skyrovix

Task: File Management Utility

Task Number: Task 4

Due Date: 10 October 2026

Required Concepts

The project covers:

Python modules

Input validation

Data processing

Error handling

Working file management utility

Documented workflow

Testing

Project submission

Project Status

Status: Completed

The project includes:

Complete working Python application

File management operations

Folder management

Input validation

Error handling

Recursive search

File information

Safe deletion confirmation

Automated testing

Manual testing

Documentation

Final Testing Status

Automated Tests : 12/12 Passed
Manual Testing  : Completed
Documentation   : Completed

Requirements

This project does not require third-party Python packages.

The application uses the following standard-library modules:

pathlib
shutil
unittest

Therefore, no additional package installation is required.

How to Test the Project

Run Automated Tests

From the project root directory:

python -m unittest discover -s tests -v

Expected result:

Ran 12 tests

OK

Run the Application

python .\src\file_manager.py

Recommended Testing Directory

For manual testing, use:

workspace

Using a dedicated workspace helps keep testing operations separate from personal files.

Safety Note

This utility performs real file-system operations such as:

Copying files

Moving files

Renaming files

Deleting files

Users should always verify the file path before performing an operation.

The delete operation requires confirmation, but the application should still be used carefully.

For learning and testing purposes, the workspace directory is recommended.

GitHub

The complete source code, tests, documentation, and project files will be maintained in the GitHub repository created for this internship task.

GitHub Repository: https://github.com/vaishnavi-05-wq/Task4_File_Management_Utility

Author

Vaishnavi

License

This project was created for educational and internship purposes as part of the Skyrovix Internship.