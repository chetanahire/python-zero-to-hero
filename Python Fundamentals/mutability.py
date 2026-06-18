# mutable objects - list, dictionary, or set
def modify_list(lst):
    list.append(10) # modifies original list


list = [1,2,3,4]
modify_list(list)
print(list) 


# immutable objects -  int, float, string, or tuple
def modify_number(num):
    num += 10  # creates new integer object


number = 5
modify_number(number)
print(number) 