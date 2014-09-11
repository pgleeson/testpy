import numpy

print("Testing numpy!")

v = [1,2,3,4]

print(v)

y = numpy.array([2.,4.,6.,8.])

print(y)

myFileName = "myfile.dat"

y.tofile(myFileName)

g = numpy.fromfile(myFileName)

print(g)

c = numpy.array( [ [1j,-2j], [-3,4] ], dtype=numpy.complex )


print("c = "+ str(c))
print("c.T = "+ str(c.T))


d = c * (3 + 4j)
print("d = "+ str(d))


x = numpy.ones( (5,4) )
x[1,2] = 20

print(x)
print(x.__class__)
print(x.dtype)


m = numpy.empty( (2,3) , dtype=complex )
print(m)
print(m.dtype)



m = numpy.zeros( (4,4) , dtype=float )

v2 = [1,2,3,4]

m[2] = v2

print("\n   m:\n")
print(m)


import tables
h5file = tables.openFile("tutorial1.h5", mode = "w", title = "Test file")

group = h5file.createGroup("/", 'someinfo', 'Some old information')

#h5file.createArray(group, 'valuez', m, "Sum vals")

h5file.close()

#exit()

    