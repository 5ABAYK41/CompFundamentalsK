import csv

class CSVReader():
    def __init__(self):
        super().__init__()

    def __read_csv_file(self):
        self.file = open('./csv/charts.csv')
        csvreader = csv.reader(self.file)
        return csvreader
    
    def __close_csv_file(self):
        self.file.close()

    def get_song_detail_by_date(self,date):
        # open the csv file
        csvreader = self.__read_csv_file()
        rows = []
        for row in csvreader:
            # select the rows by the date
            if row[0] == date:
                rows.append(row)
        # close the csv file
        self.__close_csv_file()
        return rows

    def get_song_detail_by_rank(self,rank):
        csvreader = self.__read_csv_file()
        rows = []
        for row in csvreader:
            # select the rows by the rank
            if row[1] == rank:
                rows.append(row)
        self.__close_csv_file()
        return rows

    def get_all_songs(self):
        csvreader = self.__read_csv_file()
        rows = []
        for row in csvreader:
            rows.append(row)
        self.__close_csv_file()
        # not returning label
        return rows[1:]