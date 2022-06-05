
get_users_by_department_company = """
        SELECT u.id, u.firstname, u.lastname, u.email, u.Phone1, u.Phone2,
        u.zip_code, u.Address, u.City, u.state, d.name as department, c.name as company
        FROM users u
        inner join companies c
        ON c.id = u.company_id
        inner join departments d
        on d.id = u.department_id
        where u.company_id = {company} and u.department_id = {department}
        limit {limit};
        """