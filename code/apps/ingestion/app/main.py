import pandas as pd
import db_engine as dbe
import configparser
import os


class Pipeline:

    def __init__(self, params):
        pass

    def run(self):
        tables = ['Staging', 'Users', 'Companies', 'Departments']
        cur, conn = dbe.create_connection(params)
        dbe.drop_tables(cur, conn)
        dbe.create_tables(cur, conn)
        dbe.fill_from_staging_all(cur, conn)
        dbe.drop_table(cur, conn, tables[0])        
        count_tables = dbe.check_data(cur, conn, tables)
        for k, v in count_tables.items():
            print("Table {0} has {1} records".format(k, v))


if __name__ == '__main__':

    params = {"host": "", "database": "", "user": "", "password": "", "port": ""}

    config = configparser.ConfigParser()
    config.read_file(open(os.getcwd() + '/app/config/config.cfg'))
    pg_config = dict(config.items('POSTGRESQL'))

    for k, v in pg_config.items():
        params[k] = v

    pipeline = Pipeline(params)    
    pipeline.run()