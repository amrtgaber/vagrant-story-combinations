import os
import subprocess

current_dir = os.getcwd()
if "scripts" not in current_dir:
    os.chdir(".\\scripts")

subprocess.run(["python", "all_combo_tables_extracter.py"])
subprocess.run(["python", "armor_material_table_parser.py"])
subprocess.run(["python", "blade_material_table_parser.py"])
subprocess.run(["python", "shield_material_table_parser.py"])
