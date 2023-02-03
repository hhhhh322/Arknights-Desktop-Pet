from json import load,dumps

def ChekPoint(Name):
    with open('./Favorability.json', 'r+', encoding='utf-8') as f:
        data = load(f)
        try:
            return int(data[Name])
        except:
            print('None')

def ChekIn(name: str, args: int):
    with open('./Favorability.json', 'r+', encoding='utf-8') as f1:
        data = load(f1)
        f1.seek(0)
        f1.truncate()
        data[name] = args
        data1 = dumps(data)
        f1.write(data1)

