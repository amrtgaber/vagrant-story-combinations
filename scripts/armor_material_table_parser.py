from material_table_parser import parse_materials_from_tables

parse_materials_from_tables(
    filename="Armor_materials",
    slot_order=["Helm", "Body", "Leg", "Arm"],
    material_order=["L", "B", "I", "H", "S", "D"],
    cell_start=9,
)
