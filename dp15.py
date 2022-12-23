import time
'''Create a python program capable of greeting you with Good Morning, 
Good Afternoon and Good Evening. Your program should use time module 
to get the current hour

'''
time1=time.strftime('%H')
if 6 <= int(time1) < 12:
    print('good morning')
elif 12 <= int(time1) < 15:
    print('good afternoon')
elif 15 <= int(time1) < 18:
    print('good evening')
else:
    print('good night')
