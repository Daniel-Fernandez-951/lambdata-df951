"""
Lambda School Assignment 1:
Early version of Data Cleaning functions
"""

# Libraries used in this module through pipenv
import numpy as np
import pandas as pd
import subprocess
import platform
import tabulate
import os
import datetime


# Any required variables for use here


# DS functions here
class DfTools:
    def __init__(self, df):
        self.df = df

    def total_nul(self, df):
        """
        Get the total amount of Null and NaN values
        """
        nul = (df.isnull().sum()).sum()
        na = (df.isnull().sum()).sum()
        return f'Nan Count = {na}\nNull Count = {nul}'

    def rand_df(self, df):
        """
        Shuffle--not just a dance move--a data frame
        """
        out = df.sample(frac=1).reset_index(drop=True)
        return out

    def md_copy(self, df):
        """
        Send the markdown version of data frame to
        the clipboard.
        Supports: Windows and Mac only
        """
        user_os = platform.system()
        df_md = pd.to_markdown(df)
        # return df_md
        if user_os == "Darwin":
            subprocess.run("pbcopy",
                           universal_newlines=True,
                           input=df_md)
            return " ✅ Successful, paste responsibly!"
        elif user_os == "Linux":
            return f'{user_os} currently not supported 😭'
        elif user_os == "Windows":
            subprocess.run(['clip.exe'],
                           input=df_md,
                           check=True)
            return " ✅ Successful, paste responsibly!"
        else:
            return f"{user_os}🧐. . . never seen that before!"

    @staticmethod
    def stamp_submission(submission, folder='/submission/', fileName='submission'):
        """
        In current directory, make @param folder and write to a file named
        @param submission with a time-stamp.
        @param submission: <dataframe to write>
        @param folder: '/submission/'
        @param fileName: 'submission'
        """
        path = os.getcwd()
        dtime = str(datetime.datetime.now().timestamp()).replace('.', '')
        full_path = path + folder

        try:
            f = open(f"{full_path}{fileName}_{dtime}", "w")
            f.write(submission)
            f.close()
        except FileExistsError:
            f = open(f"{full_path}{fileName}_{dtime}", "w")
            f.write(submission)
            f.close()
