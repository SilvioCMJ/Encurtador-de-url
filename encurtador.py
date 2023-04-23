import pyshorteners

url = "exemplo.com.br"

p = pyshorteners.Shortener()

#encurtando
short = p.tinyurl.short(url)

#resultado
print(short)