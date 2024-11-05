import os
# Converts all the .dat files in the scena folder to .py files
# It needs the dat2py.py script to be in the same folder
if __name__ == "__main__":
    scena_path = "./scena"
    # for each file in scena
    for file in os.listdir(scena_path):
        # if the file is a .tbl file
        if file.endswith(".dat"):
            # call dat2py.py to convert the .dat file to a .py file 
            os.system("python dat2py.py " + os.path.join(scena_path, file))
            