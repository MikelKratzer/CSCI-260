import psycopg2 as pg
import matplotlib.pyplot as plt

conn_string = "host = 'localhost' dbname='csci260' user = 'csci260' password='password'"
conn = pg.connect(conn_string)
cursor = conn.cursor()

def ourPlot(ax, field1, field2, cursor):
        print("Processing " + field1 + " and " + field2)
        cursor.execute("select coalesce(%s, 0),coalesce(%s, 0) from housing" %(field1, field2)) # coalesce returns first not null argument
        records = cursor.fetchall()
        # print(records)
        # mins = min(records)
        # maxs = max(records)

        x = []
        y = []
        for r in records:
            x.append(r[0])
            y.append(r[1])

        #xlimits = (mins[0], maxs[0])
        #ylimits = (mins[1], maxs[1])
        ax.scatter(x,y, s = 2, color = 'green') # s is point thickness
        # ax.set_xlabel("income")
        # ax.set_ylabel("value")
        #ax.set(xlim=xlimits,ylim=ylimits)

def reportAverage(ax,field1, field2, cursor, where):
    ax.set_axis_off()
    cursor.execute("""select 
        avg(coalesce(%s, 0)) as average_field1,
        stddev(coalesce(%s,0)) as stddev_field1,
        avg(coalesce(%s, 0)) as average_field2,
        stddev(coalesce(%s,0)) as stddev_field2,
        corr(coalesce(%s,0), coalesce(%s,0)) as r
        from housing %s""" %(field1, field1, field2, field2, field1, field2, where))
    records = cursor.fetchall()
    af1 = f'{records[0][0]:.3f}'
    sf1 = f'{records[0][1]:.3f}'
    af2 = f'{records[0][2]:.3f}'
    sf2 = f'{records[0][3]:.3f}'
    r = f'{records[0][4]:.3f}'
    ax.text(0.0, 0.8, "correlation_coeff = %s"%(r), fontsize=8)
    ax.text(0.0, 0.6, "average_field1 = %s"%(af1), fontsize=8)
    ax.text(0.0, 0.4, "stddev_field1 = %s"%(sf1), fontsize=8)
    ax.text(0.0, 0.2, "average_field2 = %s"%(af2), fontsize=8)
    ax.text(0.0, 0.0, "stddev_field2 = %s"%(sf2), fontsize=8)

fields = ["longitude",
    "latitude",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "median_income", 
    "median_house_value"]

fig,ax = plt.subplots(nrows = len(fields), ncols = len(fields))
# plt.subplots_adjust(wspace=1, hspace=1)

where = "where ocean_proximity = 'NEAR BAY' or ocean_proximity = '<1H OCEAN'"
for index1 in range(0,len(fields)):
    for index2 in range(0,len(fields)):
        if index1 > index2:
            ourPlot(ax[index1, index2], fields[index1], fields[index2], cursor)
        elif index1 == index2:
            ax[index1, index2].set_axis_off()
            ax[index1, index2].text(0,0.5, fields[index1],fontsize=8)
        else:
             reportAverage(ax[index1, index2],fields[index1], fields[index2], cursor, where)
        

plt.show()