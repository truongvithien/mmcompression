import os, sys
import lzw, sf

test_folder = "text//"
test_list = os.listdir(test_folder)
print(test_list)
print(len(test_list))

def run_test (algorithm):
    if algorithm == "lzw":
        for each_test in range(0,len(test_list)):
            print("Status: running test ",test_list[each_test])
            source_file = open(os.path.join(test_folder,test_list[each_test]),"r",encoding='utf-8')
            lzw.compress(source_file)
            code_file = open(os.path.join("data","lzw",test_list[each_test][:-4]+"-decimal.txt"),"r",encoding="utf-8")
            lzw.decompress(code_file)
    elif algorithm == 'sf':
        for each_test in range(0,len(test_list)):
            print("Status: running test ",test_list[each_test])
            source_file = open(os.path.join(test_folder,test_list[each_test]),"r",encoding='utf-8')
            sf.compress(source_file)
            dict_file = open(os.path.join("data","sf",test_list[each_test][:-4]+"-dictionary.txt"),"r",encoding="utf-8")
            code_file = open(os.path.join("data","sf",test_list[each_test][:-4]+"-binary.txt"),"r",encoding="utf-8")
            sf.decompress(dict_file, code_file)

def compare(algorithm):
    if algorithm == "lzw":
        for each_test in range(0,len(test_list)):
            print("Status: check accurency ",test_list[each_test])
            source_file = open(os.path.join(test_folder,test_list[each_test]),"r",encoding='utf-8')
            code_file = open(os.path.join("data","lzw",test_list[each_test][:-4]+"-decoded.txt"),"r",encoding="utf-8")
            source_text = source_file.read()
            code_text = code_file.read()
            source_text_list = source_text.split(" ")
            code_text_list = code_text.split(" ")
            print(source_text_list)
            print(code_text_list)
            accurency = 0
            for each_text in range(len(source_text_list)):
                if (source_text_list[each_text] == code_text_list[each_text]):
                    accurency = accurency + 1
                else:
                    print("error at (",each_test,"): ",source_text_list[each_text]," & ",code_text_list[each_text])
            print("-- Accurency: ", accurency/len(source_text_list))
    elif algorithm == "sf":
        for each_test in range(0,len(test_list)):
            print("Status: check accurency ", test_list[each_test])
            source_file = open(os.path.join(test_folder,test_list[each_test]),"r",encoding='utf-8')
            decode_file = open(os.path.join("data","lzw",test_list[each_test][:-4]+"-decoded.txt"),"r",encoding='utf-8')
            source_text = source_file.read()
            decode_text = decode_file.read()
            source_text_list = source_text.split(" ")
            decode_text_list = decode_text.split(" ")
            accurency = 0
            for each_text in range(len(source_text_list)):
                if (source_text_list[each_text] == decode_text_list[each_text]):
                    accurency = accurency + 1
                else:
                    print("error at (",each_test,"): ",source_text_list[each_text]," & ",decode_text_list[each_text])
            print("-- Accurency: ", accurency/len(source_text_list))

def compression_ratio(algorithm):
    if algorithm == "lzw":
        for each_test in range(0,len(test_list)):
            print("Status : calculate compression ratio ", test_list[each_test])
            source_file = open(os.path.join(test_folder,test_list[each_test]),"r",encoding='utf-8')
            code_file = open(os.path.join("data","lzw",test_list[each_test][:-4]+"-decimal.txt"),"r",encoding='utf-8')
            source_text = source_file.read()
            b0 = len(source_text)*8
            print("b0 = ",b0)
            code_text = code_file.read()
            b1 = len(code_text.split(" "))*10
            print("b1 = ",b1)
            print("Compresssion ratio calculated: ", b0/b1)
    elif algorithm == "sf":
        for each_test in range(0,len(test_list)):
            print("Status : calculate compression ratio ", test_list[each_test])
            source_file = open(os.path.join(test_folder,test_list[each_test]),"r",encoding='utf-8')
            code_file = open(os.path.join("data","sf",test_list[each_test][:-4]+"-binary.txt"),"r",encoding='utf-8')
            source_text = source_file.read()
            code_text = code_file.read()
            source_list = list(source_text)
            code_list = code_text.split(" ")
            # calc b0:
            b0 = len(source_list)*8
            print("b0 = ",b0)
            # calc b1:
            b1 = 0
            for each_code in code_list:
                b1 += len(each_code)
            print("b1 = ",b1)
            print("Compresssion ratio calculated: ", b0/b1)


#run_test("lzw")
#compare("sf")
#compression_ratio("sf")

