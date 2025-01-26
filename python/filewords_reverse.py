def print_reversed_lines(filename):
    try:
        with open (filename,'r') as file:
            for line in file:
                print(line.strip()[::-1])
    except FileNotFoundError:
        print("the file does not found")
    except Exception as e:
        print(f"an error occured:{e}")
filename="sample.txt"
print_reversed_lines(filename)