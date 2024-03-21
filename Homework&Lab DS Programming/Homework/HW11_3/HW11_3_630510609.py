#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW11_3
# 229223 Sec 002

def main():
    # print(words_to_num("one hundred eleven "))  
    test_words_to_num()

def words_to_num(words):
    dict_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,  "nineteen": 19  ,
                "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
    result = 0
    keep = 0
    billion = 0
    million = 0
    thousand = 0

    if words in dict_num:
        result = dict_num[words]
    else:
        if "-" in words:
            words = words.replace("-"," ")
        list_words = words.split()

        for i in list_words:
            if i == "billion":
                billion = keep * (10**9)
                keep = 0
            elif i == "million":
                million = keep * (10**6) 
                keep = 0
            elif i == "thousand":
                thousand = keep * (10**3)
                keep = 0
            # elif i == "hundred":
            #     hundred = keep * (10**2)
            #     keep = 0
            else: # i in dict_num:
                if i == "hundred":
                    keep *= 100
                else:
                    keep += dict_num[i]
        result = billion + million + thousand + keep
    return result

def test_words_to_num():
    assert words_to_num("fourteen") == 14 
    assert words_to_num("two hundred forty-eight ") == 248
    assert words_to_num("one hundred eleven ") == 111
    assert words_to_num("forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two") == 42641323862
    assert words_to_num("one billion one million ") == 1001000000
    print("All OK!!!!")

if __name__ == "__main__":
    main()

