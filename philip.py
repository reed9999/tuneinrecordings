#!/usr/bin/python3
import sys
from tuneinrecordingsapp import TuneInRecordingsApp

if __name__ == '__main__':
    app = TuneInRecordingsApp()
    #d = "/home/philip/Music/Tunein/2018-01/2018-01-01/"
    d = sys.argv[1]
    app.go(directory=d, output_file="./thumbnails.html")
