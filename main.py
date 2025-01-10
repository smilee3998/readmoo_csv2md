import argparse
from pathlib import Path

import pandas as pd


def csvtoMarkdown(csv_file: Path, output: Path = Path("."), sort: str = "added_time"):
    df = pd.read_csv(csv_file)
    book_title = csv_file.stem

    # Sort the highlights by added_time or chapter
    if sort == "added_time":
        df.sort_values(by=["劃線時間"], inplace=True)
    elif sort == "chapter":
        df.sort_values(by=["章節"], inplace=True)

    previous_chapter = -1
    # Create a markdown file
    md_content = f"# {book_title}\n## Highlights\n"
    for _, row in df.iterrows():
        if sort == "chapter" and row["章節"] != previous_chapter:
            # add a new chapter header
            md_content += f"\n### Chapter {row['章節']}\n"
            previous_chapter = row["章節"]
        # add the highlight content
        md_content += f"- {row['劃線內容'].replace("\n", "\n\t")}\n"

    md_file = output / f"{book_title}.md"

    # Check if the file exists
    if md_file.exists():
        # check if the file is the same
        with open(md_file, "r", encoding="utf-8") as f:
            if f.read() == md_content:
                return
        # ask for confirmation to overwrite
        overwrite = input(f"{md_file} already exists. Overwrite? (y/n): ")
        if overwrite.lower() != "y":
            print(f"Skipped {csv_file}")
            return

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Converted {csv_file} to {md_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Readmoo CSV to Markdown")
    parser.add_argument(
        "csv_file",
        type=str,
        help="Path to the CSV file or directory containing CSV files",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output directory for the generated Markdown files",
        required=False,
    )
    # add option to sort by added_time or chapter
    parser.add_argument(
        "--sort",
        type=str,
        help="Sort the highlights by added_time or chapter",
        choices=["added_time", "chapter"],
        required=False,
    )
    args = parser.parse_args()
    csv_file = Path(args.csv_file)
    sort = args.sort if args.sort else "added_time"

    if csv_file.is_file() and csv_file.suffix == ".csv":
        output_path = Path(args.output) if args.output else csv_file.parent
        csvtoMarkdown(csv_file, output_path, sort)
    elif csv_file.is_dir():
        for csv in csv_file.glob("*.csv"):
            output_path = Path(args.output) if args.output else csv_file
            csvtoMarkdown(csv, output_path, sort)
