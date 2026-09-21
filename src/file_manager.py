import shutil
from pathlib import Path


# ---------------------------------------------------------
# Project Configuration
# ---------------------------------------------------------

WORKSPACE = Path("workspace")


# ---------------------------------------------------------
# Validation Functions
# ---------------------------------------------------------

def validate_path(path_text):
    """Convert user input into a Path object."""

    if not path_text.strip():
        raise ValueError("Path cannot be empty.")

    return Path(path_text.strip())


def validate_existing_path(path):
    """Check whether the given path exists."""

    if not path.exists():
        raise FileNotFoundError(
            f"Path does not exist: {path}"
        )


def validate_directory(directory):
    """Check whether the given path is a directory."""

    validate_existing_path(directory)

    if not directory.is_dir():
        raise NotADirectoryError(
            f"Not a directory: {directory}"
        )


def validate_file(file_path):
    """Check whether the given path is a file."""

    validate_existing_path(file_path)

    if not file_path.is_file():
        raise ValueError(
            f"Path is not a file: {file_path}"
        )


# ---------------------------------------------------------
# File Listing
# ---------------------------------------------------------

def list_files(directory):
    """Return all files and folders inside a directory."""

    validate_directory(directory)

    return sorted(
        directory.iterdir(),
        key=lambda path: path.name.lower()
    )


def display_files(directory):
    """Display files and folders inside a directory."""

    items = list_files(directory)

    print("\n" + "=" * 65)
    print(f"CONTENTS OF: {directory}")
    print("=" * 65)

    if not items:
        print("Directory is empty.")
        print("=" * 65)
        return

    for item in items:

        if item.is_dir():
            item_type = "Folder"
        else:
            item_type = "File"

        print(f"{item_type:<10} {item.name}")

    print("=" * 65)


# ---------------------------------------------------------
# Folder Operations
# ---------------------------------------------------------

def create_folder(folder_path):
    """Create a new folder."""

    if folder_path.exists():
        raise FileExistsError(
            f"Folder or path already exists: {folder_path}"
        )

    folder_path.mkdir(
        parents=True,
        exist_ok=False
    )

    return True


# ---------------------------------------------------------
# Copy Operation
# ---------------------------------------------------------

def copy_file(source, destination):
    """Copy a file to the destination."""

    validate_file(source)

    if destination.exists() and destination.is_dir():
        destination = destination / source.name

    if destination.exists():
        raise FileExistsError(
            f"Destination already exists: {destination}"
        )

    destination.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy2(
        source,
        destination
    )

    return destination


# ---------------------------------------------------------
# Move Operation
# ---------------------------------------------------------

def move_file(source, destination):
    """Move a file to the destination."""

    validate_file(source)

    if destination.exists() and destination.is_dir():
        destination = destination / source.name

    if destination.exists():
        raise FileExistsError(
            f"Destination already exists: {destination}"
        )

    destination.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.move(
        str(source),
        str(destination)
    )

    return Path(destination)


# ---------------------------------------------------------
# Rename Operation
# ---------------------------------------------------------

def rename_file(source, new_name):
    """Rename an existing file."""

    validate_file(source)

    if not new_name.strip():
        raise ValueError(
            "New file name cannot be empty."
        )

    new_name = new_name.strip()

    if Path(new_name).name != new_name:
        raise ValueError(
            "New name must contain only a file name, "
            "not a path."
        )

    destination = source.parent / new_name

    if destination.exists():
        raise FileExistsError(
            f"A file with this name already exists: "
            f"{destination}"
        )

    source.rename(destination)

    return destination


# ---------------------------------------------------------
# Delete Operation
# ---------------------------------------------------------

def delete_file(file_path):
    """Delete a file."""

    validate_file(file_path)

    file_path.unlink()

    return True


# ---------------------------------------------------------
# Search Operation
# ---------------------------------------------------------

def search_files(directory, search_text):
    """Search files and folders recursively by name."""

    validate_directory(directory)

    if not search_text.strip():
        raise ValueError(
            "Search text cannot be empty."
        )

    search_text = search_text.strip().lower()

    results = []

    for path in directory.rglob("*"):

        if search_text in path.name.lower():
            results.append(path)

    return sorted(
        results,
        key=lambda path: str(path).lower()
    )


# ---------------------------------------------------------
# File Information
# ---------------------------------------------------------

def get_file_info(file_path):
    """Return basic information about a file."""

    validate_file(file_path)

    file_size = file_path.stat().st_size

    extension = file_path.suffix

    if not extension:
        extension = "No extension"

    return {
        "name": file_path.name,
        "path": str(file_path.resolve()),
        "size_bytes": file_size,
        "extension": extension,
    }


def display_file_info(file_path):
    """Display basic information about a file."""

    info = get_file_info(file_path)

    print("\n" + "=" * 55)
    print("FILE INFORMATION")
    print("=" * 55)

    print(f"Name      : {info['name']}")
    print(f"Path      : {info['path']}")
    print(f"Size      : {info['size_bytes']} bytes")
    print(f"Extension : {info['extension']}")

    print("=" * 55)


# ---------------------------------------------------------
# User Input Functions
# ---------------------------------------------------------

def get_path_from_user(prompt):
    """Get a non-empty path from the user."""

    while True:

        path_text = input(prompt)

        try:
            return validate_path(path_text)

        except ValueError as error:
            print(f"Error: {error}")


# ---------------------------------------------------------
# Menu Handlers
# ---------------------------------------------------------

def handle_list_files():
    """Handle the list-files operation."""

    try:

        directory = get_path_from_user(
            "Enter directory path: "
        )

        display_files(directory)

    except (
        FileNotFoundError,
        NotADirectoryError,
    ) as error:

        print(f"Error: {error}")


def handle_create_folder():
    """Handle the create-folder operation."""

    try:

        folder_path = get_path_from_user(
            "Enter new folder path: "
        )

        create_folder(folder_path)

        print(
            f"Folder created successfully: "
            f"{folder_path}"
        )

    except (
        FileExistsError,
        ValueError,
    ) as error:

        print(f"Error: {error}")


def handle_copy_file():
    """Handle the copy-file operation."""

    try:

        source = get_path_from_user(
            "Enter source file path: "
        )

        destination = get_path_from_user(
            "Enter destination path: "
        )

        result = copy_file(
            source,
            destination
        )

        print(
            f"File copied successfully to: "
            f"{result}"
        )

    except (
        FileNotFoundError,
        ValueError,
        FileExistsError,
        OSError,
    ) as error:

        print(f"Error: {error}")


def handle_move_file():
    """Handle the move-file operation."""

    try:

        source = get_path_from_user(
            "Enter source file path: "
        )

        destination = get_path_from_user(
            "Enter destination path: "
        )

        result = move_file(
            source,
            destination
        )

        print(
            f"File moved successfully to: "
            f"{result}"
        )

    except (
        FileNotFoundError,
        ValueError,
        FileExistsError,
        OSError,
    ) as error:

        print(f"Error: {error}")


def handle_rename_file():
    """Handle the rename-file operation."""

    try:

        source = get_path_from_user(
            "Enter file path: "
        )

        new_name = input(
            "Enter new file name: "
        )

        result = rename_file(
            source,
            new_name
        )

        print(
            f"File renamed successfully to: "
            f"{result}"
        )

    except (
        FileNotFoundError,
        ValueError,
        FileExistsError,
    ) as error:

        print(f"Error: {error}")


def handle_delete_file():
    """Handle the delete-file operation."""

    try:

        file_path = get_path_from_user(
            "Enter file path to delete: "
        )

        confirmation = input(
            f"Are you sure you want to delete "
            f"'{file_path.name}'? (yes/no): "
        ).strip().lower()

        if confirmation != "yes":

            print("Delete operation cancelled.")
            return

        delete_file(file_path)

        print(
            f"File deleted successfully: "
            f"{file_path}"
        )

    except (
        FileNotFoundError,
        ValueError,
        OSError,
    ) as error:

        print(f"Error: {error}")


def handle_search_files():
    """Handle the file-search operation."""

    try:

        directory = get_path_from_user(
            "Enter directory to search: "
        )

        search_text = input(
            "Enter file/folder name to search: "
        )

        results = search_files(
            directory,
            search_text
        )

        print("\n" + "=" * 65)
        print("SEARCH RESULTS")
        print("=" * 65)

        if not results:

            print(
                "No matching files or folders found."
            )

        else:

            for result in results:
                print(result)

        print("=" * 65)

    except (
        FileNotFoundError,
        NotADirectoryError,
        ValueError,
    ) as error:

        print(f"Error: {error}")


def handle_file_info():
    """Handle the file-information operation."""

    try:

        file_path = get_path_from_user(
            "Enter file path: "
        )

        display_file_info(file_path)

    except (
        FileNotFoundError,
        ValueError,
    ) as error:

        print(f"Error: {error}")


# ---------------------------------------------------------
# Main Application
# ---------------------------------------------------------

def main():
    """Run the File Management Utility."""

    WORKSPACE.mkdir(
        parents=True,
        exist_ok=True
    )

    while True:

        print("\n")
        print("=" * 50)
        print("       FILE MANAGEMENT UTILITY")
        print("=" * 50)

        print("1. List Files")
        print("2. Create Folder")
        print("3. Copy File")
        print("4. Move File")
        print("5. Rename File")
        print("6. Delete File")
        print("7. Search Files")
        print("8. File Information")
        print("9. Exit")

        print("=" * 50)

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            handle_list_files()

        elif choice == "2":

            handle_create_folder()

        elif choice == "3":

            handle_copy_file()

        elif choice == "4":

            handle_move_file()

        elif choice == "5":

            handle_rename_file()

        elif choice == "6":

            handle_delete_file()

        elif choice == "7":

            handle_search_files()

        elif choice == "8":

            handle_file_info()

        elif choice == "9":

            print(
                "\nThank you for using "
                "File Management Utility!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select an option from 1 to 9."
            )


# ---------------------------------------------------------
# Program Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()