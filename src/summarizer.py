import os
import typer
from typing import List

app = typer.Typer()

def is_binary(file_path: str) -> bool:
    try:
        with open(file_path, 'r') as file:
            file.read()
        return False
    except:
        return True

def generate_tree(directory: str, prefix: str = "") -> str:
    tree = ""
    files = sorted(os.listdir(directory))
    for i, filename in enumerate(files):
        if filename.startswith('.'):
            continue
        path = os.path.join(directory, filename)
        if i == len(files) - 1:
            tree += f"{prefix}└── {filename}\n"
            if os.path.isdir(path):
                tree += generate_tree(path, prefix + "    ")
        else:
            tree += f"{prefix}├── {filename}\n"
            if os.path.isdir(path):
                tree += generate_tree(path, prefix + "│   ")
    return tree

def summarize_directory(directory: str, output_dir: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_count = 0
    output_file_path = os.path.join(output_dir, f'summary_{file_count}.txt')
    output_file = open(output_file_path, 'w', encoding='utf-8')

    tree = generate_tree(directory)
    output_file.write(f"Directory Tree:\n{tree}\n")

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            file_path = os.path.join(root, file)
            if is_binary(file_path):
                continue

            output_file.write(f'File: {file_path}\n')

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                output_file.write(content + '\n\n')

            if os.path.getsize(output_file_path) > 4 * 1024 * 1024:  # 4MB
                output_file.close()
                file_count += 1
                output_file_path = os.path.join(output_dir, f'summary_{file_count}.txt')
                output_file = open(output_file_path, 'w', encoding='utf-8')

    output_file.close()

@app.command()
def main(directory: str = typer.Argument(..., help="The directory to summarize"),
        output_dir: str = typer.Argument(..., help="The directory to store the summary files")):
    summarize_directory(directory, output_dir)

if __name__ == "__main__":
    app()
