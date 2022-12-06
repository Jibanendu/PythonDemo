import numpy 

numpy.set_printoptions(legacy='1.13')
input_string='1.1,2.2,3.3'
k = input_string.split(',')

n = numpy.array(k,float)

print(numpy.floor(n))
print(numpy.ceil(n))
print(numpy.rint(n))
