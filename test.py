from main import *
from csv_reader import CSVReader

def tailer():
   print("unit test passed!")
   print("-----------------")


def test_get_rank():
   assert get_rank(['2021-11-06',2,'Easy On Me','Adele',1,1,3]) == 2, "Should be 2" 
   assert type(get_rank(['2021-11-06',2,'Easy On Me','Adele',1,1,3])) is int, "Should be int"
   tailer()

def test_get_week_on_board():
   assert get_week_on_board(['2021-11-06',2,'Easy On Me','Adele',1,1,3]) == 3, "Should be 3"
   assert type(get_week_on_board(['2021-11-06',2,'Easy On Me','Adele',1,1,3])) is int, "Should be int"
   tailer()

def test_get_peak_rank_on_board():
   assert get_peak_rank_on_board(['2021-11-06',2,'Easy On Me','Adele',1,1,3]) == 1, "Should be 1"
   assert type(get_peak_rank_on_board(['2021-11-06',2,'Easy On Me','Adele',1,1,3])) is int, "Should be int"
   tailer()

def test_get_song_detail_by_date():
   csv_reader = CSVReader()
   songs_for_custom_date = csv_reader.get_song_detail_by_date('2021-11-06')
   assert songs_for_custom_date[0] == ['2021-11-06', '2', 'Easy On Me', 'Adele', '1', '1', '3'], "Should be ['2021-11-06', '2', 'Easy On Me', 'Adele', '1', '1', '3']"
   assert songs_for_custom_date[1][0] == '2021-11-06', "Should be '2021-11-06'"
   assert songs_for_custom_date[2][1] == '3', "Should be '3'"
   assert songs_for_custom_date[3][2] == 'Fancy Like', "Should be 'Fancy Like'"
   assert songs_for_custom_date[4][3] == 'Ed Sheeran', "Should be 'Ed Sheeran'"
   assert songs_for_custom_date[0][4] == '1', "Should be 1"
   assert songs_for_custom_date[0][5] == '1', "Should be 1"
   assert songs_for_custom_date[0][6] == '3', "Should be 3"

   assert type(songs_for_custom_date[0]) is list, "Should be list"
   assert type(songs_for_custom_date[1][0]) is str, "Should be str"
   assert type(songs_for_custom_date[2][1]) is str, "Should be str"
   assert type(songs_for_custom_date[3][2]) is str, "Should be str"
   assert type(songs_for_custom_date[4][3]) is str, "Should be str"
   assert type(songs_for_custom_date[0][4]) is str, "Should be str"
   assert type(songs_for_custom_date[0][5]) is str, "Should be str"
   assert type(songs_for_custom_date[0][6]) is str, "Should be str"
   tailer()

def test_get_song_detail_by_rank():
   csv_reader = CSVReader()
   songs_for_custom_rank = csv_reader.get_song_detail_by_rank('1')
   assert songs_for_custom_rank[0] == ['2021-11-06', '1', 'Stay', 'The Kid LAROI & Justin Bieber', '2', '1', '16'], "Should be ['2021-11-06', '1', 'Stay', 'The Kid LAROI & Justin Bieber', '2', '1', '16']"
   assert songs_for_custom_rank[1][0] == '2021-10-30', "Should be '2021-10-30'"
   assert songs_for_custom_rank[2][1] == '1', "Should be '1'"
   assert songs_for_custom_rank[3][2] == 'Stay', "Should be 'Stay'"
   assert songs_for_custom_rank[4][3] == 'Coldplay x BTS', "Should be 'Coldplay x BTS'"
   assert songs_for_custom_rank[5][4] == '1', "Should be '1'"
   assert songs_for_custom_rank[6][5] == '1', "Should be '1'"
   assert songs_for_custom_rank[7][6] == '1', "Should be '1'"

   assert type(songs_for_custom_rank[0]) is list ,"Should be list"
   assert type(songs_for_custom_rank[1][0]) is str ,"Should be str"
   assert type(songs_for_custom_rank[2][1]) is str ,"Should be str"
   assert type(songs_for_custom_rank[3][2]) is str ,"Should be str"
   assert type(songs_for_custom_rank[4][3]) is str, "Should be str"
   assert type(songs_for_custom_rank[5][4]) is str, "Should be str"
   assert type(songs_for_custom_rank[6][5]) is str, "Should be str"
   assert type(songs_for_custom_rank[7][6]) is str, "Should be str"
   tailer()

def test_get_all_songs():
   csv_reader =CSVReader()
   all_songs = csv_reader.get_all_songs()
   assert all_songs[0] == ['2021-11-06', '2', 'Easy On Me', 'Adele', '1', '1', '3'], "Should be ['2021-11-06', '2', 'Easy On Me', 'Adele', '1', '1', '3']"
   assert all_songs[1][0] == '2021-11-06', "Should be '2021-11-06'"
   assert all_songs[2][1] == '3', "Should be '3'"
   assert all_songs[3][2] == 'Fancy Like', "Should be 'Fancy Like'"
   assert all_songs[4][3] == 'Ed Sheeran', "Should be 'Ed Sheeran'"
   assert all_songs[5][4] == '6', "Should be '6'"
   assert all_songs[6][5] == '7', "Should be '7'"
   assert all_songs[7][6] == '24', "Should be '24'"

   assert type(all_songs[0]) is list,"Should be list"
   assert type(all_songs[1][0]) is str,"Should be str"
   assert type(all_songs[2][1]) is str,"Should be str"
   assert type(all_songs[3][2]) is str,"Should be str"
   assert type(all_songs[4][3]) is str,"Should be str"
   assert type(all_songs[5][4]) is str,"Should be str"
   assert type(all_songs[6][5]) is str,"Should be str"
   assert type(all_songs[7][6]) is str,"Should be str"
   tailer()


if __name__ == "__main__":
    test_get_rank()
    test_get_week_on_board()
    test_get_peak_rank_on_board()
    test_get_song_detail_by_date()
    test_get_song_detail_by_rank()
    test_get_all_songs()
    print("Everything passed!")