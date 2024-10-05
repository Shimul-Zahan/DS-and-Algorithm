# For every DS and Algorithm first create a new Class
# Then create a new constructor
# After creating all of the methods thats you want to

# here we create a class
class Cookie:
    # here we create a new constructor
    def __init__(self, color):
        self.color = color
        
    # here we create a new method
    def get_color(self):
        return self.color
    
    # here we create a new method
    def set_color(self, color):
        self.color = color
        
# Create objects for this class
cookie_one = Cookie('Red')       
cookie_two = Cookie('Yellow')   
   
# Print the cookie  
print('\ncookie color is', cookie_one.get_color())
print('cookie color is', cookie_two.get_color())

cookie_one.set_color('Green')

# Print the cookie  
print('\n cookie color is', cookie_one.get_color())
print('cookie color is', cookie_two.get_color())
