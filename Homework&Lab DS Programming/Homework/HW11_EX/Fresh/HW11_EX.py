#!/usr/bin/env python3
# @Author: เมธาพร เม้ยกำเนิด
# 631610317
# 11_EX

cat = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''

def main():
    print(cat_altar(2))

def cat_altar(n) :

    cat = [" ／|、    ",
       "(°、。7   ",  
       " |、 ~ヽ  ",
       " ᒐᒐ_f_ )ノ",
       "__________"]
    # for i in cat : print(i,len(i))
    if n==1 : 
        result = "\n".join(cat) 
        return  result
    
    anw=[]
    space1=' '*10
    space2=' '*10
    cindex=0
    out=1
    inn=1

    for l in range(1,6) :
        line=''
        line= space1*(n-out)+' '*(n-out) +cat[cindex] +space1*(n-out)
       # if l == 5 : line= space1*(n-out)+' '*(n-out-1)+'|' +cat[cindex] +'|'+space1*(n-out)
        cindex=(cindex+1) % 5
        # print(line) 
        anw.append(line)
        result = '\n'.join(anw)
    # print(result)
    
    out+=1
    for l in range(6,5*n +1):
        line=''
        line= space1*(n-out)+' '*(n-out) +cat[cindex]+'|'+space2*(inn)+' '*(inn//2*2) +'|'+cat[cindex]+space1*(n-out)
  
        if l%5 ==0 :
            out+=1
            inn+=2
        cindex=(cindex+1) %5
        # print(line)
        anw.append(line)
        ret = '\n'.join(anw)
    return ret

if __name__ == '__main__':
    main()
