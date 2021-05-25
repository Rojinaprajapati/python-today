class mobile:
    processor='snapdragon'
    camera=20

redmi=mobile()
print(type(redmi))
print("the processor of redmi is:",redmi.processor)
print("the processor of redmi is:",redmi.camera)
redmi.processor="quad core"
redmi.camera=45
print("the processor of redmi is:",redmi.processor)
print("the processor of redmi is:",redmi.camera)



samsung=mobile()
print(type(samsung))
samsung.processor='s1'
samsung.camera=10
print("the processor of samsung is:",samsung.processor)
print("the processor of samsung is:",samsung.camera)
