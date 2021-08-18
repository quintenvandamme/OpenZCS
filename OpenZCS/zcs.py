from .ZSFS import *
import ctypes
import os
import os.path
import random

def Print(INPUT):
    INPUT = INPUT.replace('<Project1 : Application ZCS>', '')
    INPUT = INPUT.replace('</Project1>', '')
    INPUT = INPUT.replace('Print("', '')
    INPUT = INPUT.replace('")', '')
    return INPUT

def MsgBox(Text):
    ctypes.windll.user32.MessageBoxW(0, Text, "ZCS", 1)

def MessageBox(Text,Description):
    ctypes.windll.user32.MessageBoxW(0, Text, Description, 1)

def MakeWindow(Title):
    ctypes.windll.user32.MessageBoxW(0, "", Title, 1)

def InStr(MainString,SecondString):
    if SecondString in MainString:
        print(bool(True))
    else: print(bool(False))

def Replace(MainString,ToFind,ToReplace):
    MainString.replace(ToFind, ToReplace)

def Rnd(Min,Max):
    rnd = random.uniform(Min, Max)
    print (rnd)

def Mid(MainString,FromLeft,FromRight):
    FromLeft = FromLeft - 1
    mid = MainString[FromLeft:-FromRight]
    print(mid)

def Split(MainString,ToSplit,PartNumber):
    if PartNumber == 0:
        n0, n2, n1 = MainString.partition(ToSplit)
        print(n0)
    elif PartNumber == 1:
        n0, n2, n1 = MainString.partition(ToSplit)
        print(n1)
    else: 
        n0, n2, n1 = MainString.partition(ToSplit)
        print(n2)