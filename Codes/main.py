from Modules.Connection import Connection
import mysql.connector as connector
from datetime import date


def createAccount(email, password):
    accountID = 0

    sql = f'''
    INSERT INTO accounts (email, password) VALUES ('{email}', '{password}')
    '''

    connection = Connection()
    cursor = connection.mysqlConnection.cursor()

    try:
        cursor.execute(sql)
        accountID = cursor.lastrowid
        cursor.close()
        connection.commit()
        print('Account created.')
    except connector.Error as e:
        print(e)

    connection.closeConnection()
    return accountID


def createStudent(studentID, firstName, middleName, lastName, birthDate, accountID):

    sql = f'''
    INSERT INTO students (student_id, first_name, middle_name, last_name, birth_date, account_id)
    VALUES ({studentID}, '{firstName}', '{middleName}', '{lastName}', '{birthDate}', {accountID})
    '''

    connection = Connection()
    cursor = connection.mysqlConnection.cursor()

    try:
        cursor.execute(sql)
        cursor.close()
        connection.commit()
        print('Student Created')
    except connector.Error as e:
        print(e)

    connection.closeConnection()

def getProfile(studentID):

    sql = f'''
        SELECT s.student_id, s.first_name, s.middle_name, s.last_name, s.birth_date, a.email
        FROM students s join accounts a ON s.account_id = a.id
        WHERE student_id = {studentID} AND a.archived = False
        '''

    connection = Connection()
    cursor = connection.mysqlConnection.cursor()

    try:
        cursor.execute(sql)

        for (student_id, first_name, middle_name, last_name, birth_date, email) in cursor:
            print(f'''
            Student ID: {student_id}
            Name      : {first_name} {middle_name[0]}. {last_name}
            Email     : {email}
            Birthdate : {birth_date}
            ''')

        cursor.close()
    except connector.Error as e:
        print(e)

    connection.closeConnection()


def archiveAccount(studentID):

    sql = f'''
        UPDATE accounts a JOIN students s on a.id = s.account_id SET archived = True
        WHERE s.student_id = {studentID}
        '''

    connection = Connection()
    cursor = connection.mysqlConnection.cursor()

    try:
        cursor.execute(sql)
        cursor.close()
        connection.commit()
        print('Account archived successfully')
    except connector.Error as e:
        print(e)

    connection.closeConnection()


# implement this method
def login(email, password):
    pass


# implement this method
def updateAccount():
    pass


# account_id = createAccount('mark@gmail.com', 'password13')
# createStudent(20190001, 'Mark', 'Diaz', 'Margallo', date(2000, 12, 25), account_id)

getProfile(20190001)








