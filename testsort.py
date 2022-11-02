
try:
    f = open('main.py')
except Exception as e:
    print('False')
    # print (e)
else:
    lines = f.read()

if 'sort' in lines:
    print('False')
else:
    print('True')
