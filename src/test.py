import math
from PIL import Image
#import parser as pr
from parser import test

print(Image.__version__)

print("*args demo")


#pr.test("Hi!", 23, math.pi)
test("Hi!", 23, math.pi)

# lambda function

mult = lambda x,y: x*y
print("Multiplication result is %d" % mult(2,3))
