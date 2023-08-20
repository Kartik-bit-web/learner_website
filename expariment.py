from random import randint
store = []
def randoms(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

x = randoms(6)
print(x)
store.append(x)

#  {% with messages = get_flashed_messages() %}  
#         {% if messages %}  
#               {% for message in messages %}  
#                    <p>{{ message }}</p>  
#               {% endfor %}  
#         {% endif %}  
#      {% endwith %}  
#
print(store[0])