def sort_words_in_file(input_file, output_file):
    try:
        with open(input_file,'r') as file:
            words=file.read().split()
            words=[word.lower() for word in words]
        words.sort()
        with open(output_file,'w') as file:                 
                for word in words:
                    file.write(word + '')
                print("words have been sorted and  written to ",output_file)
    except FileNotFoundError :
        print(" Error: the input file does not exist ")
    except Exception as e :
        print(f"an error occured: {e}")
    input_file='input.txt'
    output_file='output_file.txt'
sort_words_in_file('input_file','output_file')
        
            