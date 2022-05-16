import datetime

class MyClass:
    def __format__(self, format_spec) -> str:
        print(f'MyClass __format__ called with {format_spec=!r}')
        return "MyClass()"


def equals_debugging():
    """_summary_
    demonstrate f-strings "=" sign to display the value. Useful for debugging
    """ 
    str_value = "other 🐶"
    num_value = 123

    print(f'the value is {str_value}')
    print(f'{num_value = }')
    print(f'{num_value % 2 = }')
      
def conversions():
    str_value = "other 🐶"
    print(f'{str_value!a}') # Ascii
    print(f'{str_value!s}') # gets applied before formatting
    print(f'{str_value!r}') # repr

def formatting():
    num_value = 123.456
    now = datetime.datetime.utcnow()
    print(f'{now=:%Y—%m-%d}')
    print(f'{num_value:.2f}')
    print(f'{MyClass():blah blah %%MYFORMAT%%} ')
    
    nested_format = ".2f"
    print(f'{num_value:{nested_format}}')
    
    

equals_debugging()
print()
conversions()
print()
formatting()  
