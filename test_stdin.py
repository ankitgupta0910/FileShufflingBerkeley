# import sys
# import os
#
#
# print os.getcwd()
# fo = open(os.getcwd()+"/temp.txt", "w+")
# for line in sys.stdin:
#     # print line
#     fo.write(line)
# fo.close()
#
#
# # print 'Number of arguments:', len(sys.argv), 'arguments.'
# # print 'Argument List:', sys.argv
# #
# # input =  sys.argv[1]
# # op1 = sys.argv[1] + "_op1"
# # op2 = sys.argv[1] + "_op2"
# # op3 = sys.argv[1] + "_op3"
# # # filename = input.split('/')
# # # op = filename[len(filename)-1].split
# # # print type(input)
# # print op1
# # print op2
# # print op3
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

templine = "Must needs g###ds give sentenc###sentence 'gains###nce 'gainst the###ainst the merch### the merchant t###erchant there.##"
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
print templine
