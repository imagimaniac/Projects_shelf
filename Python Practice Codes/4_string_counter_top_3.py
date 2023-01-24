import math
import os
import random
import re
import sys
import operator
from collections import Counter

# Count top 3 most occurring string letters

def arrange_strin_count(s):
    dict_1 = {}
    lis = []
    for i in range(len(s)):
        if s[i] in lis:
            continue
        else:
            dict_1[s[i]] = s.count(s[i])
            lis.append(s[i])
    k = Counter(dict_1)
    high = k.most_common(3)
    print(high)
    
s = input()  
arrange_strin_count(s)
