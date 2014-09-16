import jsonpickle

dct = {}
dct['gg']='pp'
dct['44']=77

print("Before: %s"%dct)

encoded = jsonpickle.encode(dct)
newdict = jsonpickle.decode(encoded)

print("After:  %s"%newdict)