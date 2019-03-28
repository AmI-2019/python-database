import pymysql

if __name__ == '__main__':
    # 1. prepare the SQL query
    sql = "select * from todo"

    # 2. create the connection
    connection = pymysql.connect(user="root", password="",
                                 host="localhost", database="todolist")

    # 3. get a cursor
    cursor = connection.cursor()

    # 4. execute the query
    cursor.execute(sql)

    # 5. fetch the results (and print them)
    result = cursor.fetchall()
    print(result)

    # 6. close the cursor
    cursor.close()

    # another SQL query, for inserting elements
    sql_insert = "insert into todo(description, urgent) values (%s, %s)"
    my_description = "go home"
    my_urgency = 1

    # get a new cursor
    cursor2 = connection.cursor()
    # execute the query
    cursor2.execute(sql_insert, (my_description, my_urgency))

    # commit changes
    connection.commit()

    # close the cursor
    cursor2.close()

    # 6a. finally, close the connection
    connection.close()
