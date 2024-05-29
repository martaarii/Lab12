from model.model import Model

mymodel = Model()

mymodel.buildGraph("France", 2015)
print(mymodel.getNumberOfNodes(), mymodel.getNumberOfEdges())

mappaV = mymodel.getVolumeVendita()
for key, value in mappaV.items():

    print(key, value)