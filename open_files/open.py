import io

with open('BDNewsToday.png', 'rb') as f:
    jpgdata = f.read()

print(jpgdata)

if jpgdata.startswith(b'\x89PNG\r'):
    text = u'This is a png file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))


