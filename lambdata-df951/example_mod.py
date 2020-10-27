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

# Any required variables for use here


# DS functions here
def total_nul(df):
    """
    Get the total amount of Null and NaN values
    """
    nul = (df.isnull().sum()).sum()
    na = (df.isnull().sum()).sum()
    print(f'Nan Count = {na}\nNull Count = {nul}')


def rand_df(df):
    """
    Shuffle--not just a dance move--a data frame
    """
    out = df.sample(frac=1).reset_index(drop=True)
    return out


def md_copy(df):
    """
    Send the markdown version of data frame to
    the clipboard.
    Supports: Windows and Mac only
    """
    user_os = platform.system()
    df_md = df.to_markdown()
    if user_os == "Darwin":
        subprocess.run("pbcopy",
                        universal_newlines=True,
                        input=df_md)
        print("✅Successful, paste responsibly!")
    elif user_os == "Linux":
        print(f'{user_os} currently not supported 😭')
    elif user_os == "Windows":
        subprocess.run(['clip.exe'],
                        input=df_md,
                        check=True)
        print("✅Successful, paste responsibly!")
    else:
        print(f"{user_os}🧐. . . never seen that before!")
