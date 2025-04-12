D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

#UNION
D_UNION = {}
for key in D1:
    if key not in D_UNION:
        D_UNION[key] = D1[key]
for key in D2:
    if key not in D_UNION:
        D_UNION[key] = D2[key]
        
print("UNION:",D_UNION)
#OUTPUT - UNION: {'ok': 1, 'nok': 2, 'new': 3}

#INTERSECTION
D_INTERSECTION = {}
for key in D1:
    if key in D2:
        D_INTERSECTION[key] = D1[key]
        
print("INTERSECTION:",D_INTERSECTION)
# OUTPUT - INTERSECTION: {'ok': 1}

#SUBTRACTION (D1-D2)
d1 = D1.copy() 
for key in D2:
    if key in d1:
        del d1[key]
        
print("D1-D2:",d1)
# OUTPUT - D1-D2: {'nok': 2}

#MERGE
D_MERGE = {}
for key in D1:
    if key not in D_MERGE:
        D_MERGE[key] = D1[key]
for key in D2:
    if key in D_MERGE:
        D_MERGE[key] += D2[key]
    else:
        D_MERGE[key] = D2[key]
        
print("MERGE:",D_MERGE)
# OUTPUT - MERGE: {'ok': 3, 'nok': 2, 'new': 3}