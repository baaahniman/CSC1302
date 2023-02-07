#Prolog
#Author: Bahniman Rajkonwar Das
#Email: bdas6@student.gsu.edu
#Section:34
lst=[10,1,30,20,4,9,19,6]
def last(lst):
    removed_item=lst[-1]
    new_list=lst[0:len(lst)-1]
    print(new_list)
    return removed_item
def main():
    print(min(lst))
    print(max(lst))
    print(sum(lst))
    print(last(lst))
main()
