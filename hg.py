import os
import tkinter as tk
re = os.getcwd()
print(re)

win = tk.Tk()
win.title('Shutdown_Timer')
win.geometry('200x200')

titel = tk.Label(win,text='定时关机')
titel.pack()

titel_2 = tk.Label(win,text='输入分钟后关机')
titel_2.pack()

e = tk.Entry(win,show=None)
e.pack()

def shutdown():
    var = e.get()
    n_min = int(var)
    n_sec = n_min*60
    os.system("shutdown -a")
    os.system("shutdown -s -t %d" % (n_sec))
    print('将在%d秒后关机' %(n_sec))

def shutdown_cancel():
    os.system("shutdown -a")
    

b_shutdown = tk.Button(text='Shutdown',command=shutdown)
b_shutdown.pack()

b_cancel = tk.Button(text='Cancel',command=shutdown_cancel)
b_cancel.pack()
# t = tk.Text(win,height=2)
# t.pack()



win.mainloop()

# #分钟转秒函数
# def m2s(min):
#     min = int(min)
#     sec = min*60
#     return(sec)

# print(e)
# # min_input = input("定时关机时间_min:")
# min_input = int(min_input)
# print(m2s(min_input))

# os.system("shutdown -s -t %d" % (m2s(min_input)))