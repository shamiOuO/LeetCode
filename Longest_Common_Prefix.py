# def longestCommonPrefix(strs):
#     Shortest_str = min(strs,key=len)
#     Longest_str = max(strs, key=len)
#
#     # for index, c in enumerate(Shortest_str):
#     #     if c != Longest_str[index]:
#     #         return Shortest_str[:index]
#     # return Shortest_str
#
#
# print(longestCommonPrefix(["flower","flow","flight"]))
strs =["ab","a"]
Prefix = min(strs,key=len)
for str in strs:
    for index,chr in enumerate(str):
        if index < len(Prefix) and chr != Prefix[index]:
            Prefix = Prefix[:index]
print("答案是:"+Prefix)