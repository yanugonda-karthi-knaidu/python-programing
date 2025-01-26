def count_vowels(input_string):
    vowels ="aeiouAEIOU"
    vowel_count=sum(map(input_string.count,vowels))
    return vowel_count
input_string=str(input("enter the string :"))
vowel_count=count_vowels(input_string)
print(f"number of vowels in the string: {vowel_count}")


