# DROP TABLES
users_table_drop = "DROP TABLE IF EXISTS Users"
departments_table_drop = "DROP TABLE IF EXISTS Departments"
companies_table_drop = "DROP TABLE IF EXISTS Companies"
staging_table_drop = "DROP TABLE IF EXISTS Staging"

# CREATE TABLES

staging_table_create = ("""
CREATE TABLE IF NOT EXISTS Staging(
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
CREATE TABLE IF NOT EXISTS Users(
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
CREATE TABLE IF NOT EXISTS Departments(
    id serial NOT NULL,
    name varchar,
    CONSTRAINT department_pkey PRIMARY KEY(id)
);
""")


companies_table_create = ("""
CREATE TABLE IF NOT EXISTS Companies(
    id serial NOT NULL, 
    name integer,
    CONSTRAINT company_pkey PRIMARY KEY(id)
);
""")

constraints = ("""

ALTER TABLE Users
  ADD CONSTRAINT users_department_id_fkey
    FOREIGN KEY (department_id) REFERENCES Departments (id);

ALTER TABLE Users
  ADD CONSTRAINT users_company_id_fkey
    FOREIGN KEY (company_id) REFERENCES Companies (id);

""")

## FILL  TABLES FROM STAGING

users_fill_from_staging = ("""
insert into Users (firstname, lastname, email, Phone1, Phone2, zip_code, Address, City, state, department_id, company_id)
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
from staging_eats s
INNER JOIN Companies c
ON s.company_name = c.name
INNER JOIN Departments d
ON s.company_name = d.name;
""")

companies_fill_from_staging = ("""
    insert into Companies (NAME)
    select distinct company_name as Name
    from Staging;
""")

departments_fill_from_staging = ("""
    insert into Departments (NAME)
    select distinct department as Name
    from Staging;
""")


fill_table_queries = [companies_fill_from_staging,departments_fill_from_staging,users_fill_from_staging]
create_table_queries = [staging_table_create, users_table_create, departments_table_create, companies_table_create]
drop_table_queries = [users_table_drop, departments_table_drop, companies_table_drop, staging_table_drop]