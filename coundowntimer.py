import time

seconds = int(input("Enter time in seconds: "))

while seconds:
    mins = seconds // 60
    secs = seconds % 60

    timer = f"{mins:02d}:{secs:02d}"

    print(timer)

    time.sleep(1)

    seconds -= 1

print("Time's up!")