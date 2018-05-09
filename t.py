import win32com.client


speak = win32com.client.Dispatch('SAPI.SPVOICE')

x = input("请输入中文：")

speak.Speak(x)


import winsound
winsound.Beep(1000, 1000)
