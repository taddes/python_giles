"""
Trick to emulate switch cases
Removes need for chained if statements
"""

def myfunc(a, b):
    return a + b
  
funcs = [myfunc]
print(funcs[0](2, 3))
"""
func_dict = {
   'cond_a': handle_a,
   'cond_b': handle_b,
   'cond_c': handle_c,
}

# Returns a default defined value in case the condition not found
func_dict.get(cond, handle_default)()
"""

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    if operator == 'sub':
        return x - y
    if operator == 'mul':
        return x * y
    if operator == 'div':
        return x / y

# Switch case emulation
# Not most performant or best for memory, esp if you call it a lot
# Can optimize by caching the dictionary in a variable and just reference the variable to call it
# Every time function called, it has to create that dict
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }.get(operator, lambda: None)()

print(dispatch_dict('add', 22, 65))