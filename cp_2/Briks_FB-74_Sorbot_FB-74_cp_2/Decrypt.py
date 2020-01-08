
print('Decrypt')
crp_txt = open('D:/FIELS/CRYPT/LAB2/Crypted_text.txt', 'r', encoding = 'utf-8')
rd = crp_txt.read()

key = "космонавтика"
key *= len(rd) // len(key) + 1
key = key.upper()
msg = ''
for i,j in enumerate(rd):
	save = j.upper()
	if (ord(j) in range(32, 65)):
		msg += j
		continue
	x = ((ord(save) - ord(key[i])) % 32) + ord('А')
	if (j.islower()):
		msg += chr(x).lower()
	elif (j.isupper()):
		msg += chr(x).upper()
	else:
		msg += chr(x)

with open('Decrypted_text.txt', 'w', encoding = 'utf-8') as c:
	c.write(str(msg))
input('Press Enter to exit')  