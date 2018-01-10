import os, glob
import lzw

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

run_test("lzw")
compare("lzw")


