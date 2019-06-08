import os
import subprocess

def fileRead(fileName):
    defaultInputFront = 'python3 ./classify-hangul.py ../'
    defaultInputBack = ' --label-file ../labels/2350-common-hangul.txt'
    defaultInput = defaultInputFront + fileName + defaultInputBack
    result = subprocess.check_output(defaultInput, shell=True)
    splitResult = result.split()
    letter = splitResult[3].decode('utf-8')

    return letter