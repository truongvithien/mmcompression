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
            source_file_dir = os.path.join(test_folder,test_list[each_test])
            lzw.compress(source_file_dir)
            code_file_dir = os.path.join("data","lzw",test_list[each_test][:-4]+"-decimal.txt")
            lzw.decompress(code_file_dir)
    elif algorithm == 'sf':
        for each_test in range(0,len(test_list)):
            print("Status: running test ",test_list[each_test])
            source_file = os.path.join(test_folder,test_list[each_test])
            sf.compress(source_file)
            dict_file_dir = os.path.join("data","sf",test_list[each_test][:-4]+"-dictionary.txt")
            code_file_dir = os.path.join("data","sf",test_list[each_test][:-4]+"-binary.txt")
            sf.decompress(dict_file_dir, code_file_dir)

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
        output_cr_lzw = open(os.path.join("data","compression_ratio_lzw.txt"),"w",encoding='utf-8')
        for each_test in range(0,len(test_list)):
            print("Status : calculate compression ratio ", test_list[each_test])
            source_file = open(os.path.join(test_folder,test_list[each_test]),"r",encoding='utf-8')
            code_file = open(os.path.join("data","lzw",test_list[each_test][:-4]+"-decimal.txt"),"r",encoding='utf-8')
            source_text = source_file.read()
            code_text = code_file.read()
            source_list = list(source_text)
            code_list = code_text.split(" ")
            # calc b0:
            b0 = len(source_list)*8
            print("b0 = ",b0)
            # calc b1:
            b1 = 0
            for each_code in range(len(code_list)-1):
                b1 += len(str(bin(int(code_list[each_code]))))
            print("b1 = ",b1)
            cr = b0/b1
            print("Compresssion ratio calculated: ", cr)
            output_cr_lzw.write(test_list[each_test]+"\t"+str(cr)+"\n")
        output_cr_lzw.close()
    elif algorithm == "sf":
        output_cr_sf = open(os.path.join("data","compression_ratio_sf.txt"),"w",encoding='utf-8')
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
            cr = b0/b1
            print("Compresssion ratio calculated: ", cr)
            output_cr_sf.write(test_list[each_test]+"\t"+str(cr)+"\n")
        output_cr_sf.close()

def main():
    algorithms = ["lzw"]
    for each_algorithm in algorithms:
        run_test(each_algorithm)
        compare(each_algorithm)
        compression_ratio(each_algorithm)

main()



