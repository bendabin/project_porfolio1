# This action imports the csv module
import csv
import os

#Generate the lists for the files  
tom_list= ["Top Gun", "Risky Business", "Minority Report"]
leo_list=  ["Titanic", "The Revenant", "Inception"]
den_list= ["Training Day", "Man on Fire", "Flight"]

movies_list= [tom_list, leo_list, den_list]

#Write row data to the csv file
with open("movies.csv", "w") as f:
    write = csv.writer(f, delimiter = ",")
    for movie in movies_list:
        write.writerow(movie)    
    
    """
    write.writerow(tom_list)
    write.writerow(leo_list)
    write.writerow(den_list)
    """




"""
with open ("movies.csv","w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(tom_list)


# Create the CSV file
with open("movies.csv","w", write= csv.writer(f, delminiter= ",")) as f:
    write.writerow(tom_list)
    write.writerow(leo_list)
    write.writerow(den_list)

"""



