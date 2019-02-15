import numpy as np
import pandas as pd
import sqlite3
 

class DataHandler(object):
    """ 
    """

    def __init__(self):
        """ 
        """
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()

        self.inverse_pair = {'AUDUSD': 'USDAUD',
                             'EURUSD': 'USDEUR',
                             'GBPUSD': 'USDGBP',
                             'NZDUSD': 'USDNZD',
                             'USDCAD': 'CADUSD',
                             'USDCHF': 'CHFUSD',
                             'USDJPY': 'JPYUSD',
                             'USDNOK': 'NOKUSD',
                             'USDSEK': 'SEKUSD'}

    def get_pair_for_holding_period(self, pair, holding_period, freq):
        """ 
        This function retrieves from the database information
        - For a given currency pair 
        - For a given holding period (Spot and Forward)

        TODO: Some error check would be handy
        """


        # Getting all information fo a given pair
        query = """SELECT 
                   "Date" AS "Date", 
                   "Spot" AS "Spot", 
                   "{time_specifier}" AS "Forward" 
                   FROM {pair};""".format(time_specifier=holding_period, pair=pair)

        # Get the data into a DataFrame
        df = pd.read_sql_query(query, self.conn)


        # Setting the correctly parsed date as Index
        df['Date'] =  pd.to_datetime(df['Date'], format='%d-%b-%Y')
        df = df.set_index('Date')

        # Dropping not trading days (They have Nan values)
        df = df.dropna()

        # If the end of the month is not a trading day padding with last trading day
        #frequency = holding_period[-1]

        # Convert sampling frequency to Pandas convention
        # TODO: This should be a class constant
        frequency = {'1W' : '1W',
                       '2W' : '2W',
                       '1M' : '1M',
                       '2M' : '2M',
                       '3M' : '3M',
                       '6M' : '6M',
                       '1Y' : '1A',
                       '2Y' : '2A',
                       '3Y' : '3A',
                       '4Y' : '4A',
                       '5Y' : '5A',
                       '6Y' : '6A',
                       '7Y' : '7A',
                       '8Y' : '8A',
                       '9Y' : '9A',
                       '10Y': '10A'}
 
        # Resample
        # df = df.asfreq(freq=frequency[holding_period], method='pad')

        # Resample (according to the article a decision is made every month!)
        #df = df.asfreq(freq='M', method='pad')
        df = df.asfreq(freq=freq, method='pad')

        return df


    def get_pair_raw(self, pair):
        """ 
        """

        # Getting all information fo a given pair
        query = """SELECT 
                   "Date" AS "Date", 
                   "Spot" AS "Spot" 
                   FROM {pair};""".format(pair=pair)

        # Get the data into a DataFrame
        df = pd.read_sql_query(query, self.conn)


        # Setting the correctly parsed date as Index
        df['Date'] =  pd.to_datetime(df['Date'], format='%d-%b-%Y')
        df = df.set_index('Date')

        return df
 

    def push_csv(self, csv_path, pair_name):
        """ Importing a CSV file into the DataBase
        It expects the FULL Path of the CSV file
        In the exporter I used TAB as separator so it uses TAB as separator as well
        """
        df = pd.read_csv(csv_path + pair_name, sep='\t')
        df.to_sql(pair_name, self.conn, if_exists='replace')

    def invert_and_push_csv(self, csv_path, pair_name):
        """ The purpose og this function is to invert the currency pair related data

        Calculates the reciprocal of spot and forward data
        Exchanges the names of base and quote currenty columns (R to Q anc vica versa)
        Gets the inverse curreny par name and pushes the data into the database

        TODO: This function is ugly
              The mapping should be done better
        """
        df = pd.read_csv(csv_path + pair_name, sep='\t')

        # Reciprocal of the spot price
        df['Spot'] = np.reciprocal(df['Spot'])

        # Reciprocal of all forward prices
        df['1W'] = np.reciprocal(df['1W'])
        df['2W'] = np.reciprocal(df['2W'])
        df['1M'] = np.reciprocal(df['1M'])
        df['2M'] = np.reciprocal(df['2M'])
        df['3M'] = np.reciprocal(df['3M'])
        df['6M'] = np.reciprocal(df['6M'])
        df['1Y'] = np.reciprocal(df['1Y'])
        df['2Y'] = np.reciprocal(df['2Y'])
        df['3Y'] = np.reciprocal(df['3Y'])
        df['4Y'] = np.reciprocal(df['4Y'])
        df['5Y'] = np.reciprocal(df['5Y'])
        df['6Y'] = np.reciprocal(df['6Y'])
        df['7Y'] = np.reciprocal(df['7Y'])
        df['8Y'] = np.reciprocal(df['8Y'])
        df['9Y'] = np.reciprocal(df['9Y'])
        df['10Y'] = np.reciprocal(df['10Y'])
        
        # Renaming columns
        df = df.rename(columns={'R1W' : 'Q1W' ,
                                'R2W' : 'Q2W' ,
                                'R1M' : 'Q1M' ,
                                'R2M' : 'Q2M' ,
                                'R3M' : 'Q3M' ,
                                'R6M' : 'Q6M' ,
                                'R1Y' : 'Q1Y' ,
                                'R2Y' : 'Q2Y' ,
                                'R3Y' : 'Q3Y' ,
                                'R4Y' : 'Q4Y' ,
                                'R5Y' : 'Q5Y' ,
                                'R6Y' : 'Q6Y' ,
                                'R7Y' : 'Q7Y' ,
                                'R8Y' : 'Q8Y' ,
                                'R9Y' : 'Q9Y' ,
                                'R10Y': 'Q10Y',
                                'Q1W' : 'R1W' ,
                                'Q2W' : 'R2W' ,
                                'Q1M' : 'R1M' ,
                                'Q2M' : 'R2M' ,
                                'Q3M' : 'R3M' ,
                                'Q6M' : 'R6M' ,
                                'Q1Y' : 'R1Y' ,
                                'Q2Y' : 'R2Y' ,
                                'Q3Y' : 'R3Y' ,
                                'Q4Y' : 'R4Y' ,
                                'Q5Y' : 'R5Y' ,
                                'Q6Y' : 'R6Y' ,
                                'Q7Y' : 'R7Y' ,
                                'Q8Y' : 'R8Y' ,
                                'Q9Y' : 'R9Y' ,
                                'Q10Y': 'R10Y'})
        
        # Pushing to the DataBase
        df.to_sql(self.inverse_pair[pair_name], self.conn, if_exists='replace')

    def get_pairs(self):
        """ Prints some information on the DB
        Mostly used for verification purposes
        """
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table';")

        res = []
        for i in self.c.fetchall():
            res.append(i[0])

        return res


    def get_column_names(self, table_name):
        """ Getting the column names
        """
        result = self.conn.execute("SELECT * FROM {table}".format(table=table_name))
        names = list(map(lambda x: x[0], result.description))
        
        return names

    def commit(self):
        """ Just a lyer on the SQLite commit method
        """
        self.conn.commit()

    def close(self):
       """Safely close the connection
       """
       self.conn.commit()
       self.conn.close()

