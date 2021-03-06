#!python

from __future__ import division, print_function
from operator import itemgetter


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            # TODO: increment item count
            if item in self:
                self.tokens += 1
                self[item] += 1
            else:
                self.tokens += 1
                self.types += 1
                self[item] = 1
            pass

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        # TODO: retrieve item count
        if item in self:
            return self[item]
        else:
            return 0

        pass


class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        new_word_list = []

        for item in iterable:
            # if item in new_word_list:
            #     self.tokens += 1
            #     word_index = new_word_list.index(item)
            #     new_word_list[word_index + 1] += 1
            # else:
            #     self.tokens += 1
            #     self.types += 1
            #     new_word_list.append(item)
            #     new_word_list.append(1)

            # for x in range(0, len(new_word_list), 2):
            #     self.append(tuple([new_word_list[x], new_word_list[x+1]]))
            if self.__contains__(item):
                self.tokens += 1
                word_index = self._index(item)
                current_item = self.pop(word_index)
                current_count = current_item[1] + 1
                self.insert(word_index, (item, current_count))
                print("index: " + str(word_index))
                print("current item: " + str(current_item))
            else:
                self.tokens += 1
                self.types += 1
                self.append((item, 1))

        print(self)

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        # TODO: retrieve item count
        if any(item in code for code in self):
            word_index = self._index(item)
            current_item = self[word_index]
            current_count = current_item[1]
            return current_count

        return 0

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        # TODO: check if item is in histogram
        if any(item in code for code in self):
            return True

        return False

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        # TODO: implement linear search to find an item's index
        indices = next((i for i, v in enumerate(self) if v[0] == target), -1)
        return indices


def test_histogram(text_list):
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    # print(hist_dict.types)
    # print('dictogram:', hist_dict)

    hist_list = Listogram(text_list)
    print(hist_list.tokens)
    print('listogram:', hist_list)
    print(hist_list.__contains__('fish'))
    print(hist_list._index('blue'))
    print(hist_list.count('fish'))


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
