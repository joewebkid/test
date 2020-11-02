# import simplecrypt
#
# with open('C:\Python\maya\encrypted.bin', 'rb') as fo:
#     ciphertext = fo.read()
#     with open('C:\Python\maya\passwords.txt') as fin:
#         for line in fin:
#             line = line.replace('\n', '')
#             try:
#                 dec = simplecrypt.decrypt(line, ciphertext)
#             except simplecrypt.DecryptionException:
#                 pass
#             else:
#                 print(line, dec)
#                 with open('C:\Python\maya\crypted.bin', 'wb') as fo:
#                     fo.write(dec)
#             # print("decrypted text: %s" % dec)
# #---------------------------------
# import requests
# from simplecrypt import decrypt, DecryptionException
#
# code = requests.get('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
# passes = requests.get('https://stepic.org/media/attachments/lesson/24466/passwords.txt').content
#
# for p in passes.split():
#     try:
#         s = decrypt(p, code)
#     except DecryptionException:
#         pass
#     else:
#         print(p, s)
#====================================================
import itertools

# itertools.takewhile(func, iterable) #возвращает элементы до тех пор, пока func возвращает истину.
def primes():
    i = 2
    while True:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
                yield i
        i+=1

print(list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))

print(list(itertools.takewhile(lambda x : x <= 31, primes())))


# n = input("n=")
# lst = []
# for i in xrange(2, n+1):
#     for j in xrange(2, i):
#         if i % j == 0:
#             # если делитель найден, число не простое.
#             break
#     else:
#         lst.append(i)
# print lst
