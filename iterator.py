# iterable means the object can be looped over. Something is iterable doesnt means that it is iterator
# an iterator is an object with the state which remembers where it is at during iteration and it fetched nextvalue using __next__ method



class Sentence:
    def __init__(self, sentenc):
        self.sentenc= sentenc
        self.index= 0
        self.words= self.sentenc.split()

    def  __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index= self.index
        self.index+=1
        return self.words[index]

sentence= "This is a great idea"

obj1= Sentence(sentence)
# for i in obj1:
#     print(i)
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))




"""

ids= [1,2,3,4,5]

# for id in ids:
#     print(id)
#     print(dir(id))
#     break
# print("*"*100)
# print(dir(ids))
# print("*"*100)

nums= ids.__iter__()
# nums= iter(ids)
# print("*"*100)
# print(nums)
# print("*"*100)
# print(dir(nums))
# print("*"*100)
# print(nums.__next__())
# print("#"*100)
# print(iter(nums))

# print(next(iter(ids)))
# print(next(iter(ids)))
# print(next(iter(ids)))
# print(next(iter(ids)))

print(next(nums))
print(next(nums))
print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
print("*"*100)

# print(ids.__iter__().__next__())
# print(ids.__iter__().__next__())


class Myrange:
    def __init__(self, start, end):
        self.value= start
        self.end= end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        
        current= self.value
        self.value+=1
        return current
    

def myrange(start, end):
    current= start
    while current<end:
        yield current
        current+=1


num= myrange(3,9)
for n in num:
    print(n)"""
"""
test= Myrange(1,10)

# for num in test:
#     print(num)
print(next(test))
print(next(test))
print(next(test))"""