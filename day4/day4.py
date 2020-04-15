from hashlib import md5

count = 0
while True:
    to_hash = ('bgvyzdsv' + str(count)).encode('ascii')
    hash = md5(to_hash).hexdigest()
    if hash.startswith('000000'):
        break
    count = count + 1
print(count)