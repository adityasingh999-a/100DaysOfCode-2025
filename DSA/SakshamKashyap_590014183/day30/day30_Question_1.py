def clear_ith_bit(num,k):
    print(num & ~(1<<k))

num = int(input("Enter the number: "))
k = int(input("Enter the ith value: "))

clear_ith_bit(num,k)