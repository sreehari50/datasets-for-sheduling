import csv
with open('datasetsa.csv', 'w') as csvfile:
    fieldnames = ['Unique_id','Arakuzha','Perumballoor']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    places={"Arakuzha","Perumballoor"}
    pp=10000
    for j in range(10,76,1):
        for k in range(j+5,j+16,2):
            writer.writerow({'Unique_id':pp,'Arakuzha':j,'Perumballoor':k})
            pp+=1