dic = {"I": 1,  "V": 5,  "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = 'LVIII'
ans =0
i = 0
while i < len(s):
       if i + 1< len(s) and dic[s[i]] < dic[s[i+1]]:
              ans += dic[s[i+1]]- dic[s[i]]
              i += 2
       else:
              ans += dic[s[i]]
              i +=1
print(ans)