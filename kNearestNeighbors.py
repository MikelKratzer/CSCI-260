import psycopg2 as pg
import matplotlib.pyplot as plt

conn_string = "host = 'localhost' dbname = 'csci260' password = 'password'"
conn = pg.connect(conn_string)
cursor = conn.cursor()

labels = ("total_bedrooms", "median_income", "median_house_value")
cursor.execute("select coalesce(%s,0) as x, coalesce(%s, 0) as y, coalesce(%s, 0) as z from normhousing limit 500;" %labels)
records = cursor.fetchall()
cols = {"x":0, "y":1, "z":2}

x = []
y = []
z = []
for r in records:
    x.append(r[cols['x']])
    y.append(r[cols['y']])
    z.append(r[cols['z']])

goodx = [0.15]
goody = [0.45]
goodz = [0.75] # directly from realtor/client
cursor.execute("select %s, %s, %s, sqrt((%s-%f)^2+(%s-%f)^2+(%s-%f)^2) as d from normhousing order by d limit 10;" 
               %(labels[0], labels[1], labels[2], labels[0], goodx[0], labels[1], goody[0], labels[2], goodz[0]))
closeRecords = cursor.fetchall()

close_x = []
close_y = []
close_z = []
for r in closeRecords:
    close_x.append(r[cols['x']])
    close_y.append(r[cols['y']])
    close_z.append(r[cols['z']])

xlimits = (min(x), max(x)) # or (0,1)
ylimits = (min(y), max(y))
zlimits = (min(z), max(z))


fig  = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(x,y,z, marker = 'o')
ax.scatter(goodx, goody, goodz, marker = '^')
ax.scatter(close_x, close_y, close_z, marker = '*', s = 30)
ax.set_xlabel(labels[0])
ax.set_ylabel(labels[1])
ax.set_zlabel(labels[2])

plt.show()