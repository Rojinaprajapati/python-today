class Mobile:
    def __init__(self,processor,camera):
        self.processor=processor
        self.camera=camera

    def getProcessorName(self):
        return self.processor
    
    def getCamera(self):
        return self.camera
Redmi=Mobile("Snapdragon",13)
print("The Processor of Redmi is ",Redmi.processor)
print("The Camera of Redmi is : ",Redmi.camera)

Samsung=Mobile("Quad Core ",35)
print("The Processor of Samsung is ",Samsung.getProcessorName())
print("The Camera of Samsung is : ",Samsung.getCamera())

