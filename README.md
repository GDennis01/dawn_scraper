## Script Dumper for The Legend of Heroes: Trails through Daybreak
These python scripts let you dump the english script for the game The Legend of Heroes: Trails through Daybreak.
They are quite messy but they do the job.

## Info
File list:
- `scena/` folder containing all the .dat files from the game. You can get them by using the ph3 tool on the game's data folder.
- `files/t_name.json` file containing the names of the characters. You can get it from the game's data folder just like the scena folder.
- `files/converted_files/` : .dat files converted to .py files
- `files/csv_files/` : scraped csv files from the trails api(in json format lol)
- `files/refined_csv_files/` : files/csv_files/ converted to proper csv files just like you would get from clicking "export" on the trailsinthedatabse website
- `files/refined_texts/` : refined texts in the form of (CharacterName,Dialogue)
- `files/name_lens.txt` : number of lines for each file, used for debugging

- `final_csvs/`: final csvs ready for the delivery

- `scena/`: all .dat files from the scena folder dumped through the use of the ph3 tool.


`main.py`: from the converted_files/ folder, this script will convert all the .py files to refined_texts

`whole_scena_to_py.py`: convert the .dat files in the scena folder to .py files inside files/converted_files/
`join_csv.py`: join refined_csv_files with csv_files

`download_all_csv_files.py`: contains the commented  script that downloads all the csv files from the trails api. It also convert them from json to csv,saving them to refined_csv_files/


## How to run
1. Put `.dat` files in the `scena/` folder by using the PH3 Tool on the game's data folder
2. Convert `.dat` files to `.py` files by running `whole_scena_to_py.py`. It accepts as argument the path to the `dat2py.py` file from [KuroTools](https://github.com/nnguyen259/KuroTools)
3. Get the `t_name.json` file from the game's data folder and put it in the `files/` folder   
4. Run `main.py` to convert the `.py` files to refined texts
5. Run `download_all_csv_files.py` to download all the csv files from the trailsinthedatabase website
6. Run `join_csv.py` to join the csv files with the refined texts
7. The final csv files will be in the `final_csvs/` folder

