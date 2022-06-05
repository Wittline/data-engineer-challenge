import pandas as pd
import db_engine as dbe
import configparser
import os


class Pipeline:

    def __init__(self, params, staging_file):
        self.params = params
        self.staging_file = staging_file

    def run(self):
        tables = ['users', 'companies', 'departments']
        columns_staging = ['first_name','last_name','company_name','address','city','state','zip','phone1','phone2','email','department']
        cur, conn = dbe.create_connection(self.params)
        dbe.drop_tables(cur, conn)
        dbe.create_tables(cur, conn)
        dbe.set_staging(cur, conn, self.staging_file, columns_staging)
        dbe.fill_from_staging_all(cur, conn)
        dbe.drop_table(cur, conn, 'staging')
        dbe.set_constraints(cur, conn)
        count_tables = dbe.check_data(cur, conn, tables)
        for k, v in count_tables.items():
            print("Table {0} has {1} records".format(k, v))
        dbe.close_connection(cur, conn)


if __name__ == '__main__':

    params = {"host": "", "database": "", "user": "", "password": ""}

    config = configparser.ConfigParser()
    config.read_file(open(os.getcwd() + '/app/config/config.cfg'))
    pg_config = dict(config.items('POSTGRESQL'))        
    staging_file = config.get('STAGINGFILE','location')    

    for k, v in pg_config.items():
        params[k] = v
    
    print(params)

    pipeline = Pipeline(params, staging_file)
    pipeline.run()