# -*- coding: UTF-8 -*-
#check python
import sys
if sys.version[0]=='2':
    python2=True
    python3=False
else:
    python2=False
    python3=True

#simple function for testing python
def hello(input):
    output = "Hello" + input + "!"
    print(output)

hello(" World!")

count = 1
if python2:
    title = "Hello Python 2"
else:
    title = "Hello Python 3"
while count <= 7:
    if count == 1:  
        print(title) 
    else:
        print(format(str(count),"s")) #print partice with format and convert type
    count += 1

#List is similar array
list_test=list() #empty list
list_test=[ 1,2,3,4,5,6,7,8]
print (list_test)

#tuple partice //tuple is simple data strcture
tuple_standard = "chaos" , "Iaa421" , 2313
tuple_address = "127.0.0.1" , 80
tuple_name,tuple_Id,tuple_number = tuple_standard #support variable assign using tuple , but tuple can't modify
tuple_host,tuple_port = tuple_address
print ( "%d %d" % (tuple_number,tuple_port)) 
print ("name:%s id:%s" % (tuple_standard[0] , tuple_Id)) # can using '%' to get value for variable
#address[0]="127.0.0.3" will error ,beacuse tuple d

#set partice
test_set=set("Hello")
print(test_set)
partice_set_str = "Hello, it's wonderful day!"
partice_set=set(partice_set_str.split()) 
''' mult-line comment by using triple ' 
string.split can use regular-express by using the command "import re" and "re.split(' |,|.|;',youwannasplitString)"
string.split does not support mutiply token,can use regular-express,and default token is space
'''
print(partice_set)


#dictionary partice
dictionary_test={
    "name":"chaos",
    "Id":"A1702",
    "Salary":6666,
    "tast" :{
        "first":123,
        "second":32458
    }
}
print dictionary_test["name"]
#like json format

#iteration and loop
for n in [1,2,3,4,5,6,7,8]:
    print ("2 to the %d power is %d" % (n,2**n))  # ** represent power calculate
#range to create integer list.In python 2,if range nuber is too large, maybe cousume available memory
#so use xrange to avoid to problem. In python 3 , the xrange() rename range() and old range() has removed.
if python2:
    for n in xrange(100): #xrange() represent on demand when lookup are requested
        print("%d"% (2*n))
else: #python 3
    for n in range(100):
        print("%d"% (2*n))
range_t1 = range (5)      #t1=0,1,2,3,4
range_t2 = range (1,8)    #t2=1,2,3,4,5,6,7  start:1 stop:8
range_t3 = range (0,14,3) #t3=0,3,6,9,12     start:0 stop:14 step:3 
range_t4 = range (8,1,-1) #t4=8,7,6,5,4,3,2  start:8 stop:1  step:-1

for tmp_iter in dictionary_test:
    if(type(dictionary_test[tmp_iter])==dict): #use type function to check type ,maybe write recursive function to print dictionary item
        for tmp_iter2 in dictionary_test[tmp_iter]:
            print(tmp_iter2,dictionary_test[tmp_iter][tmp_iter2])
    print (tmp_iter,dictionary_test[tmp_iter])

#function partice, use "def" to create function.
def calculate_divide(a,b):
    q= a//b #truncation divide,similar to "C program q=a/b" 
    r= a-q*b #r = a mod b ,
    return (q,r) #return muitple variable by tuple
def countdown (x): #generator by use "yield"
    while x>0:
        yield x
        x -= 1
gen_cd_result=countdown(5)
print gen_cd_result.next()
print gen_cd_result
for n in countdown(6):
    print n
'''
generator will genrate an entire sequence of results if it use the yield statment.
"yield" whose behavior like return ,but it doesn't clean frame(**it is the same as call stack in C program language**)
 when you execute generator,it will execute until encounting "yield".
 yield will execute expression which is after "yield". For example ,expression only have a variable ,it will be passed(like return behavior)
 expression would wait for getting object. ex: Q=yield T 
 and generator need an object to accept the results.
 Use object which accept generator's result and Use next() to resume generator process until next yield
 ex: 
    a=countdown(5)
    print a.next() //5, resume countdown frame, will execute x-=1 and countinue while-loop until encounter yield statment
    print a.next() //4
    ....
    for-loop partce using countdown will perform like the example
 '''
#partice" Use yield statment to pass variable/object"
def yield_waitMsg():  #if funciont doesn't have any parameter, it is not to "void". The feature is different with C
    wait_msg="test accept msg "  
    n=0
    while n<3:
        msg =  yield wait_msg
        print("test msg : %s"%msg)
        n+=1

a = yield_waitMsg()
print a.next()
a.send("TEst")
del a
#*****All values used in parogram are object.****
class partice_class_stack(object): #python class inherit by (). the example partice_class_stack is inherit object-class
    @classmethod
    def __init__(self):
        self.stack=[]
    def push(self,object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()
class_test = partice_class_stack()
class_test.push("DIve")
class_test.push(43)

if python2:
    print u"\u2665".encode("utf-8") + u"中文測試 Traceback1 get out\n".encode("utf-8") 
    #default codecs is ascii.Want to print unicode/utf-8 character, should add prefix caharacter 'u' and encode to unicode/utf8
else:
    print ("\u2665"+"trick or treat!") #python 3 default is unicode and prefix character 'u' is unnecessary.

#"type(object) is type" = "isinstance(object,type)"
def re_or_co(a,b):
    if a is b: # re_t1 and re_t2 are the same object
        print "2 reference 1"
    else:
        print "2 copy from 1"
#reference and copy
re_t1=[1,2,[3,4]]
re_t2=re_t1             #reference
re_or_co (re_t1,re_t2)
re_t2=list(re_t1)       #copy
re_or_co (re_t1,re_t2)

re_t2.append(33)
print re_t1 
print re_t2
re_t1[2][1]= 9 
re_t1.append(243)
print re_t1
print re_t2
"""
In python ,a= [1,2,[3,4]].interpreter will create [1,2,[3,4]] list object and assign a to referece to it.
b=list(a) , copy action is create an object "b" to refenece to object to which a reference
a and b will share list [1,2,[3,4]] object.If modify the list object by a or b, it will influence a and b(because they share the same object).
If a or b modify action wouldn't influence the list object referenced , it will not influence another.
If you want to a and b modify action don't affect another completely, you can use deepcopy
""" 
import copy
re_t1=[1,2,[3,4]]
re_t2 = copy.deepcopy(re_t1)
re_t2[2][0]=-100
print re_t1
print re_t2

#first class:
items={
    'name':"Chaos",
    'tect':"Hello world"
}
items["func"]=abs
import math
items["mod"] = math
nums=[12,123,1234]
items["error"] = ValueError
items["append"] = nums.append
print items["func"](-45)
print items["mod"].sqrt(4)
items["append"](15)
print nums
print (type(math))