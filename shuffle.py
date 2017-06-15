import urllib

fi = open("/Users/ankitgupta/PycharmProjects/untitled1/sample_input", "r")
lines = fi.readlines()
frag_list = []
for line in lines:
    # print line
    frag_list.append(line)
    # frag_list.append(urllib.unquote_plus(line.replace('\n', '')))
    # fo.write(urllib.unquote_plus(line.replace('\n', '###')))
fi.close()
length = len(frag_list)
i = 0
result_list = [''] * len(frag_list)
for idx, val in enumerate(frag_list):
    temp_list = frag_list[0:len(frag_list)]
    temp_val = temp_list[i]
    str1 = temp_val[:-1]
    temp_list.remove(temp_val)
    while not any(item.startswith(str1) for item in temp_list) and len(str1) >= 3:
        str1 = str1[1:]
    else:
        # print "Str1", " ", str1
        if any(item.startswith(str1) for item in temp_list):
            # print "In eIF"
            i += 1
        else:
            # print "Ijn else"
            # print temp_list
            result_list[len(frag_list)-1] = temp_val
            break

i = 1
while frag_list is not None:
    # temp_list = frag_list[0:len(frag_list)]
    # temp_val = temp_list[i]
    str1 = result_list[length-i][:-1]
    print str1
    # frag_list.remove(str1)
    # str1 = str1[:-1]
    while not any(item[2:-1].endswith(str1) for item in frag_list) and len(str1) >= 3:
        str1 = str1[:-1]
    else:
        # print "Str1", " ", str1
        for item in temp_list:
            if item[:-1].endswith(str1):
                result_list[length-i-1] = item
                try:
                    frag_list.remove(item)
                except:
                    print item
                i += 1
                break

print result_list
print len(frag_list)
print frag_list
