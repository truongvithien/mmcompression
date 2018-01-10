def init_dict():
    ascii_dict = dict()
    ascii_in_number = range(1,4048)
    for each_char in ascii_in_number:
        ascii_dict[each_char] = chr(int(hex(each_char),16))
    print("Status: Initialized ascii table.")
    dictionary = ascii_dict
    return(dictionary)

dictionary = init_dict()

for key, value in dictionary.items():
    print(str(key)+"\t"+str(value)+"\n")

print(chr(int("0x20AC",16)))

print(int("0x20AC",16))
