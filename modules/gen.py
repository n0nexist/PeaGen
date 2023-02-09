from random import randint
from rich import print
import datetime

card_types = ["americanexpress","visa13", "visa16","mastercard","discover"]

def generate_card(type,cardlenght=None):
    
    def prefill(t):
        def_length = 16
        if t == card_types[0]:
            return [3, randint(4,7)], 13
        elif t == card_types[1] or t == card_types[2]:
            if t.endswith("16"):
                return [4], def_length - 1
            else:
                return [4], 12
        elif t == card_types[3]:
            return [5, randint(1,5)], def_length - 2
        elif t == card_types[4]:
            return [6, 0, 1, 1], def_length - 4
        else:
            return [], def_length
    def finalize(nums):
        check_sum = 0
        check_offset = (len(nums) + 1) % 2
        for i, n in enumerate(nums):
            if (i + check_offset) % 2 == 0:
                n_ = n*2
                check_sum += n_ -9 if n_ > 9 else n_
            else:
                check_sum += n
        return nums + [10 - (check_sum % 10) ]

    try:
        t = type.lower()
    except:
        pass

    if t in card_types:
        initial, rem = prefill(t)
    else:
        try:
            t = int(t)
        except:
            print("[ERROR] invalid bin/card type")
            exit()
        
        initial = [int(x) for x in str(t)]    
        rem = cardlenght-len(initial)

    so_far = initial + [randint(1,9) for x in range(rem - 1)]
    returnme = str(int("".join(map(str,finalize(so_far)))))    

    return returnme


def gendata(data):
    if data == "year":
        d = str(datetime.datetime.now().year+randint(3, 5))
    elif data == "month":
        d = str(randint(1, 12))
        if len(d) == 1:
            d = ("0"+str(d))
    else:
        d = str(randint(111, 999))

    return d