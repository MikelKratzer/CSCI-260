import psycopg2 as pg
#import pprint

# All psycopg2 operations should be contained in this python file.
# Model in MVC data structure (goal is to strip view and controller from Courses)

class Course:
    def __init__(self, newId = 0, newNumber= ' '):
        self.id = newId
        self.number = newNumber
    def create(self, cursor, conn):
        query = "insert into courses (number) values ('%s')" %(self.number)
        cursor.execute(query)
        conn.commit()
    def retrieve(self, row):
        ID = 0
        NUMBER = 1
        self.id = row[ID]
        self.number = row[NUMBER]
    def update(self, cursor, conn, newId = None, newNumber = None):
        if (newId!= None):
            self.id = newId
        if (newNumber!= None):
            self.number = newNumber
        query = "update courses set number = '%s' where id = %s"%(self.number,self.id)
        cursor.execute(query)
        conn.commit()
    def delete(self, cursor, conn):
        query = "delete from courses where id = %s" %(self.id)
        cursor.execute(query)
        conn.commit()
    def describe(self):
        return "id=%s, number=%s"%(self.id, self.number)

# This is a python structure for a set of Course Objects.

class Courses:
    def __init__(self):
        conn_string = "host='localhost' dbname = 'csci260' user = 'csci260' password = 'password'"
        # print("Connecting to database\n ->%s" % (conn_string))
        self.conn = pg.connect(conn_string)
        self.cursor = self.conn.cursor()

    def create(self, c):
        c.create(self.cursor, self.conn)
    def delete(self, c):
        c.delete(self.cursor, self.conn)
    def update(self,c):
        c.update(self.cursor, self.conn)

    # def delete(self):
    #     id = input("Please enter the id to be deleted: ")
    #     query = "delete from courses where id = %s" %(id)
    #     self.cursor.execute(query)
    #     self.cursor.commit()

    # def update(self):
    #     id = input("Please enter the id to update: ")
    #     new_number = input("Updated course number: ")
    #     query = "update courses set number = %s where id = %s"%(new_number,id)
    #     self.cursor.execute(query)
    #     self.cursor.commit()

    # def create(self):
    #     id = input("Please enter the new id: ")
    #     number = input("Please input the new number for the course: ")
    #     query = "insert into courses (id,number) values (%s, '%s')" %(id, number)
    #     self.cursor.execute(query)
    #     self.cursor.commit()


    def retrieve(self):
        self.cursor.execute("select id,number from courses") # postgres queries
        records = self.cursor.fetchall() # gives list of tuples from query
        # print("|id | number |")
        # print("+---+--------+")
        ret = ""
        for i in records:
            c=Course()
            c.retrieve(i)
            ret += c.describe() + "\n"
            #print("| %s |%s|"%(i[ID],i[NUMBER])) # adds maintainability
        # print("+---+--------+")
        return ret

def main():
    conn_string = "host='localhost' dbname = 'csci260' user = 'csci260' password = 'password'"
    print("Connecting to database\n ->%s" % (conn_string))
    conn = pg.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")
    # create(cursor)
    # retrieve(cursor)
    choice = ''
    c = Courses(cursor)
    while choice.upper() != 'Q':
        print(" 1) Retrieve Current Courses \n 2) Add New Course \n 3) Update Course \n 4) Delete Course \n Q) Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            c.retrieve()
        elif choice == '2':
            c.create()
        elif choice == '3':
            c.update()
        elif choice == '4':
            c.delete()

if __name__ == "__main__":
    main()