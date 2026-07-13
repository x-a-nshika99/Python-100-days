# def my_function():
    # do this 
    # then do 
    # finally do 

def format_name(f_name , l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return {formated_f_name}, {formated_l_name}

format_name(f_name="anshika" , l_name= "pal")

print(format_name)


# multi return in one function 

def format_name1(f_name , l_name):
    """take a first and 
       lasy name"""
    if f_name == "" or l_name =="" :
        return "you did not put anyvalue"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return {formated_f_name}, {formated_l_name}

format_name1(f_name="anshika" , l_name= "pal")

print(format_name1)



# docstring  Docstrings are basically a 
# way for us to create little bits of documentation as
#  we're coding along


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)
# answer why
# a = 5 which means c= 5 and b= 10 this mean d = 10 . 
# the output of inner function become the output of outer function.
