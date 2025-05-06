# Vagrant Story item combination scripts

Scripts that extract item combination data and output csv files.

## Run all scripts

```bash
python ./scripts/run_all.py
```

## Run individual script

```bash
python ./scripts/all_combo_tables_extracter.py
```

This script reads the whole guide as input then outputs csv files for every "type" combination table to the `csv/` folder.

```bash
python ./scripts/<armor | blade | shield>_material_table_parser.py
```

These scripts read copies of the material tables placed in the `material_tables/` folder and output csv files of all the material combinations to the `csv/` folder. The copies of the material tables used as inputs have minor added white space to align all the first columns.

## Credits

Credit to JTilton and his amazing combinations guide on gamefaqs. Link to the original guide: https://gamefaqs.gamespot.com/ps/914326-vagrant-story/faqs/8485.

## License

[MIT licensed](LICENSE).
