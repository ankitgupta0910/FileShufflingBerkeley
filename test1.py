def overLappedStringLength(s1, s2):
    t = []
    if len(s1) > len(s2):
        s1 = s1[len(s1) - len(s2):]

    t = computeBackTrackTable(s2)

    m = 0
    i = 0
    while m + i < len(s1):
        if s2[i] is s1[m + i]:
            i += 1
        else:
            m += i - t[i]
            if i > 0:
                i = t[i];

    print i


def computeBackTrackTable(s):
    t = []
    cnd = 0
    t.insert(0, -1)
    t.insert(1, 0)
    pos = 2
    l = len(s)
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


overLappedStringLength("This day is cal", "is call'd the f###d the feast of ###east of Crispia###rispian.")
#
# print computeBackTrackTable("is call'd the f###d the feast of ###east of Crispia###rispian.")

# print computeBackTrackTable("e program")

# print computeBackTrackTable("d the feast of ###east of Crispia###rispian.")
