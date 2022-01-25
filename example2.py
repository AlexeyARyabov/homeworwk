time = int(input("input time: "))
h = time // 3600
if h < 10:
    h = f"0{h}"
s = time % 3600
m = s // 60
if m < 10:
    m = f"0{m}"
s = s % 60
if s < 10:
    s = f"0{s}"
print(f"time: {h}:{m}:{s}")