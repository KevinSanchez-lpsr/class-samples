def isPrime(my_num):
        for n in range(2,my_num):
                if my_num % n == 0:
                        return False
        return True
print ("this is true")
print (isPrime(11))
print ("this is false")
print (isPrime(10))
list = []
for number in range(2,1001):
        x = isPrime(number)
        if x == True:
                list.append(number)
                myfile = open("primes.txt", "w")
                myfile.write(str(list) + "/n")

print(list)

myfile.close()
