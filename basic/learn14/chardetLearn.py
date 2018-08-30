import urllib.request
rawdata = urllib.request.urlopen('http://www.google.cn/').read()
import chardet
print(chardet.detect(rawdata))