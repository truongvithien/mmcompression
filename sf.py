import os


def init_stat_table(source_content_list):
    """
    :param source_content:
    :return:
    probability table stored like this..
    symbol  count
    """
    prob_table = {}
    # count
    for each_char in source_content_list:
        meet_char = next((key for key, value in prob_table.items() if key == each_char), None)
        if meet_char != None:
            prob_table[each_char] = prob_table[each_char] + 1
        else:
            prob_table.update({each_char:1})
    # calculate prob
    for each_symbol in prob_table:
        prob_table[each_symbol] = prob_table[each_symbol]/len(source_content_list)
    return prob_table

def make_approx(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key = lambda x:x[1]))
    new_list = [0 for x in range(len(sorted_dict))]
    flag = 0
    id = 0
    left_dict = dict()
    right_dict = dict()
    for each_key in sorted_dict.keys():
        if flag == 0:
            new_list[id] = each_key
            left_dict.update({new_list[id]:sorted_dict[new_list[id]]})
            flag = 1
        else:
            new_list[len(new_list)-id-1] = each_key
            right_dict.update({new_list[len(new_list)-id-1]:sorted_dict[new_list[len(new_list)-id-1]]})
            flag = 0
            id += 1
    return left_dict, right_dict

def sf_recursive(dict_table, string_list, root_code):
    size = len(string_list)
    if size <= 1:
        dict_table[list(string_list)[0]] = root_code
        #print("symbol",list(string_list)[0],"prob:",list(string_list.values())[0],"; code:",root_code)
    else:
        string_list_left, string_list_right = make_approx(string_list)
        sf_recursive(dict_table,string_list_left, root_code + "1")
        sf_recursive(dict_table,string_list_right, root_code + "0")

def compress(source):
    dict_table = {}
    source_content = source.read()
    article_name = source.name[6:-4]
    source_content_list = list(source_content)
    sf_recursive(dict_table,init_stat_table(source_content_list), "")
    output_dict = open(os.path.join("data","sf",article_name + "-dictionary.txt"),"w",encoding="utf-8")
    output_binary = open(os.path.join("data","sf",article_name + "-binary.txt"),"w",encoding="utf-8")
    #print(output_dict)
    for each_ele in dict_table:
        output_dict.write(each_ele+"\t"+dict_table[each_ele]+"\t")

    output_code = list()
    for each_char in source_content_list:
        code = dict_table[each_char]
        output_code.append(code)
        output_binary.write(code+" ")
    output_dict.close()
    output_binary.close()
    return dict_table, output_code

def decompress(dictionary, code):
    dict_content_list = dictionary.read().split("\t")
    code_content_list = code.read().split(" ")
    article_name = code.name[8:-11]
    output_string = ""
    for each_bin in range(len(code_content_list)-1):
        output_string += dict_content_list[dict_content_list.index(code_content_list[each_bin])-1]

    output_decode = open(os.path.join("data","sf",article_name + "-decoded.txt"),"w",encoding="utf-8")
    output_decode.write(output_string)
    output_decode.close()
    return 0

