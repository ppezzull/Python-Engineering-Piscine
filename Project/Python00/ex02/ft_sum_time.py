h = int(input("Insert input: "))
m = int(input("Insert minutes: "))
s = int(input("Insert seconds: "))
if (h < 0 or m < 0 or s < 0):
    seconds = 0
else:
    seconds = (((h * 60) + m) * 60) + s
print(f"Total seconds: {seconds}")
