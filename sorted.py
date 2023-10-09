def reverse_sort_dictionary(dict):
    key = list(dict.keys())
    key.sort()
    ans = []
    for i in range (len(key)-1,-1,-1):
        ans.add("(" + key[i] + ","+ dict[key][0] + ")")
        
    return ans
