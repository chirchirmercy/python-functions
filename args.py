# # def mycountry(country="Rwanda")
# # print(f"Hello from{country}")


# def greet(*names):
#     for name in names: 
#         print(f"Hello{name}")



# def sum(*numbers):
#     answer=0
# for number in numbers 
#     answer+=number


# return answer

# # //create a function that acan accept any number of itegers 
# # //and return the results of multiply and all of them
# def multiply(*nums):
#     answer=1
#     for num in nums:
#     answer=number


#     return answer



# def student_attributes(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")







    #    // A function named concatenate_args that takes any number of string arguments in 
    #    //positional arguments format and concatenates them into a single string
def concatenate_args(*stringy, sep="/"):
    return sep.join(stringy)

    #   // A function named concatenate_kwargs that takes any number of string arguments in 
    #   //keyword arguments  format and concatenates them into a single string
  def concatenate_kwargs(*kwargs):
       nums=""
    for key,value in kwargs.items():
       nums+=value
    return nums