def in_order(num_list):
    for i in range(1,len(num_list)):
        if num_list[i-1]>num_list[i]:
            return False
    return True

list1=[5,6,7,8,3]
list2=[5,6,7,8,10]
def main(list):
    print(list)
    if (in_order(list)):
        print('inorder')
    else:
        print('not in order')
main(list1)
main(list2)


