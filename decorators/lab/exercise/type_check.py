def type_check(param_type):
    def decorator(func_ref):
        def wrapper(*args):
            for param in args:
                if type(param) is not param_type:
                    return "Bad Type"
            result = func_ref(*args)
            return result
        
        return wrapper
    return decorator


# @type_check(str) 
# def first_letter(word): 
#     return word[0] 

# print(first_letter('Hello World')) 
# print(first_letter(['Not', 'A', 'String'])) 