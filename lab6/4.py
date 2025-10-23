import time
number_to_test = int(input("give number: "))
delay = int(input("give delay in ms: "))
delay_sec = delay/1000
time.sleep(delay_sec)
root = number_to_test**0.5

print(root)
