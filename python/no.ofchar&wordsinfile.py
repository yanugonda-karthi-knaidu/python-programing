def count_file_starts(filename):
    num_character=0
    num_words=0
    num_lines=0
    with open(filename,'r') as file:
        for line in file: 
            num_lines+=1
            num_character+=len(line)
            words=line.split()
            num_words+=len(words)
            print("number of characters: ",num_character)
            print("number of  words: ",num_words)
            print("number of lines : ",num_lines)
filename="sample.txt"
count_file_starts(filename)