# DROP TABLES
users_table_drop = "DROP TABLE IF EXISTS users"
departments_table_drop = "DROP TABLE IF EXISTS departments"
companies_table_drop = "DROP TABLE IF EXISTS companies"
staging_table_drop = "DROP TABLE IF EXISTS staging"

# CREATE TABLES

staging_table_create = ("""
CREATE TABLE IF NOT EXISTS staging(
        id serial PRIMARY KEY NOT NULL,
        first_name varchar,
        last_name varchar,
        company_name varchar,
        address varchar,
        city varchar,
        state varchar,
        zip varchar,
        phone1 varchar,
        phone2 varchar,
        email varchar,
        department varchar
);
""")

users_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
        id serial NOT NULL,
        firstname varchar,
        lastname varchar,
        email varchar,
        Phone1 varchar,
        Phone2 varchar,
        zip_code varchar,
        Address varchar,
        City varchar,
        state varchar,
        department_id integer NOT NULL,
        company_id integer NOT NULL,
        CONSTRAINT users_pkey PRIMARY KEY(id)
);
""")


departments_table_create = ("""
CREATE TABLE IF NOT EXISTS departments(
    id serial NOT NULL,
    name varchar,
    CONSTRAINT department_pkey PRIMARY KEY(id)
);
""")


companies_table_create = ("""
CREATE TABLE IF NOT EXISTS companies(
    id serial NOT NULL, 
    name varchar,
    CONSTRAINT company_pkey PRIMARY KEY(id)
);
""")

constraints = ("""

ALTER TABLE users
  ADD CONSTRAINT users_department_id_fkey
    FOREIGN KEY (department_id) REFERENCES departments (id);

ALTER TABLE users
  ADD CONSTRAINT users_company_id_fkey
    FOREIGN KEY (company_id) REFERENCES companies (id);

""")

## FILL  TABLES FROM STAGING

users_fill_from_staging = ("""
insert into users (firstname, lastname, email, Phone1, Phone2, zip_code, Address, City, state, department_id, company_id)
select 
    s.first_name as firstname,
    s.last_name as lastname,
    s.email as email, 
    s.phone1 as Phone1, 
    s.phone2 as Phone2, 
    s.zip as zip_code, 
    s.address as Address, 
    s.city as City, 
    s.state as state, 
    d.id as department_id, 
    c.id as company_id
from staging s
INNER JOIN companies c
ON s.company_name = c.name
INNER JOIN departments d
ON s.department = d.name;
""")

companies_fill_from_staging = ("""
    insert into companies (name)
    select distinct company_name as Name
    from staging;
""")

departments_fill_from_staging = ("""
    insert into departments (NAME)
    select distinct department as Name
    from staging;
""")


fill_table_queries = [companies_fill_from_staging,departments_fill_from_staging,users_fill_from_staging]
create_table_queries = [staging_table_create, users_table_create, departments_table_create, companies_table_create]
drop_table_queries = [users_table_drop, departments_table_drop, companies_table_drop, staging_table_drop]
create_constraints = [constraints]