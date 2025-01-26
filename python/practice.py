def count_file_lines(input_file):
    num_characters=0
    num_words=0
    num_lines=0
    with open (input_file,'r') as file:
        for line in file:
            num_lines +=1
            num_characters +=len(line)
            words=line.split()
            num_words+=len(words)
        print("no of lines: ",num_lines)
        print("no of words: ",num_words)
        print("no of characters: ",num_characters)
input_file="sample.txt"
count_file_lines(input_file)