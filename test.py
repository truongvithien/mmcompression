import os

test_folder = "text//"
test_list = os.listdir(test_folder)
sumary = open(os.path.join("sumary.txt"),"w",encoding='utf-8')
sumary.write("id\tname\tfize size\tword count\tchar count\n")
for each_test in range(0, len(test_list)):
    test_file = open(os.path.join(test_folder,test_list[each_test]),"r",encoding='utf-8')
    test_content = test_file.read()
    sumary.write(str(each_test)+"\t"+test_list[each_test]+"\t"+str(os.path.getsize(os.path.join(test_folder,test_list[each_test])))+"\t"+str(len(test_content.split(" ")))+"\t"+str(len(test_content))+"\n")

sumary.close()
