Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> type(3)
<class 'int'>
>>> ballots = 1,341
>>> ballots
(1, 341)
>>> type(ballots)
<class 'tuple'>
>>> number = 73.81
>>> type(number)
<class 'float'>
>>> type("Hello World")
<class 'str'>
>>> type('True')
<class 'str'>
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

>>> counties = ["Arapahoe","Denver","Jefferson"]

>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> counties[0]
'Arapahoe'
>>> counties[2]
'Jefferson'
>>> print(counties[-1])
Jefferson
>>> len(counties)
3
>>> counties[1:]
['Denver', 'Jefferson']
>>> counties[1:3]
['Denver', 'Jefferson']
>>> counties.append("El Paso")
>>> counties
['Arapahoe', 'Denver', 'Jefferson', 'El Paso']
>>> counties.insert(2,"El Paso")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.pop("El Paso")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    counties.pop("El Paso")
TypeError: 'str' object cannot be interpreted as an integer
>>> counties.pop(3)
'Jefferson'
>>> counties.insert(3,"Jefferson")
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson', 'El Paso']
>>> counties.pop(-1)
'El Paso'
>>> counties.pop[-1]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    counties.pop[-1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> counties
['Arapahoe', 'Denver', 'El Paso', 'Jefferson']
>>> counties.pop(-2)
'El Paso'
>>> counties[2] = 'El Paso'
>>> countie
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    countie
NameError: name 'countie' is not defined
>>> counties
['Arapahoe', 'Denver', 'El Paso']
>>> counties.insert(1,"El Paso")
>>> counties.remove("Arapahoe")
>>> counties
['El Paso', 'Denver', 'El Paso']
>>> counties = ['Arapahoe','Denver','Jefferson']
>>> counties
['Arapahoe', 'Denver', 'Jefferson']
>>> my_tuple = ()
>>> counties_tuple = ('Arapahoe', 'Denver', 'Jefferson')
>>> len(counties_tuple)
3
>>> counties_tuple[1]
'Denver'
>>> counties_tuple[:-2]
('Arapahoe',)
>>> counties_tuple[:-
	       ]
SyntaxError: invalid syntax
>>> counties_tuple[:-1]
('Arapahoe', 'Denver')
>>> counties_tuple[:2]
('Arapahoe', 'Denver')
>>> counties_tuple[1:2]
('Denver',)
>>> counties_dict = {}
>>> counties_dict
{}
>>> counties_dict["Arapahoe"] = 422829
>>> counties_dict
{'Arapahoe': 422829}
>>> counties_dict['Denver'] = 463353
>>> counties_dict['Jefferson'] = 432438
>>> counties_dict
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
>>> counties_dict.items()
dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])
>>> counties_dict.keys()
dict_keys(['Arapahoe', 'Denver', 'Jefferson'])
>>> counties_dict.values()
dict_values([422829, 463353, 432438])
>>> counties_dict.get('Denver')
463353
>>> 
KeyboardInterrupt
counties_dict
>>> counties_dict['Arapahoe']
422829
>>> print(counties_dict['Arapahoe'])
422829
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters":422829})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}]
>>> voting_data.append({"county":"Denver", "registered_voters":463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters":432438})
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> 
>>> voting_data.insert(1,({"county":"El Paso", "registered_voters":461149}))
>>> voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> voting_data.remove({'county': 'Arapahoe', 'registered_voters': 422829})
>>> voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
>>> #What is the score?
>>> 
>>> Score = int(input("What is your test score?"))
What is your test score?
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    Score = int(input("What is your test score?"))
ValueError: invalid literal for int() with base 10: ''
>>> numbers = [0,1,2,3,4]

for num in numbers:
    print(num)
    
SyntaxError: multiple statements found while compiling a single statement
>>> counties_tuple = ("Arapahoe","Denver","Jefferson")

for i in range(len(counties_tuple)):
    print(counties_tuple[i])
    
SyntaxError: multiple statements found while compiling a single statement
>>> counties_tuple = ("Arapahoe","Denver","Jefferson")

for i in (len(counties_tuple)):
    print(counties_tuple[i])
    
SyntaxError: multiple statements found while compiling a single statement
>>> 