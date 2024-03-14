import os
import sys
import pytest

from src.summarizer import summarize_directory, generate_tree

def test_generate_tree(tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file1.txt").write_text("This is file 1.")
    (test_dir / "file2.txt").write_text("This is file 2.")

    expected_tree = "├── file1.txt\n└── file2.txt\n"
    assert generate_tree(str(test_dir)) == expected_tree

def test_summarize_directory(tmp_path):
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file1.txt").write_text("This is file 1.")
    (test_dir / "file2.txt").write_text("This is file 2.")

    output_dir = tmp_path / "output"
    summarize_directory(str(test_dir), str(output_dir))

    assert len(list(output_dir.iterdir())) == 1
    with open(output_dir / "summary_0.txt", 'r') as f:
        content = f.read()
        assert "This is file 1." in content
        assert "This is file 2." in content
        assert "├── file1.txt\n└── file2.txt\n" in content
