import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)
mycursor = mydb.cursor()


class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        mycursor.execute("select max(salary) from emp group by(salary) order by salary desc limit 1;")
        result = mycursor.fetchone()
        return result

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        mycursor.execute("select min(salary) from emp group by(salary) order by salary asc limit 1;")
        data = mycursor.fetchone()
        return data

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
