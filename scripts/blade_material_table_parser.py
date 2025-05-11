from material_table_parser import parse_materials_from_tables

parse_materials_from_tables(
    filename="Blade_materials",
    slot_order=[
        "Dagger",
        "Sword",
        "Great Sword",
        "AxeMace",
        "Great Axe",
        "Staff",
        "Heavy Mace",
        "Polearm",
        "Crossbow",
    ],
    material_order=["B", "I", "H", "S", "D"],
    cell_start=16,
)
