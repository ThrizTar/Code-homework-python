scores = [['John', 50, 45, 28, 48], 
          ['Jane', 48, 36, 23, 50], 
          ['Dave', 39, 49, 55, 23]]
# เต็ม 100 ทุกรอบเอาดีสุด 3 ครั้ง
# เก็บ 15 คะแนน

def cal_score(one_record):
    # ['Dave', 39, 49, 55, 23]

    one_record = one_record[1:]
    total =sum(one_record) - min(one_record)
    # drop = list(map(lambda x : [x[0], sum(x[1:] - min(x[1:]))], scores))
    return 15 * (total/300)

scaled_scores = list(map(lambda x : [x[0], cal_score(x)], scores))
print(scaled_scores)
# print(cal_score(['Dave', 39, 49, 55, 23]))
    