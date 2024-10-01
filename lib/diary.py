class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.

        total = 0
        for entry in self.all():
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        return len((" ".join([x.contents for x in self.entries])).split(" ")) / wpm

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        # valid_entries = [x for x in self.all() if len(x.contents.split(" ")) <= wpm * minutes]
        valid_entries = filter(lambda x: len(x.contents.split(" ")) <= wpm * minutes, self.all())
        return sorted(valid_entries, key=lambda x: x.contents.split(" "))[-1]
