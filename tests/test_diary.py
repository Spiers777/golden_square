from lib.diary import *
from lib.diary_entry import *

def test_add_and_all():
    test_diary = Diary()
    test_diary.add(DiaryEntry("test1", "test1 content"))
    test_diary.add(DiaryEntry("test2", "test2 content"))
    assert [[x.title, x.contents] for x in test_diary.all()] == [[x.title, x.contents] for x in [DiaryEntry("test1", "test1 content"), DiaryEntry("test2", "test2 content")]]

def test_count_words():
    test_diary = Diary()
    test_diary.add(DiaryEntry("test1", "test1 content"))
    test_diary.add(DiaryEntry("test2", "test2 content"))
    assert test_diary.count_words() == 4

def test_reading_time():
    test_diary = Diary()
    test_diary.add(DiaryEntry("test1", "test1 content"))
    test_diary.add(DiaryEntry("test2", "test2 content"))
    assert test_diary.reading_time(4) == 1

def test_find_best_entry_for_reading_time():
    test_diary = Diary()
    correct_entry = DiaryEntry("test2", "1 2")
    test_diary.add(DiaryEntry("test1", "1"))
    test_diary.add(correct_entry)
    test_diary.add(DiaryEntry("test3", "1 2 3"))
    assert test_diary.find_best_entry_for_reading_time(2, 1) == correct_entry