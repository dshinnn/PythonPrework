# Question 1
def hello_name(user_name):
    print("hello_" + user_name)

hello_name("bob")

# Question 2
def first_odds():
    for num in range(1,101):
        if num % 2 == 1:
            print(str(num) + " ")
        else:
            continue

first_odds()

# Question 3
def max_num_in_list(a_list):
    max = 0
    for num in a_list:
        if num > max:
            max = num
        else:
            continue
    return max

print("\n" + str(max_num_in_list([1, 20, 3, 4, 5])))

# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False

#print("\n" + str(is_leap_year(1600)))

# Question 5
def is_consecutive(a_list):
    max = max_num_in_list(a_list)
    for num in a_list:
        next_num = num + 1
        if num == max or next_num in a_list:
            continue
        else:
            return False
    return True

print(str(is_consecutive([7,1,2,3,4,5,0,6])))
