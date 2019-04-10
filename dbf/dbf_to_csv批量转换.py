# 转载文件，如有侵权，请告知~~~
# Title:            DBFConverterToCSV
# Description:      Converte DBF files to CSV files
# Author:           Tobias Menzel
# # # # # # # # # # # # # # # # # # # # # # # # # # #
# Import modules
import dbfread
import subprocess as sub
import pandas as pd
import os
# Define functions
def clear():
    """Clear the console screen on windows"""
    sub.call('cls', shell=True)
def main():
    """Main function to convert all DBF files into CSV files"""
    # Declaration
    cnt_errors = 0
    # Get the script path, all DBF files inside this path will be converted into CSV.
    script_path = os.path.dirname('work_dir')
    # Clear the console screen
    clear()
    # Script is starting to find all DBF files.
    print('Script is searching for DBF files.')
    # Search for DBF files inside the script path.
    for dirpath, dirname, filenames in os.walk(script_path):
        for filename in filenames:
            if filename.endswith(".dbf"):
                print("Convert: {filename} to .csv".format(filename=filename))
                # Combine both strings
                full_path = dirpath + "\\" + filename
                # Try to load the DBF file
                try:
                    table = dbfread.DBF(full_path, encoding="gbk", ignore_missing_memofile=False)
                except dbfread.exceptions.DBFNotFound as dbf_exc:
                    print("Error occurred: \n{file} \n{error}".format(file=filename, error=dbf_exc))
                    cnt_errors += 1
                    continue
                # Load data from table into an DataFrame.
                df = pd.DataFrame(iter(table))
                # Remove last four characters.
                csv_file = filename[:-4] + ".csv"
                # Join the script path.
                output_path_csv = os.path.join(script_path, csv_file)
                # Print a message and create the csv file.
                print("Convert: {filename} to .csv".format(filename=filename))
                df.to_csv(output_path_csv, sep=';')
    # Print out amount of not converted DBF files.
    if cnt_errors > 0:
        print('Amount of not converted files: {}'.format(cnt_errors))
# Application entry point
if __name__ == '__main__':
    main()