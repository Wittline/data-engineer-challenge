from typing import Optional
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import pandas as pd
import psycopg2
import db_engine as dbe
import os
from pydantic import BaseModel
import configparser
from sql_queries import get_users_by_department_company

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "This is my database api"}

class SearchUser(BaseModel):
    department: int
    company: int
    limit: int


@app.post("/read")

async def read(item: SearchUser):
    try:

        item = item.dict()

        params = {"host": "", "database": "", "user": "", "password": ""}

        config = configparser.ConfigParser()
        config.read_file(open(os.getcwd() + '/app/config/config.cfg'))
        pg_config = dict(config.items('POSTGRESQL'))
        
        for k, v in pg_config.items():
            params[k] = v     

        cur, conn = await dbe.create_connection(params)

        query = get_users_by_department_company.format(**item)
        
        cur.execute(query) 
        results = cur.fetchall()
        dbe.close_connection(cur, conn)
        return results

    except (Exception, psycopg2.Error) as error:
        msg = "Error while fetching data from PostgreSQL: {}".format(error)
        dbe.close_connection(cur, conn)
        return {'error':True, 
                'message': msg}        

if __name__== '__main__':
    uvicorn.run(app, port = 8080, host= "0.0.0.0")