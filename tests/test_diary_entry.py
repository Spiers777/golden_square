from lib.diary_entry import *

def test_count_words():
    entry = DiaryEntry("blah", "test test test")
    assert entry.count_words() == 3

def test_reading_time():
    entry = DiaryEntry("blah", "test test test")
    assert entry.reading_time(3) == 1
    
def test_reading_chunk():
    entry = DiaryEntry("blah", "word1 word2 word3")
    chunk1 = entry.reading_chunk(1, 1)
    chunk2 = entry.reading_chunk(1, 1)
    assert chunk1 == "word1" and chunk2 == "word2"
