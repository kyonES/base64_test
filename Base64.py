base64_table = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e",
                "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]
s=input()
codepoints=[]
for c in s:
    codepoint=ord(c)
    codepoints.append(codepoint)
part6s=[]
i=0
base64=""
while i < len(codepoints)*8:
    #何バイト目を見るか
    a=i//8
    #aを何ビットスキップして見るか
    b=i%8
    x=codepoints[a]
    #最初のバイトの値
    first=((63<<2>>b)&255&x)<<b>>2
    if b>2 and a<len(codepoints)-1:
        c=a+1
        #次のバイトから何ビットとるか
        d=b-2
        y=codepoints[c]
        second=((((1<<d)-1)<<(8-d))&y)>>(8-d)
    else:
        second=0
    result=first|second
    base64+=base64_table[result]
    i+=6
print(base64)
