#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(lst):
    
    idx=0
    sublst=[]
    while idx<len(lst):
        if lst[idx]!=5:
            sublst.append(lst[idx])
        elif lst[idx]==5:
            return sublst 
        idx=idx+1
    return sublst

lst=[1,2,3,4,6,7,8]
a=sublist(lst)    
print(a)
#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.

