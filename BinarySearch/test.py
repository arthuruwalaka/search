from recursivebinarysearch import RecursiveSearch
x = list(range(0,20,2))
print(x)
min = 0 
max = len(x) - 1
print(RecursiveSearch(x,0,min,max))