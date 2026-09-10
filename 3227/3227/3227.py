"""[LEARNING LOGS] ไพ่ 44 ใบ"""
card = input().strip().upper()
last = card[-1]
first = card[:-1]
first_name = {"A" : "ace","J" : "jack","Q" : "queen","K" : "king"}
last_name = {"D" : "diamonds","H" : "hearts","S" : "spades","C" : "clubs"}
rank = first_name.get(first, first)
last_ = last_name[last]
print(f"{rank} of {last_}")
