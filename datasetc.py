import csv
with open('datasetc.csv', 'w') as csvfile:
    fieldnames = ['Unique_id', 'Kothamangalam','Mathirappilly','Karukadam','Puthuppady']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    places={"Kothamangalam","Mathirappilly","Karukadam","Puthuppady"}
    pp=30000
    for j in range(20,81,5):
                for k in range(j+15,j+31,5):
                    for l in range(20,31,5):
                        for m in range(30,41,5):
                            writer.writerow({'Unique_id': pp, 'Kothamangalam': j, 'Mathirappilly': k, 'Karukadam': l, 
                                 'Puthuppady': m})
                            pp+=1