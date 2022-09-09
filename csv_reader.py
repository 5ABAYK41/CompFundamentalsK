import csv

def get_song_detail_by_date(date):
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

def get_song_detail_by_rank(rank):
    file = open('./csv/charts.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        # select the rows by the rank
        if row[1] == rank:
            rows.append(row)
    file.close()
    return rows

def get_all_songs():
    file = open('./csv/charts.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    return rows