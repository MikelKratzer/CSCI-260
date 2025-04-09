import psycopg2 as pg
#import pprint
class Courses:
    def __init__(self, _cursor):
        self.cursor = _cursor

    def delete(self):
        id = input("Please enter the id to be deleted: ")
        query = "delete from courses where id = %s" %(id)
        self.cursor.execute(query)
        self.cursor.commit()

    def update(self):
        id = input("Please enter the id to update: ")
        new_number = input("Updated course number: ")
        query = "update courses set number = '%s' where id = %s"%(new_number,id)
        self.cursor.execute(query)
        self.cursor.commit()

    def create(self):
        id = input("Please enter the new id: ")
        number = input("Please input the new number for the course: ")
        query = "insert into courses (id,number) values (%s, '%s')" %(id, number)
        self.cursor.execute(query)
        self.cursor.commit()


    def retrieve(self):
        self.cursor.execute("select id,number from courses") # postgres queries
        records = self.cursor.fetchall() # gives list of tuples from query
        ID = 0
        NUMBER = 1
        print("|id | number |")
        print("+---+--------+")
        for i in records:
            print("| %s |%s|"%(i[ID],i[NUMBER])) # adds maintainability
        print("+---+--------+")

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