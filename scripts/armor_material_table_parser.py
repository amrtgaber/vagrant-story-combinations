import csv
import os

INPUT_FILE = "../material_tables/Armor_materials.txt"
OUTPUT_DIR = "../csv"
OUTPUT_FILE = f"{OUTPUT_DIR}/Armor_materials.csv"
SLOT_ORDER = ["Helm", "Body", "Leg", "Arm"]
MATERIAL_ORDER = ["L", "B", "I", "H", "S", "D"]
SLOT_SIZE = len(MATERIAL_ORDER)
CELL_START = 9  # Skip to first real cell


def parse_cell(value):
    """Extract base material and upgrade/downgrade flags"""
    if not value:
        return "", False, False
    is_upgrade = value.startswith("+")
    is_downgrade = value.startswith("-")
    base = value[-1]
    return base, is_upgrade, is_downgrade


def extract_materials(line):
    """Split line into materials"""
    # Extract line into list of materials
    cells = [cell for cell in line.split() if line.strip()]
    # split list into blocks
    blocks = [cells[i : i + SLOT_SIZE] for i in range(0, len(cells), SLOT_SIZE)]
    return blocks


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    with open(INPUT_FILE, "r") as file:
        lines = [line.rstrip() for line in file if line.strip()]

    lines = lines[4:]  # Skip header lines
    output_rows = []
    second_slot_idx = 0
    row_idx = 0
    for line in lines:
        if line.startswith("-------"):
            second_slot_idx += 1
            row_idx = 0
            continue

        blocks = extract_materials(line[CELL_START:])

        first_slot_idx = 0
        for block in blocks:
            cell_idx = 0
            for cell in block:
                result_material, is_upgrade, is_downgrade = parse_cell(cell)
                output_rows.append(
                    {
                        "slot1": SLOT_ORDER[first_slot_idx],
                        "slot2": SLOT_ORDER[second_slot_idx],
                        "material1": MATERIAL_ORDER[cell_idx],
                        "material2": MATERIAL_ORDER[row_idx],
                        "result_material": result_material,
                        "is_upgrade": is_upgrade,
                        "is_downgrade": is_downgrade,
                    }
                )
                cell_idx += 1
            first_slot_idx += 1
        row_idx += 1

    # Write to CSV
    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "slot1",
                "slot2",
                "material1",
                "material2",
                "result_material",
                "is_upgrade",
                "is_downgrade",
            ],
        )
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"✅ Extracted {len(output_rows)} combinations to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
