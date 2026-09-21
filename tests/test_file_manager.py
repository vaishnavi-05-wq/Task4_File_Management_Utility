import tempfile
import unittest
from pathlib import Path

from src.file_manager import (
    copy_file,
    create_folder,
    delete_file,
    get_file_info,
    list_files,
    move_file,
    rename_file,
    search_files,
)


class TestFileManager(unittest.TestCase):
    """Test cases for the File Management Utility."""

    def setUp(self):
        """Create a temporary workspace before each test."""

        self.temp_directory = tempfile.TemporaryDirectory()

        self.workspace = Path(
            self.temp_directory.name
        )

        self.source_file = (
            self.workspace / "sample.txt"
        )

        self.source_file.write_text(
            "Hello File Manager",
            encoding="utf-8",
        )

    def tearDown(self):
        """Remove the temporary workspace after each test."""

        self.temp_directory.cleanup()

    def test_list_files(self):
        """Test listing files in a directory."""

        items = list_files(self.workspace)

        self.assertEqual(
            len(items),
            1,
        )

        self.assertEqual(
            items[0].name,
            "sample.txt",
        )

    def test_create_folder(self):
        """Test creating a new folder."""

        new_folder = (
            self.workspace / "documents"
        )

        result = create_folder(new_folder)

        self.assertTrue(result)

        self.assertTrue(
            new_folder.exists()
        )

        self.assertTrue(
            new_folder.is_dir()
        )

    def test_copy_file(self):
        """Test copying a file."""

        destination = (
            self.workspace / "copy.txt"
        )

        result = copy_file(
            self.source_file,
            destination,
        )

        self.assertTrue(
            destination.exists()
        )

        self.assertTrue(
            destination.is_file()
        )

        self.assertEqual(
            result,
            destination,
        )

        self.assertEqual(
            destination.read_text(
                encoding="utf-8"
            ),
            "Hello File Manager",
        )

    def test_move_file(self):
        """Test moving a file."""

        destination = (
            self.workspace / "moved.txt"
        )

        result = move_file(
            self.source_file,
            destination,
        )

        self.assertFalse(
            self.source_file.exists()
        )

        self.assertTrue(
            destination.exists()
        )

        self.assertTrue(
            destination.is_file()
        )

        self.assertEqual(
            result,
            destination,
        )

    def test_rename_file(self):
        """Test renaming a file."""

        result = rename_file(
            self.source_file,
            "renamed.txt",
        )

        expected = (
            self.workspace / "renamed.txt"
        )

        self.assertTrue(
            expected.exists()
        )

        self.assertFalse(
            self.source_file.exists()
        )

        self.assertEqual(
            result,
            expected,
        )

    def test_delete_file(self):
        """Test deleting a file."""

        result = delete_file(
            self.source_file
        )

        self.assertTrue(result)

        self.assertFalse(
            self.source_file.exists()
        )

    def test_search_files(self):
        """Test searching for files by name."""

        results = search_files(
            self.workspace,
            "sample",
        )

        self.assertEqual(
            len(results),
            1,
        )

        self.assertEqual(
            results[0].name,
            "sample.txt",
        )

    def test_search_is_case_insensitive(self):
        """Test that file search is case-insensitive."""

        results = search_files(
            self.workspace,
            "SAMPLE",
        )

        self.assertEqual(
            len(results),
            1,
        )

        self.assertEqual(
            results[0].name,
            "sample.txt",
        )

    def test_file_information(self):
        """Test retrieving file information."""

        info = get_file_info(
            self.source_file
        )

        self.assertEqual(
            info["name"],
            "sample.txt",
        )

        self.assertEqual(
            info["extension"],
            ".txt",
        )

        self.assertEqual(
            info["size_bytes"],
            len("Hello File Manager"),
        )

        self.assertIn(
            "path",
            info,
        )

    def test_invalid_path(self):
        """Test handling of a missing file."""

        missing_file = (
            self.workspace / "missing.txt"
        )

        with self.assertRaises(
            FileNotFoundError
        ):
            delete_file(missing_file)

    def test_empty_search(self):
        """Test validation for empty search text."""

        with self.assertRaises(
            ValueError
        ):
            search_files(
                self.workspace,
                "",
            )

    def test_empty_path(self):
        """Test validation for an empty path."""

        from src.file_manager import validate_path

        with self.assertRaises(
            ValueError
        ):
            validate_path("")


if __name__ == "__main__":
    unittest.main()