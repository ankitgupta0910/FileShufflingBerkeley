import urllib
from operator import sub

fi = open("/Users/ankitgupta/PycharmProjects/untitled1/sample_input", "r")
# fo = open(output_file1, "w+")
# print fi.read().replace('\n', '+')
lines = fi.readlines()
frag_list = []
for line in lines:
    # print line
    frag_list.append(line)
    # fo.write(urllib.unquote_plus(line.replace('\n', '###')))
fi.close()

# for i in frag_list:
#     print i
print frag_list
i = 1
result_list = [''] * len(frag_list)
for idx, val in enumerate(frag_list):
    str1 = frag_list[idx][:-1]
    if idx is len(frag_list) - 1:
        result_list[len(frag_list) - 1] = str
        break
    while not any(item.startswith(str1) for item in frag_list):
    # while not frag_list[idx].startswith(str1) and str1 is not '':
        str1 = str1[1:]
    else:
        if str1 is '' and idx is len(frag_list) - 1:
            result_list[len(frag_list) - 1] = val
            break
        else:
            i += 1
            continue
    if result_list[:-1] is not '':
        break
# j = 1
# for k in frag_list:
#     for i in frag_list:
#         str = i[0:-1]
#         print type(j)
#         print type(len(result_list))
#         print len(result_list) - j
#         str1 = result_list[len(result_list) - j]
#         print str1
#         while not str.startswith(result_list[len(result_list) - j]) and str is not '':
#             str = str[1:]
#         else:
#             if str is not '':
#                 result_list.insert(len(result_list)-j-1, i)
#                 j += 1

print result_list


# for idx in range(0, len(frag_list)):
#     found_global = False
#     found_local = False
#     chk_str = idx
#     nex_str = idx + 1
#     if idx is len(frag_list) - 1:
#         break
#     str1 = frag_list[idx][:-1]
#     str2 = frag_list[idx + i]
#     # i = 1
#     # j = -1
#
#     while not found_global:
#         while not str2.startswith(str1):
#             str1 = str1[1:]
#             # str2 = str2[:-1]
#         else:
#             if str1 is '':
#                 temp_str = frag_list[len(frag_list) - 1]
#                 frag_list[len(frag_list) - 1] = frag_list[idx]
#                 frag_list[idx] = temp_str
#             else:
#                 found_local = True
#                 found_global = True
#         if found_local:
#             if nex_str - chk_str is 1:
#                 print str1, " ", str2
#             else:
#                 temp_str = frag_list[nex_str]
#                 frag_list[nex_str] = frag_list[idx + i]
#                 frag_list[idx + i] = temp_str
#         else:
#             while i < len(frag_list) - 1:
#                 i += 1
#                 str1 = frag_list[idx][:-1]
#                 str2 = frag_list[idx + i]
#                 found_local = False
#     print str1
#
#     # print str2
# # fo.close()
