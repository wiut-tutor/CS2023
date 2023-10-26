student = {'name':'lola',
            'age': 19,
           'course':'BIS'}
print(student)

student2 = dict()

print(student2)
student2['name']='Ahmad'
student2['age']=17
student2['course']='BIS'
student2['married'] =False

print(student2)
print(student2['name'])
#print(student2['last name'])
print(len(student2))
print('Ahmad' in student2['name']) # works for string
values = student2.values()
print(2 in values)
print (17 in values) # works for int
print("married", True in values)



myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}

def calculateAverage(finalMarks):
	total = 0

	for mark in finalMarks:
		total = total+finalMarks[mark]
	average = total/len(finalMarks)
	return average

print(calculateAverage(myFinalMarks))

finalMarks = {}

"""
3. Create a dictionary with characters as keys and counters as the corresponding values.
The first time you see a character, you would add an item to the dictionary. 
After that you would increment the value of an existing item. 
"""
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

h = histogram('brontosaurus')

print(h)


h = histogram('a')
print(h)
print(h.get('a', 0))
print(h.get('c', 0))

csf = {
'cw1-weight': 0.4,
'cw1-mark':79,
'exam-weight':0.6,
'exam-mark':65
}

print(csf.get('cw1-weight')*csf.get('cw1-mark')+csf.get('exam-weight')*csf.get('exam-mark'))

######Looping in dictionaries###
def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)
###################


def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

def reverse_lookup(d, v):
	for k in d:
		if d[k]==v:
			return k
	raise LookupError()

h = histogram ('parrot')

key = reverse_lookup(h,1)
print(key)

