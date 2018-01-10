import os

# init ascii dictionary
# the larger range, the exactly encode (but it make slower)
range_ascii = 256

def init_dict():
    ascii_dict = dict()
    ascii_in_number = range(1,range_ascii)
    for each_char in ascii_in_number:
        ascii_dict[each_char] = chr(int(hex(each_char),16))
    print("Status: Initialized ascii table.")
    dictionary = ascii_dict
    return(dictionary)

def compress(source):
    dictionary = init_dict()
    source_content = source.read()
    lists = list(source_content)
    id = 0
    s = lists[0]
    output_code = list()
    article_name = source.name[6:-4]
    output_table_dictionary = open(os.path.join("data","lzw",article_name + "-table-dictionary.txt"),"w",encoding="utf-8")
    output_table_work = open(os.path.join("data","lzw",article_name + "-table-work.txt"),"w",encoding="utf-8")
    output_decimal = open(os.path.join("data","lzw",article_name + "-decimal.txt"),"w",encoding="utf-8")
    output_binary = open(os.path.join("data","lzw",article_name + "-binary.txt"),"w",encoding="utf-8")

    output_table_work.write("s\tc\tout\tcode\tstring\n===================================\n")
    content_len = len(lists)
    dictionary_len = len(dictionary)
    while (id < content_len-1):
        c = lists[id+1]
        print("== check ",id, " {",s,";",c,"}")
        print(s+"\t"+c)
        join = s + c
        if join in dictionary.values():
            s = join
            #step = len(join)+1
            print("s + c {"+join+"} founded")
            output_table_work.write(s+"\t"+c+"\n")
        else:
            dictionary_len = dictionary_len + 1
            code = next((key for key, value in dictionary.items() if value == s), 63)
            output_code.append(code)
            dictionary.update({dictionary_len:join})
            print("== dictionary update : ",{dictionary_len:join})
            output_table_work.write(s+"\t"+c+"\t"+str(code)+"\t"+str(dictionary_len)+"\t"+join+"\n")
            s = c
        code = next((key for key, value in dictionary.items() if value == s), 63)
        #output_code.append(code)
        id = id + 1
        if id+1 == len(lists):
            c = "EOF"
            code = next((key for key, value in dictionary.items() if value == s), 63)
            output_code.append(code)
            output_table_work.write(s+"\t"+"EOF!\t"+str(code))
            break
    # output return table
    output_table_dictionary.write("code\tstring\n")
    output_table_dictionary.write("===============\n")
    sorted(dictionary.items(), key = lambda x:x[1])
    for key, value in dictionary.items():
        output_table_dictionary.write(str(key)+"\t"+str(value)+"\n")
    output_table_dictionary.close()

    # output return decimal, binary
    for code in output_code:
        output_decimal.write(str(code)+" ")
        print(code)
        print(bin(code))
        output_binary.write(str(bin(code))+" ")
    output_decimal.close()
    output_binary.close()
    return output_code

def decompress(code):
    print(code.name)
    article_name = code.name[9:-12]
    output_string = list()
    dictionary = init_dict()
    code_content = code.read()
    lists = code_content.split(" ")
    dictionary_len = len(dictionary)
    output_decode = open(os.path.join("data","lzw",article_name + "-decoded.txt"),"w",encoding="utf-8")
    output_dictionary = open(os.path.join("data","lzw",article_name + "-decoded-dictionary.txt"),"w",encoding="utf-8")
    code_len = len(lists)
    s = None
    id = -1
    while (id < len(lists)-1):
        k = lists[id+1]
        if k == '':
            break
        if int(k) <= dictionary_len:
            entry = dictionary[int(k)]
        else:
            entry = None
        print(k," : ",entry)
        if entry == None:
            if s != None:
                entry = s + s[0]
                print(entry)
            #else:
            #    entry = s

        output_string.append(entry)
        if (s != None):
            dictionary_len = dictionary_len + 1
            print("dictionary update: ",{dictionary_len:s+entry[0]})
            dictionary.update({dictionary_len:s+entry[0]})
        s = entry
        id = id + 1
    sorted(dictionary.items(), key = lambda x:x[1])
    for key, value in dictionary.items():
        output_dictionary.write(str(key)+"\t"+str(value)+"\n")
    output_dictionary.close()

    print(output_string)
    print(dictionary)

    for string in output_string:
        output_decode.write(string)
    output_decode.close()
    return entry

