import numpy as np
import pandas as pd
# import sqlite3


class DataHandler(object):
    """
    This Class handles the hystorical yield curve data
    for the whole project

    TODO: Use Google BigQuery to store data instead of
    always importing forom excel or csv
    """

    def __init__(self):
        """
        """
        # self.conn = sqlite3.connect(db_file)
        # self.c = self.conn.cursor()
        self.df = pd.DataFrame()

    def import_xls(self, file_path):

        tmp = pd.read_excel(file_path)
        # Original columns
        # ['Dátum/Date', 'Nap/Day', 'Év/Year', 'Hozam (%)/Yield (%)']

        tmp.columns = ['Date', 'Day', 'Year', 'Yield']

        if self.df.empty:
            self.df = tmp
        else:
            self.df = self.df.append(tmp, ignore_index=True)

    def stats(self):
        """
        This function is for giving a simple descriptive
        stgatistics on the DataFrame of yield curves
        """
        print(self.df.shape)
        print(self.df.isnull().sum(axis=0))

    def to_csv(self, file_path):
        """
        Prints the actual internal dataframe to csv
        """
        self.df.to_csv(file_path)
        
    def push_csv(self, csv_path, pair_name):
        """
        Importing a CSV file into the DataBase
        """
        # df = pd.read_csv(csv_path + pair_name, sep='\t')
        # df.to_sql(pair_name, self.conn, if_exists='replace')
        pass

    def commit(self):
        """ Just a lyer on the SQLite commit method
        """
        # self.conn.commit()
        pass

    def close(self):
        """Safely close the connection
        """
        # self.conn.commit()
        # self.conn.close()
        pass
