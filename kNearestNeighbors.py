import psycopg2 as pg
import matplotlib.pyplot as plt


def KNN(v1,v2,v3,f1,f2,f3,K,P,S):
    v1=float(v1)
    v2=float(v2)
    v3=float(v3)
    K=float(K)
    P=float(P)
    S=float(S)
    conn_string = "host = 'localhost' dbname = 'csci260' password = 'password'"
    conn = pg.connect(conn_string)
    cursor = conn.cursor()

    labels = (f1,f2,f3,P,S)
    cursor.execute("select coalesce(%s,0) as x, coalesce(%s, 0) as y, coalesce(%s, 0) as z from normhousing tablesample system (%f) repeatable(%f);" %labels)
    records = cursor.fetchall()
    cols = {"x":0, "y":1, "z":2}

    x = []
    y = []
    z = []
    for r in records:
        x.append(r[cols['x']])
        y.append(r[cols['y']])
        z.append(r[cols['z']])

    goodx = [v1]
    goody = [v2]
    goodz = [v3] # directly from realtor/client
    cursor.execute("select %s, %s, %s, sqrt((%s-%f)^2+(%s-%f)^2+(%s-%f)^2) as d from normhousing order by d limit %f;" 
                %(labels[0], labels[1], labels[2], labels[0], goodx[0], labels[1], goody[0], labels[2], goodz[0], K))
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
    ax.scatter(close_x, close_y, close_z, marker = '*', s = 100)
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])

    plt.show()


if __name__ == "__main__":
	KNN(0.45,0.15,0.45, \
        "total_bedrooms","median_income","median_house_value", \
        10,10,11301)