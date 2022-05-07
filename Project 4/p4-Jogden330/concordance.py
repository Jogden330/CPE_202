from hash_quad import *
import string

# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.next = None

# class Value:
#
#     def __init__(self):
#
#         self.front = None
#         self.back = None
#         # self.num_items = 0
#
#     def add(self, value):
#         new_value = Node(value)
#         if self.front == None:
#             self.front = new_value
#             self.back = new_value
#         else:
#             self.back.next = new_value
#             self.back = new_value
#         # self.num_items += 1
#
#     def check_last_value(self, value):
#         if self.back.data == value:
#             return True
#         else:
#             return False
#
#     def value_string(self):
#         string = ""
#         cur_node = self.front
#         while(cur_node != None):
#             string = string + " " + str(cur_node.data)
#             cur_node = cur_node.next
#         return string
#
#         # val_list = [None] * (self.num_items)
#         # cur_node = self.front
#         # for index in range(self.num_items):
#         #     val_list[index] = cur_node.data
#         #     cur_node = cur_node.next
#         # return ' '.join([str(val) for val in val_list])

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    # """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
    #         Starting size of hash table should be 191: self.stop_table = HashTable(191)
    #         If file does not exist, raise FileNotFoundError"""

    def load_stop_table(self, filename):
        self.stop_table = HashTable(191)
        with open(filename, "r") as file:  # opens the file as readable
            for line in file:
                line = line.rstrip()
                self.stop_table.insert(line.lower())

    #     """ Read words from input text file (filename) and insert them into the concordance hash table,
    #         after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
    #         (The stop words hash table could possibly be None.)
    #         Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
    #         Starting size of hash table should be 191: self.concordance_table = HashTable(191)
    #         If file does not exist, raise FileNotFoundError"""
    def load_concordance_table(self, filename):
        line_count = 0
        self.concordance_table = HashTable(191)
        with open(filename, "r") as file:
            for line in file:
                line_count += 1
                line = line.replace("'", '')
                for punctuatin in string.punctuation:
                    line = line.replace(punctuatin, ' ')
                word_list = line.split()
                for word in word_list:
                    if self.stop_table == None or (word.isalpha() and not self.stop_table.in_table(word.lower())):
                        self.add_insert(word, line_count)


    def add_insert(self, word, line_count):
        if self.concordance_table.in_table(word.lower()):
            value = self.concordance_table.get_value(word.lower())
            if value[-1] != line_count:
                value.append(line_count)
        else:
            self.concordance_table.insert(word.lower(), [line_count])

    # """ Write the concordance entries to the output file(filename)
    # See sample output files for format."""
    def write_concordance(self, filename):

        key_list = self.concordance_table.get_all_keys()
        key_list.sort()
        with open(filename, "w") as write_file:

            for key in key_list:
                value = self.concordance_table.get_value(key)
                # write_file.write(key + ':' + " " + value.value_string() + "\n")
                string_list = ' '.join([str(index) for index in value])
                write_file.write(key + ':' + " " + string_list + "\n")