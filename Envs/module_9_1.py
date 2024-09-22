

def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        if function in (max, min):
            res_list = [function(int_list)]
        elif function in (len, sum):
            res_list = [function(int_list)]
        else:
            res_list = function(int_list)
        result[function.__name__] = res_list
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))