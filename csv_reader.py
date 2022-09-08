import csv

def get_top_ranked_song(date):
    # open the csv file
    file = open('./csv/charts.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        # select the rows by the date
        if row[0] == date:
            rows.append(row)
    # close the csv file
    file.close()
    return rows