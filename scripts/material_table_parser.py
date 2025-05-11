import csv
import os

from utils import parse_cell

current_dir = os.getcwd()
if "scripts" not in current_dir:
    os.chdir(".\\scripts")


def extract_materials(line, slot_size):
    """Split line into materials"""
    # Extract line into list of materials
    cells = [cell for cell in line.split() if line.strip()]
    # split list into blocks
    blocks = [cells[i : i + slot_size] for i in range(0, len(cells), slot_size)]
    return blocks


def parse_materials_from_tables(filename, slot_order, material_order, cell_start):
    input_file = f"../material_tables/{filename}.txt"
    output_dir = "../csv"
    output_file = f"{output_dir}/{filename}.csv"
    slot_size = len(material_order)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    with open(input_file, "r") as file:
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

        blocks = extract_materials(line[cell_start:], slot_size)

        first_slot_idx = 0
        for block in blocks:
            cell_idx = 0
            for cell in block:
                result_material, tier_change = parse_cell(cell)
                output_rows.append(
                    {
                        "slot1": slot_order[first_slot_idx],
                        "slot2": slot_order[second_slot_idx],
                        "material1": material_order[cell_idx],
                        "material2": material_order[row_idx],
                        "result_material": result_material,
                        "tier_change": tier_change,
                    }
                )
                cell_idx += 1
            first_slot_idx += 1
        row_idx += 1

    # Write to CSV
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "slot1",
                "slot2",
                "material1",
                "material2",
                "result_material",
                "tier_change",
            ],
        )
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Extracted {len(output_rows)} combinations to {output_file}")
