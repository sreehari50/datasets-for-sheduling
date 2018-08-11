import csv
with open('datasetsb.csv', 'w') as csvfile:
    fieldnames = ['Unique_id', 'Vazhakulam','Avoly','Anicadu','Kizhakkekara']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    places={"Vazhakulam","Avoly","Anicadu","Kizhakkekara"}
    pp=20000
    for j in range(10,31,5):
                for k in range(j+10,j+41,5):
                    for l in range(40,56,5):
                        for m in range(35,56,5):
                            writer.writerow({'Unique_id': pp, 'Vazhakulam': j, 'Avoly': k, 'Anicadu': l, 'Kizhakkekara': m}) 
                            pp+=1