






cursor.execute("select coalesce(total_bedrooms,0) as x, coalesce(median_income, 0) as y, coalesce(median_house_value, 0) as z from normhousing")


x = []
y = []
z = []
for r in records:
    x.append(r[0])
    y.append(r[0])
    z.append(r[2])