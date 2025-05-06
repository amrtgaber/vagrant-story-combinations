import os
import re

INPUT_FILE = "../vagrant_story_combinations_guide.txt"  # Path to the input guide file
OUTPUT_DIR = "../csv"  # Directory to save the output CSV files


def extract_tables_from_guide():
    # Create a folder to store the output files
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    # Read the contents of the file
    with open(INPUT_FILE, "r") as file:
        guide_text = file.read()

    # Regular expression to find the table title and content
    table_regex = re.compile(
        r"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n(.+?)\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n(.+?)(?=\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|\Z)",
        re.DOTALL,
    )

    # Find all tables in the guide
    tables: list[str] = re.findall(table_regex, guide_text)

    # Iterate over all tables found
    for title, table_content in tables:
        # Skip material tables
        if "Material" in title:
            continue

        # Clean the title to make it a valid filename
        clean_title = (
            title.strip()
            .replace(" + ", "_")
            .replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
            .replace("Combinations", "")
        )
        filename = f"{OUTPUT_DIR}/{clean_title}.csv"

        # Extract only the item names (removing headers and other unnecessary parts)
        # Look for rows that contain the format of "item + item -> item"
        item_rows = []
        item_row_regex = re.compile(
            r"([A-Za-z\s]+?)\s{2,}([A-Za-z\s]+?)\s{2,}([A-Za-z\s\+\-]+?)(?:\s{2,}([A-Za-z\s\+\-]+))?$"
        )

        for line in table_content.splitlines():
            if (
                line.startswith("First Slot")
                or line.startswith("=")
                or line.startswith(" ")
            ):
                continue

            match = item_row_regex.match(line.strip())
            if match:
                item1, item2, result, swap = match.groups()
                item_rows.append(
                    f"{item1.strip()}, {item2.strip()}, {result.strip()}{f', {swap.strip()}' if swap is not None else ''}"
                )

        # Write the filtered item rows to a file
        with open(filename, "w") as file:
            file.write("first slot, second slot, result, swap\n")  # Header
            file.write("\n".join(item_rows))

        print(
            f"Wrote {len(item_rows)} lines for table '{title.strip()}' saved as '{filename}'."
        )

    print(f"{len(tables)} total tables extracted.")


# Run the function to extract and save each table
extract_tables_from_guide()
