import time 

count = 6 
while True:
     if count > 0:
          print(f"Fa Ammo  {count}")
          count -=1
          time.sleep(0.1)
     else:
          count = 6
          print('Reload...')
          time.sleep(2)
          