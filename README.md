# Project Summarizer for LLM

This tool summarizes the contents of a directory, including its subdirectories and files, and outputs the summary to text files. These files are for uploading when asking large language models (LLMs) like ChatGPT or Claude for information about a project.

## Features

- Generates a tree structure of the directory and its contents.
- Outputs the contents of all non binary files to a series of text files.
- Splits the output into multiple files if the size exceeds 4MB.

## Installation

To use this tool, you can install the required dependencies using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

## Usage

To summarize a directory and output the summary to a specified output directory, run the following command:

```bash
poetry run python src/summarizer.py [path-to-directory] [path-to-output-directory]
```
Replace [path-to-directory] with the path to the directory you want to summarize, and [path-to-output-directory] with the path to the directory where you want to save the output files.