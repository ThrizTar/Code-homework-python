#!/usr/bin/env python
# @Author: kk
# @Last Modified time: 2022-09-24 21:16:41

cat = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''



def main():
    print(cat_altar(int(input())))

def cat_altar(n):
    keep_cat = []
    list_cat_up = []
    list_cat_down = []
    se = 1

    # Loop for create cat altar n times
    for i in range(1, n+1):

        # set top of on the altar
        if i == 1:
            space_0 = " " * ((n-1) * 11)
            cat = \
    ''' ／|、    
(°、。7   
 |、 ~ヽ  
 ᒐᒐ_f_ )ノ
__________
'''
            list_cat_top = cat.split("\n")
            keep_cat += list(map(lambda x : space_0 + x , list_cat_top[:-1]))

        # set up and down step
        else:

            # step up
            space_1 = " " * ((n-i) * 11)
            cat_up = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''
            list_cat_up = cat_up.split("\n")
            list_cat_up = list_cat_up[:-1]

            # step down
            cat_down = \
    '''| ／|、    
|(°、。7   
| |、 ~ヽ  
| ᒐᒐ_f_ )ノ
|__________
'''
            list_cat_down = cat_down.split("\n")
            list_cat_down = list_cat_down[:-1]

            # zip for prepare to used
            top_down_cat = zip(list_cat_up, list_cat_down)
            list_top_down_cat = list(top_down_cat)

            # combine all of the cat on the altar
            keep_cat += list(map(lambda x :space_1 + (x[0] + " "*(((se)*10)) + x[1]) if se ==  1 else space_1 + (x[0] + " "*(((se)*11)-1) + x[1]) ,list_top_down_cat))
            se += 2

            # return result
        result = "\n".join(keep_cat)
    return result

if __name__ == '__main__':
    main()
