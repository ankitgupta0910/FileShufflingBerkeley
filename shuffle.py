import urllib

fi = open("/Users/ankitgupta/PycharmProjects/untitled1/sample_input", "r")
# fo = open(output_file1, "w+")
# print fi.read().replace('\n', '+')
lines = fi.readlines()
frag_list = []
for line in lines:
    # print line
    frag_list.append(urllib.unquote_plus(line))
    # fo.write(urllib.unquote_plus(line.replace('\n', '###')))
fi.close()
for i in frag_list:
    print i
# for idx in range(0, len(frag_list)):
#     if idx is len(frag_list) - 1:
#         break
#     str1 = frag_list[idx][0:-1]
#     str2 = frag_list[idx + 1][0:-1]
#     i = 1
#     j = -1
#     while str1 is not str2:
#         str1 = str1[1:]
#         str2 = str2[:-1]
#     print str1
#     print str2
# fo.close()
