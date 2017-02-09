import time

#get the current time
cur_time = time.time()


#floor divide current time by number of seconds in a day
days_since_epoch = cur_time // (86400)

print('Days since epoch: ')
print(days_since_epoch)

today = cur_time - (days_since_epoch*86400)

print (today)
print((today / 60)/60)
