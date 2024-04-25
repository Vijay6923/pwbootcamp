class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

a = Complex(6, 8)
b = Complex(9, 5)

c = a + b
d = a - b

print(c.real, c.imaginary)
print(d.real, d.imaginary)

# class Complex:
#     def __init__(self,real,imaginary):
#         self.real=real
#         self.imaginary=imaginary
#     def __add__(self,other):
#         return complex(self.real+other.real,self.imaginary + other.imaginary)
#     def __sub__(self,other):
#         return complex(self.real-other.real,self.imaginary - other.imaginary)
#a=complex(6, 8)
#b=complex(9, 5)
#c=a + b
#d=a - b
#print(c.real, c.imaginary)
#print(d.real, d.imaginary) 
