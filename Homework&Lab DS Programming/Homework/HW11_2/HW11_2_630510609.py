#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW11_2
# 229223 Sec 002

def main():
    runner_up()

def runner_up():
    # input total student
    total = int(input())
    runner_ = 0
    sum_ = 0

    # find max and runner up
    for i in range(total):
        current_score = float(input())
        if i == 0:
            max_ = current_score
        else:
            if(current_score > max_):
                runner_ = max_
                max_ = current_score
            else:
                if(current_score > runner_ and current_score != max_):
                    runner_ = current_score
        sum_ += current_score
    averrage = sum_ / total
    
    # everyone have a same score
    if averrage == current_score:
        runner_ = None

    
    print("---")
    print("Max score is: %.2f" %max_)
    if runner_ != None:
        print("Runner up is: %.2f" %runner_)
    else:
        print("Runner up is:",runner_)
    print("Averrage is: %.2f" %averrage)

if __name__ == "__main__":
    main()