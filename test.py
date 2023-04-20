# nums = [9,6,4,2,3,5,7,0,1]

# n = len(nums)

# print((n*(n+1)//2)-sum(nums))

# nums = [4,3,2,7,8,2,3,1]
# nums = [2,3,3,4,5]

# sorted_nums = sorted(nums)
# # print(nums)
# res = {k:v for k,v in enumerate(sorted_nums, 1)}
# print(res)

# i = 0
# pos = nums[i] - 1
# print(nums[i])
# print(nums[pos])


# nums = [4,3,2,7,8,2,3,1]

# full = [i for i in range(1,len(nums)+1)]

# print(list(set(full) - set(nums)))
# i = 0

# while i<len(nums):
#     pos = nums[i] - 1
#     if nums[i]!=nums[pos]:
#         nums[i], nums[pos] = nums[pos], nums[i]
#     else:
#         i+=1
# # print(nums)

# res = []

# for i in range(len(nums)):
#     if nums[i] != i+1:
#         res.append(i+1)
# print(res)


# nums = [2,2,1]

# res = 0

# for num in nums:
#     res ^= num

# print(res)


# prices = [7,1,5,3,6,4]

# # 5

# current_price = prices[0]
# min_price = prices[0]
# max_price = prices[0]


# for i in prices:
#     if i<current_price:
#         min_price = i
#     else:
#         max_price = i
#     current_price = i
# print(min_price)
# print(max_price)

# prices = [7,1,5,3,6,4]

# max_profit = 0
# min_price = prices[0]

# for i in range(1, len(prices)):
#     price = prices[i]
#     max_profit = max(max_profit, price - min_price)
#     min_price = min(min_price, price)

# print(max_profit)



# def func(prices):
#     buy = prices[0]
#     profit = 0
#     for i in prices[1:]:
#         if i - buy > 0:
#             profit = max(profit, i - buy)
#         else:
#             buy = i
#     return profit

# print(func(prices))


# dict_ = {'Bootcamp': 8, 'Makers': 8, 'coding': 6, 'hello': 5}


# nums = [-1,0,3,5,9,12]

# target = 9

# if target in nums:
#     return nums.index(target)
# else:
#     return -1

# nums = [2,7,11,15]
# target = 9

# dict1 = {}

# for i, num in enumerate(nums):
#     res = target - nums[i]
#     l = []
#     if res in dict1:
#         l.append(dict1[res])
#         l.append(i)
#         print(l)
#     else:
#         dict1[num] = i

# print(dict1)


# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = sorted(dict_.items(), key=lambda x:x[-1])

# print(dict(sorted_dict))

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}

# print(robert.intersection(kail).intersection(merri))


# l = ['r', 'a', 't', 'A']
# # print(ord(''))
# l.sort()
# print(l)

# letters = ["c","f","j"]
# target = "a"
# # print(ord(target))

# nums = []

# for l in letters:
#     nums.append(ord(l))

# for i in range(len(nums)):
    



# nums = [1,1,4,4,5]

# res = 0

# for num in nums:
#     res^=num

# print(res)


# nums = [1,2,1,3,2,5]
# sett = set(nums)
# for i in sett.copy():
#     if i in nums and nums.count(i)>1:
#         sett.remove(i)
# print(list(sett))

# nums = [2,2,3,2]


# print((sum(set(nums))*3 - sum(nums))//2)
# print(set(nums))
# print(sum(set(nums))*3)
# print(sum(nums))



# Let the numbers be x,y,z,.....
# require sum should be 3x+3y+3z
# original sum = 3x+3y+z
# Subtract require sum from original sum
# (3x+3y+3z) - (3x+3y-z) = 2z
# div the ans by 2 = 2z/2 = z--> our ans


# sett = set(nums)
# for i in sett.copy():
#     if i in nums and nums.count(i)>1:
#         sett.remove(i)
# print(list(sett)[0])

# l = {i:nums.count(i) for i in nums}

# for k,v in l.items():
#     if v == 1:
#         return k

# dict1 = {}

# for num in nums:
#     if num in dict1:
#         dict1[num] += 1
#     else:
#         dict1[num] = 1

# for k,v in dict1:
#     if v == 1:
#         return v



# letters = ["x","x","y","y"]

# target = "z"

# print('a'<'c')

# print(ord('a'), ord('c'))

# for i in letters:
#     if target>i:
#         print('yes')

# left = 0
# right = len(letters)


# while left<right:
#     # mid = left+right//2
#     mid = left+(right-left)//2
#     if letters[mid]<=target:
#         left = mid + 1
#     else:
#         right = mid

# print(letters[left%len(letters)])
# print(left, right, mid)


# s = "ab#c"
# t = "ad#c"

# s = "ab##"
# t = "c#d#"


# def func(s):
#     l = []
#     for i in s:
#         if i!='#':
#             l.append(i)
#         elif l:
#             l.pop()

#     return "".join(l)

# print(func(s) == func(t))
# print(l)

# for i in range(len(s)):
#     if s[i] == '#':
#         s = s[:i-1]+s[i+1:]

# for i in range(len(t)):
#     if t[i] == '#':
#         t = t[:i-1]+t[i+1:]

# print(s1 == t1)
# print(s, t)



# s = "pwwkew"
# s = "bbbbb"
# s = "abcabcbb"

# def func(s):
#     sub = ''
#     res = ''
#     for i in s:
#         if i not in sub:
#             sub += i
#         else:
#             if len(res) <= len(sub):
#                 res = sub
#             sub = sub.split(i)[-1] + i
#     return max(len(res), len(sub))

# print(func(s))



# from collections import Counter
# chars = Counter()

# left = right = 0
# res = 0

# while right<len(s):
#     r = s[right]
#     chars[r] += 1
#     # print(chars)
#     while chars[r]>1:
#         l = s[left]
#         chars[l] -= 1
#         left += 1
    
#     res = max(res, right - left + 1)

#     right += 1
# print(res)


# for i in s:


# l = []

# for i in list(s):
#     l.append(ord(i))

# print(l)

# ll = []

# for i in range(len(l)):
#     if l[i]+1 == l[i+1]:
#         ll.append(l[i])
# print(ll)

# i = 0

# while i<len(l)-1:
#     j = 0
#     while j<len(l)-i-1:
#         if l[j]>l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
#         j+=1
#     i+=1
# print(l)


# intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
# intervals.sort(key=lambda x:x[0])
# res = []

# for i in intervals:
#     if not res or res[-1][-1]<i[0]:
#         res.append(i)
#     else:
#         res[-1][-1] = max(res[-1][-1], i[-1])

# print(res)

# n = 11111111111111111111111111111101
# print(bin(n))

# n = '00000010100101000001111010011100'

# num = 43261596

# print(bin(num)[::-1])


# res = ''
# reversed = str(bin(n))[::-1]
# print(reversed)
# print(reversed[:-2])
# if reversed[0] == 0:
#     res+=reversed[:-2]
#     return int(res[::-1]+'000000', 2)
# else:
#     return int(reversed[:-2], 2)



# reversed = str(int(bin(n)))[::-1]


# balance = 400

# def spent(target, spend):
#     global balance
#     dict1 = {}

#     if balance < spend:
#         print('Недостаточно средств на балансе')
#     else:
#         dict1['target'] = target
#         dict1['spend'] = spend
#         balance -= spend
#         return dict1

# def deposit(amount):
#     global balance 
#     balance+=amount
#     return balance

# print(spent('prod', 400))
# print(deposit(500))


# balance = 0
# def spent(item, amount, balance):
#     l = {}
#     if amount <= balance:
#         l.update({'target': item, 'spend': amount})
#         balance -= amount
#         return l, balance
#     else:
#         return 'Недостаточно средств'

# def deposit(amount: int, balance):
#     balance += amount
#     return balance

# print(spent('prod', 400, 0))
# print(deposit(500, 0))


# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
  
#     def bar():
#         global var
#         var = 'переменная bar'
        
 
#     bar()
# foo()
# print('переменная в foo: ', var)
# def longest_word(filename:str):
#     with open(filename) as file:
#         words = file.read().split()

#     words.sort(key=len, reverse=True)

#     max_len = len(words[0])

#     for word in words:
#         if len(word) == max_len:
#             print(word)

# class A:
#     ...

# class B:
#     ...

# class D(A,B):
#     ...

# class E(B,A):
#     ...

# class F(D,E):
#     ...




# stroka = 'SLOVO'
# stroka2 = 'SLED_SLOVO'
# znak = '\n'


# print(f"{stroka}{znak}{stroka2}{znak}{stroka}")



# for obj in objects:
#     # print(obj.name)

#     # 'fly' in dir(obj) == hasattr(obj, 'fly')
#     attrs = ['fly', 'swim', 'walk', 'talk']
#     for attr in attrs:
#         if hasattr(obj, attr):
#             # attr = 'fly'
#             # getattr(obj, attr) == obj.fly
#             method = getattr(obj, attr)
#             method()

# obj = Human()

# a = getattr(obj, 'walk')
# a()

# getattr(obj, 'walk')()


# import datetime
# print(datetime.datetime.now().strftime('%H:%M:%S'))



#1

# class Product:
#     base_price = 20000

#     def __init__(self, model, year, color):
#         self.m = model
#         self.y = year
#         self.c = color
    
#     def has_garantiya(self, val):
#         if (val - self.y)>2:
#             return "Ваша гарантия истекла"
#         else:
#             return "Гарантия действительна"
    
#     @classmethod
#     def change_price(cls, rate):
#         cls.base_price += cls.base_price * rate/100
    
# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price) 

# 5

# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount
    
#     @staticmethod
#     def dollarize(float_num):
#         if float_num>0:
#             return f"${float_num:,.2f}"
#         else:
#             return "-${:,.2f}".format(-float_num)

#     def update(self, value):
#         self.amount = value
    
#     def __repr__(self):
#         return str(self.amount)

#     def __str__(self):
#         return self.dollarize(self.amount)

# cash = MoneyFmt(12345678.021) 
# print(cash) 
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash))


# nums = [1,2,3,4,5,6,7]
# k = 3

# # Output: [5,6,7,1,2,3,4]

# # return nums[-k:]+nums[:-k]
# cp = nums.copy()

# for res, i in zip(range(-k,k+1), range(len(nums))):
#     nums[i] = cp[res]

# print(nums)
    

# nums = [1,2]
# nums = [1,2,3,4,5,6,7]
# k = 3

# cp = nums.copy()

# for i in range(k):
#     nums.insert(0, nums[-1])
#     nums.pop()

# print(nums)


nums1 = [1,2,2,1]
nums2 = [2,2]


set1 = set(nums1)
hm = []

for num in nums2:
    if num in set1:
        hm.append(num)
        set1.remove(num)

# print(hm)

def intersection(nums1, nums2):
    set1 = set(nums1)
    result = []
    for num in nums2:
        if num in set1:
            result.append(num)
            set1.remove(num)
    return result

# print(intersection([1,2,2,1], [2,2]))

def intersection2(nums1, nums2):
    dict1 = {}
    dict2 = {}
    result = []
    for num in nums1:
        dict1[num] = dict1.get(num, 0) + 1
    for num in nums2:
        dict2[num] = dict2.get(num, 0) + 1
    for key in dict1:
        if key in dict2:
            result += [key] * min(dict1[key], dict2[key])
    return result

# print(intersection2([1,2,2,1], [2,2]))

# nums1 = [1,2,2,1]
# nums2 = [2,2]

# dict1 = {}
# dict2 = {}
# res = []

# for num in nums1:
#     dict1[num] = nums1.count(num)
# for num in nums2:
#     dict2[num] = nums2.count(num)

# for key in dict1:
#     if key in dict2:
#         res+=[key]*min(dict1[key],dict2[key])
# print(res)


# nums1 = [1,2,2,1]
# nums2 = [2,2]

# nums1.sort()
# nums2.sort()
# i = j = 0
# result = []
# while i < len(nums1) and j < len(nums2):
#     if nums1[i] == nums2[j]:
#         if not result or nums1[i] != result[-1]:
#             result.append(nums1[i])
#         i += 1
#         j += 1
#     elif nums1[i] < nums2[j]:
#         i += 1
#     else:
#         j += 1

# print(result)


# nums1.sort()
# nums2.sort()
# i = j = 0
# result = []
# last_added = None
# while i < len(nums1) and j < len(nums2):
#     if nums1[i] == nums2[j]:
#         if nums1[i] != last_added:
#             result.append(nums1[i])
#             last_added = nums1[i]
#         i += 1
#         j += 1
#     elif nums1[i] < nums2[j]:
#         i += 1
#     else:
#         j += 1

# nums1 = [1,2,2,1]
# nums2 = [2,2]

# seen = {}
# result = []

# for num in nums1:
#     if num not in seen:
#         seen[num] = 0
#     seen[num]+=1

# for num in nums2:
#     if num in seen and seen[num]>0:
#         result.append(num)
#         seen[num]-=1

# print(result)


s = "The_Stealth-Warrior"
l = []
if '-' in s and '_' in s:
    s = s.split('-')
    for i in s:
        l.append(i.split('_'))
# print(l)
# ss = s.split('-')

# res = ''
# for c in ss:
#     res+=c.title()
# print(res)



import re


text = "The_Stealth-Warrior"

list1 = [x for x in text]
# print(list(text))

# for i in range(len(list1)):
#     if list1[i] in ('_', '-'):
#         list1[i+1] = list1[i+1].upper()
# return ''.join([i for i in list1 if i not in ('-', '_')])

# Check if input text is empty
# if not text:
#     return ""

# Split the text into words based on dashes or underscores
# words = re.split(r'[-_]', text)
# print(words)

# Capitalize the first word if it was originally capitalized
# if words[0][0].isupper():
#     words[0] = words[0][0] + words[0][1:].lower()

# Capitalize the first letter of each subsequent word
# for i in range(1, len(words)):
#     words[i] = words[i][0].upper() + words[i][1:].lower()

# Join the words together and return the result
# return "".join(words)

# print(to_camel_case("The_Stealth-Warrior"))


# text = 'the_stealth_warrior'
# print(text[:1]+text.title()[1:].replace('_',''))



# data = [[32, 5], [56, 20]]
# res = ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

# print(res)

# lst = [1, 0, 1, 2, 0, 1, 3]
lst = [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
"""
lst = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lst = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
# list1 = lst.copy()

# for i in list1:
#     if i == 0:
#         lst.pop(lst.index(i))
#         lst.append(0)
# print(lst)

# lst = [9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]
# lst = [0]

# for i, v in enumerate(lst):
#     if v == 0:
#         lst.pop(i)
#         lst.append(0)
# print(lst)

# count = 0
# for i, v in enumerate(lst):
#     if v == 0:
#         lst[i] = None
#         count+=1
# for i in range(count):
#     lst.append(0)

# print([i for i in lst if i is not None])


# nums = [4,3,0,4,0,2,1]

# i = 0

# for j in range(len(nums)):
#     if nums[j]!=0:
#         nums[i], nums[j] = nums[j], nums[i]
#         i+=1
# print(nums)

# number = int(''.join([str(i) for i in digits])) + 1
# return [int(i) for i in str(number)]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

res = []
matrix.reverse()
# print(matrix)

for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         print(matrix)
# print(matrix)
# reversed_list = list(reversed(matrix))
# print(reversed_list)
# while len(res) != len(matrix):
#     for i in range(len(reversed_list)):
#         res.append(reversed_list[i][i])
# print(res)

# x = 1534236469
# # print(x.bit_length())
# # print(int(str(x)[::-1]))
# res = int(str(abs(x))[::-1])
# if res.bit_length()<32:
#     if x>0: 
#         print(res) 
#     else: 
#         print(-res)
# print(0)

# s = "A man, a plan, a canal: Panama"
# "0P"

# l = ''.join([i.lower() for i in s if i.isalpha() or i.isdigit()])
# return l==l

# haystack = "sadbutsad"
# needle = "sad"

# if needle in haystack:
#     return haystack.find(needle)
# else:
#     return -1

# strs = ["flower","flow","flight"]
# strs = ['cir', 'car']

# res = ''

# for i in zip(*strs):
#     if len(set(i)) == 1:
#         res += i[0]
#     else:
#         print(res)

# l = ''.join([i[0] for i in zip(*strs) if len(set(i))==1])
# print(l)
# print(res)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# n1 = nums1[:m]
# n2 = nums2[:n]

# nums1.clear()
# nums1.extend(n1+n2)
# # nums1.extend(n2)
# nums1.sort()
# print(nums1)

"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

# nums = [-2,1,-3,4,-1,2,1,-5,4]

# for num in nums:
#     if num>0:
#         for i in range(nums.index(num), len(nums)):

"""
nums = [1,2,3,1]
Output: 4

nums = [2,7,9,3,1]
Output: 12
"""

# nums = [1,2,3,1]
# nums = [2,7,9,3,1]
# nums = [1,2]
# nums = [2,1,1,2]

# nums = [0]*3+nums

# nums = [0,0,0,2,1,1,2]

# for i in range(3, len(nums)):
#     house1 = nums[i-3]+nums[i]
#     house2 = nums[i-2]+nums[i]
#     nums[i] = max(house1, house2)

# print(max(nums))


# profit = 0
# for i in range(0, len(nums), 2):
#     profit+=nums[i]

# profit2 = 0
# for i in range(1, len(nums), 2):
#     profit2+=nums[i]

# if profit>profit2:
#     print(profit)
# else:
#     print(profit2)

# print(profit)


"""
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""

# n = 15

# res = []

# for i in range(1, n+1):
#     if not i%3 and not i%5:
#         res.append("FizzBuzz")
#     elif not i%3:
#         res.append("Fizz")
#     elif not i%5:
#         res.append("Buzz")
#     else:
#         res.append(str(i))

# print(res)


# n = 10

# count=0

# if n == 1:
#     return 0

# if n>=2:
#     count+=1


# for i in range(3,n+1):
#     a = int(i**0.5)
#     for j in range(2,a+1):
#         if i%j==0:
#             count+=1
# print(count)



# print((0.1+0.1+0.1))
# print(0.1+0.1+0.1+0.1)

# from decimal import Decimal

# print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))


# class A:
#     name = 'John'
#     last_name = 'Snow'

#     def __str__(self):
#         return self.last_name
    
#     def __repr__(self):
#         return self.name
    

# a = A()

# print(a)


# MyClass = type('MyClass',(), {'attr': 'cls attr'})

# obj = MyClass()

# print(obj)

# class MyClass:
#     attr = 'cls attr'

# obj = MyClass()



# list1 = [1,2,3,4,5]

# def func(lst):
#     for i in list1:
#         yield i

def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib_iter = fibonacci()
for i in range(10):
    print(next(fib_iter))

# for i in range(10):
#     print(next(fib_iter))