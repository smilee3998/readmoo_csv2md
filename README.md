# ReadMoo CSV to Markdown Converter

This project provides a script to convert downloaded highlights from ReadMoo books into markdown notes.

## Features

- Convert ReadMoo highlights CSV to markdown format
- Organize highlights by book and chapter
- Easy to use command-line interface

## Installation

1. Clone the repository:
2. Navigate to the project directory:
    ```sh
    cd readmoo_csv2md
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To convert a ReadMoo highlights CSV file to markdown, run the following command:
```sh
python main.py path/to/highlights.csv
```

## Example
1. To convert a ReadMoo highlights CSV file to markdown in `added_time` order, run the following command:

```sh
python main.py highlights.csv --sort added_time
```

This will generate a markdown file with the same name as the CSV file, containing all the highlights formatted as markdown notes.

2. To convert ReadMoo highlights CSV files from a folder to markdown in `chapter` order to a specific output folder, run the following command:

```sh
python main.py path/to/folder/ --sort chapter --output path/to/output/folder/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
