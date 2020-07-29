import requests, datetime, time, asyncio
from threading import Thread

proxi = {
    'http': "105.27.237.28:80",
    'https': "105.27.237.28:80"
}

def gen_num(charset, xex, por):
    if xex[0] != 38:
        xex[0] += 1
    else:
        try:
            xex[1] += 1
        except IndexError:
            xex.append(0)
            por += 1
        xex[0] = 0


    for i in range(1, len(xex)):
        # print(i)
        if xex[i] <= 38:
            pass
        else:
            try:
                xex[i+1] += 1
            except IndexError:
                xex.append(0)
                por += 1
            xex[i] = 0
            
    code = ''
    for char_num in xex:
        # print(char_num)
        code += charset[char_num]
    # print (code, xex)

    return code, xex, por
    
    


def request(code):
    data = {'code' : code,
            'item' : '4'}
    try :
        test = requests.get("https://slimehack.com/"+code)
        if test.status_code != 404:
            print("\n|" + code + '|' + str(test.status_code) + "|")
    except TimeoutError:
        pass

thouse = 0
ColRunError = 0
charset = ['.', '+', '=', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'b', 'c', 'd',  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',  'm',  'n', 'o',  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '/']

print(len(charset))

xex = [0]

por = 1
coll = 0

while True:
    code, xex, por = gen_num(charset, xex, por)
    try:
        th = Thread(target=request, args=(str(code),))
        th.start()
        coll += 1
        if coll % 100 == 0:
            thouse += 1
            print("\rHundrid end, all: {}, ColRunError: {}, por: {}".format(str(thouse), str(ColRunError), str(por)), end=" ")
    except RuntimeError:
        time.sleep(10)
        ColRunError += 1
    time.sleep(0.1)
    

        
    
