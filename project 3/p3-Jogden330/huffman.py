from ordered_list import *
from huffman_bit_writer import *
from huffman_bit_reader import *

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    # checks If Huffmen node is equal to the onother Huffman node
    def __eq__(self, other):
        return type(other) == HuffmanNode and self.freq == other.freq and self.char == other.char

    # checks If Huffmen node is less the onother Huffman node
    # the order is decided by frequency with tise going to the charicter value
    def __lt__(self, other):
        if self.freq == other.freq:
            return type(other) == HuffmanNode and self.char < other.char
        else:
            return type(other) == HuffmanNode and self.freq < other.freq

    # string -> List
    # '''Opens a text file with a given file name (passed as a string) and counts the
    #     frequency of occurrences of all the characters within that file'''
    def cnt_freq(filename):
            char_freq = [0]*256
            with open(filename,"r") as file:        # opens the file as readable
                for line in file:                   # inports each line in the file
                    for char in line:               # itorates each charicter in the line
                        char_freq[ord(char)] += 1   # adds one to the list in the index representing the askii value of the charicter
            return char_freq

        # list -> Huffmantree
        # '''Create a Huffman tree for characters with non-zero frequency
        #     Returns the root node of the Huffman tree'''
    def create_huff_tree(char_freq):
        return huff_list_to_tree(create_huff_ord_list(char_freq))  #chreats the huffman trey be calling two helper functions

        # list -> ordered list
        # '''creats an orededed list of huffman Nodes containing each non zero iteam in a frequench array '''
    def create_huff_ord_list(char_freq):
        ordered_huff_list = OrderedList()                                       #enitalizing the huffman node
        for index in range(len(char_freq)):                                     #cical throu each entry in a frequench array
            if char_freq[index] != 0:                                           #if entery in the frequench array is zero it wont be added to the ordered list
                ordered_huff_list.add(HuffmanNode(index, char_freq[index]))     #creats the hufmannade and adds it to the ordered list
        return ordered_huff_list

        # orderedlist -> Huffmantree
        # '''creats a hufman tree from an ordered list, it the ordered kist is empty returns non'''
    def huff_list_to_tree(ordered_huff_list):
        if ordered_huff_list.size() == 0:                                                   #if the ordered list is empty returns None
            return None
        if ordered_huff_list.size() == 1:
            node = ordered_huff_list.pop(0)
            return HuffmanNode(node.char,node.freq)
        while ordered_huff_list.size() > 1:                                                 #as lond as there are mor the one thing in the ordered list do the fallowing
            leaf_1 = ordered_huff_list.pop(0)                                               #pop the first two items off the list
            leaf_2 = ordered_huff_list.pop(0)
            Tree = HuffmanNode(min(leaf_1.char,leaf_2.char), leaf_1.freq + leaf_2.freq)     #creat a new fufman node that has the smallist the frequency of bothe iteam poped off the list
            Tree.left = leaf_1                                                              #set the new nodes praches equal to that of the previas nodes
            Tree.right = leaf_2
            ordered_huff_list.add(Tree)                                                     #add the new back onto the ordered list
        return ordered_huff_list.pop(0)                                                     #return the root ot the Huffman tree

        # Huffmantree -> list
        # '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
        #     as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    def create_code(node):
        code = ""                                              # initalizes code string
        code_list = [''] * 256                                 # initsalizes code list to none
        if node == None:                                       # if the node peramiter dose not exist return an empty code list
            return code_list
        if node.left is None and node.right is None:           # if the node peramiter dose not exist return an empty code list
            return code_list
        return create_code_rec(node, code, code_list)          # calls a helperfunction to creat the code list

        # Huffmantree, string, list -> list
        # '''Returns an array (Python list) of Huffman codes. For each node on a fufman tree recrursivly, use the integer ASCII representation
        #     as the index into the arrary, with the resulting Huffman code for that character stored at that location'''
    def create_code_rec(node, code, code_list):
        if node.left is None and node.right is None:           #if the node is a lief on the trey store the code into the list and return
            code_list[node.char] = code
            return
        create_code_rec(node.left, code + "0", code_list)      #make a recursive call on the lest side of the tree appending a "0" to the code
        create_code_rec(node.right, code + "1", code_list)     #make a recursive call on the right side of the tree appending a "1" to the code
        return code_list                                       #return the list

        # list -> string
        # '''Input is the list of frequencies. Creates and returns a header for the output file
        # Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    def create_header(freqs):
        header_string = ""                                                                      #enitalizes the string
        for index in range(len(freqs)):                                                         #itreates throge each element on the frequench list
            if freqs[index] != 0:                                                               #it the index in the list is zero do right to the string
                header_string = header_string + str(index) + " " + str(freqs[index]) + " "      #appends the aski value and the frequency to the string
        return header_string[:-1]                                                               #return all but the last space to the string

        # string, string -> None
        # '''Takes inout file name and output file name as parameters - both files will have .txt extensions
        # Uses the Huffman coding process on the text from the input file and writes encoded text to output file
        # Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
        # This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods
        # provided in the huffman_bits_io module to write both the header and bits.
        # Take not of special cases - empty file and file with only one unique character'''
    def huffman_encode(in_file, out_file):
        heder_string = create_header(frep_list)                             #creates the heder file
        code_list = create_code(create_huff_tree(frep_list))                #creats the code

        incoder = HuffmanBitWriter(out_file[:-4] + "_compressed.txt")       #creats and opens a file to store the compresses output

        with open(in_file, "r") as read_file:                               # opens the input file as readable
            with open(out_file, "w") as write_file:                         # opens the output file as writable
                 if heder_string != "":                                     # if the header file is an empy strin right nothing to the fials

                     write_file.write(heder_string  + "\n")                 # adds the headrstring to the output file
                     incoder.write_str(heder_string  + "\n")                # adds the headrstring to the compressed file
                     for line in read_file:                                 # reads the input file line by line the charicter by charicter
                         for char in line:
                             incoder.write_code(code_list[ord(char)])       #rights the charicter representation of each code to the output file
                             write_file.write(code_list[ord(char)])         #rights the cconpression file

            incoder.close()                                                 #closes the compression file
    # string -> list
    # turns a header string into a frep_list
    def parse_header(header_string):
        char_freq = [0] * 256
        if header_string == "" or header_string is None:
            return char_freq
        char_freq = [0] * 256
        header_list = header_string.split()
        for i in range(0, len(header_list), 2):
            char_freq[int(header_list[i])] = int(header_list[i+1])
        return char_freq

    # string, string -> None
    # decompresses a huffmen compressed file and saves it as the decoded_file
    def huffman_decode(encoded_file, decode_file):

        decoder = HuffmanBitReader(encoded_file)
        write_file = open(decode_file, "w")
        header = decoder.read_str()
        if header != "":

            freq_list = parse_header(header)
            toptree = create_huff_tree(freq_list)
            total_char = 0
            treenode = toptree

            for index in freq_list:
                total_char += index

            while total_char > 0:
                if treenode.left is None and treenode.right is None:
                        write_file.write(chr(treenode.char))
                        treenode = toptree
                        total_char -= 1
                else:
                        bit = decoder.read_bit()
                        if bit is False:
                            treenode = treenode.left
                        if bit is True:
                            treenode = treenode.right

        write_file.close()
        decoder.close()