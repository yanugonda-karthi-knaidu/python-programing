#writ a python program to create, display, append, insert and reverse the order of the items in the array

def display_array(arr):
    print("Current Array:", arr)

def append_to_array(arr, item):
    arr.append(item)
    print(f"Appended {item} to the array.")

def insert_to_array(arr, index, item):
    if 0 <= index <= len(arr):
        arr.insert(index, item)
        print(f"Inserted {item} at index {index}.")
    else:
        print("Index out of bounds!")

def reverse_array(arr):
    arr.reverse()
    print("Array reversed.")

def main():
    array = [1, 2, 3, 4, 5]
    display_array(array)
    append_to_array(array, 6)
    display_array(array)
    insert_to_array(array, 2, 10)
    display_array(array)
    reverse_array(array)  
if __name__ == "__main__":
    main()