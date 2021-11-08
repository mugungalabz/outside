import hashlib
str = "NOLSrolingthraotNOLS'sbenaeth"
print(hashlib.md5(str.encode('utf-8')).hexdigest())
