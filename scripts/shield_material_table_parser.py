from material_table_parser import parse_materials_from_tables

parse_materials_from_tables(
    filename="Shield_materials",
    slot_order=["Shield"],
    material_order=["W", "B", "I", "H", "S", "D"],
    cell_start=9,
)
