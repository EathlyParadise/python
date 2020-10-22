<<<<<<< HEAD
# print builtin fuction
print("Hello World") 
print("Hello Python World") 
print("hotfix branch") 
=======
print('%10s%10s%10s' % ('name','age','address'))
print('%-10s%-10s%-10s' % ('name','age','address'))
print('{:10}{:10}{:10}'.format('name','age','address'))
print('{:>10}{:>10}{:>10}'.format('name','age','address'))
print('{:<10}{:<10}{:<10}'.format('name','age','address'))
print('{:^10}{:^10}{:^10}'.format('name','age','address'))
print('{:-^10}{:-^10}{:-^10}'.format('name','age','address'))
# 화폐단위 1000단위 컴머
print('{:,} {:,}'.format(10000,10000))

#IP address 192.168.108.11
a1,a2,a3,a4 = bin(192),bin(168),bin(108),bin(11)
print(a1,a2,a3,a4,sep='.')
#0b11000000.0b10101000.0b01101100.0b00001011

print('{:08b}.{:08b}.{:08b}.{:08b}'.format(192,168,108,11))
# 11000000.10101000.1101100.1011
# 11000000.10101000. 1101100.    1011
# 11000000.10101000.01101100.00001011

print('{4} {5} {0} {1} {2} {3}'.format('The','famine','was','severe','in','Samaria'))
>>>>>>> 96a9963eeae3b7481469268cfd0ede1c5221b0b6
