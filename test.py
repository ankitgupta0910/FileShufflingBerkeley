import urllib
import sys, os
from suffix_tree import SuffixTree

def overLappedStringLength(s1, s2):
    t = []
    if len(s1) > len(s2):
        s1 = s1[len(s1) - len(s2):]

    t = computeBackTrackTable(s2)
    if t is not None:
        m = 0
        i = 0
        while m + i < len(s1):
            if s2[i] is s1[m + i]:
                i += 1
            else:
                m += i - t[i]
                if i > 0:
                    i = t[i]

        return i
    else:
        return False


def computeBackTrackTable(s):
    t = []
    cnd = 0
    t.insert(0, -1)
    t.insert(1, 0)
    pos = 2
    while pos < len(s):
        if s[pos - 1] is s[cnd]:
            t.insert(pos, cnd+1)
            pos += 1
            cnd += 1
        elif cnd > 0:
            cnd = t[cnd]
        else:
            t.insert(pos,0)
            # t[pos] = 0
            pos += 1

    return t

if len(sys.argv) is not 1:
    input_file =  sys.argv[1]
    output_file1 = sys.argv[1] + "_op1.txt"
    output_file2 = sys.argv[1] + "_op2.txt"
    output_file3 = sys.argv[1] + "_op3.txt"
else:
    fo = open(os.getcwd() + "/temp_input.txt", "w+")
    for line in sys.stdin:
        # print line
        fo.write(line)
    fo.close()
    input_file = os.getcwd() + "/temp_input.txt"
    output_file1 = os.getcwd() + "/temp_output1.txt"
    output_file2 = os.getcwd() + "/temp_output2.txt"
    output_file3 = os.getcwd() + "/temp_output3.txt"

fi = open(input_file, "r")
fo = open(output_file1, "w+")
# print fi.read().replace('\n', '+')
lines = fi.readlines()

for line in lines:
    # print line.replace('\n','###')
    fo.write(urllib.unquote_plus(line.replace('\n', '###')))
fi.close()
fo.close()


###########################Step 2#################################
fi = open(output_file1, "r")
fo = open(output_file2, "w+")
lines = fi.readlines()
for line in lines:
    # print line
    templine = line
    # if templine.isspace():
    #     print "Ankit" + templine
    # else:
    while "###" in templine:
        str = templine.split("###", 1)
        # print len(str)
        if len(str) > 1:
                n = overLappedStringLength(str[0], str[1])
                if n > 2 or str[1] is '':
                    # print str[1][n:]
                    templine = str[0] + str[1][n:]
                    # print str[0] + str[1][n:]
                else:
                    templine = ''
    # print templine
    fo.write(templine)
# print line
fi.close()
fo.close()

###########################Step 3#################################
fi = open(output_file2, "r")
fo = open(output_file3, "w+")
lines = fi.readlines()
oldline = ''
for line in lines:
    if oldline is line:
        fo.write('')
    else:
        fo.write(line)
    oldline = line
fi.close()
fo.close()








#     stree = SuffixTree(str)
# #
#     data = {}
#     for l in stree.innerNodes:
#     # print len(l.pathLabel), l.pathLabel
#         data[l.pathLabel] = len(l.pathLabel)
# # print max(stree.innerNodes)
# # for key, value in data.iteritems():
# #     print key, value
# #     print data.keys()[data.values().index(max(data.itervalues()))]  # Prints george
#     patt = data.keys()[data.values().index(max(data.itervalues()))]  # Prints george
#     otpt = str.replace(patt, '', 1)
#     fo.write(otpt)
#     print str.replace(patt, '', 1)
# fi.close()
# fo.close()

########################################

# #
# fi = open("/Users/ankitgupta/PycharmProjects/untitled1/shake4_input", "r")
# fo = open("/Users/ankitgupta/PycharmProjects/untitled1/shake4_output", "w")
# # print fi.read().replace('\n', '')
# stree = SuffixTree('public class HelloWorld rld {')
# #
# data = {}
# for l in stree.innerNodes:
#     # print len(l.pathLabel), l.pathLabel
#     data[l.pathLabel] = len(l.pathLabel)
# # print max(stree.innerNodes)
# for key, value in data.iteritems():
#     print key, value
# print data.keys()[data.values().index(max(data.itervalues()))]  # Prints george
# print '//shake4 prograe program'.replace('e progra', '', 1)

# def pattern(inputv):
#
#     k = 0
#     # while pattern_end < len(inputv):
#     for i in range(0, len(inputv)):
#         pattern_end = i
#         for j in range(pattern_end + 1, len(inputv)):
#
#             pattern_dex = j % (pattern_end + 1)
#             if (inputv[pattern_dex] != inputv[j]):
#                 pattern_end = j;
#                 continue
#
#             if (j == len(inputv) - 1):
#                 print pattern_end
#                 print inputv[0:pattern_end + 1];
#         print inputv;


# def pattern(inputv):
#     for i in range(0,len(inputv) - 1):
#         for j in range(i+1,len(inputv) - 1):
#             if inputv[i] is inputv[j]:
#                 pattern_end = i
#                 for k in range(pattern_end + 1, len(inputv)):
#                     pattern_dex = k % (pattern_end + 1)
#                     if (inputv[pattern_dex] != inputv[j]):
#                         pattern_end = k;
#                         continue
#
#                     if (k == len(inputv) - 1):
#                         print pattern_end
#                         print inputv[0:pattern_end + 1]
#                 print inputv;
#
# str = "shake4_output1 prograe progra"
#
# pattern(str)

# j = 2
# result = ''
# for i, d in enumerate(str):
#     j = i + 1
#     while j < len(str):
#         if str[i] is str[j]:
#             while str[i] is not str[j]:
#                 i += 1
#                 j += 1
#                 result = result + str[i]
#             print str[i],
#             j += 1
#         else:
#             j += 1
