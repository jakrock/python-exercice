import sqlite3
connexion=sqlite3.connect("jobs.db")


cursor =connexion.cursor()
query="select Major , Major_category from recent_grads where Major_category !='Engineering'"
cursor.execute(query)
result=cursor.fetchmany(5)
print(result)
connexion.close()
connexion2=sqlite3.connect('jobs2.db')
cursor1=connexion2.cursor()
query="select Major from recent_grads order by Major desc"
cursor1.execute(query)
result1=cursor1.fetchall()
print(result1[0:7])
connexion2.close()