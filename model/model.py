from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.idMapRetailers = {}

        self._bestSol = []
        self.bestPeso = 0

    def getCountries(self):
        return DAO.getCountries()
    def buildGraph(self, country, anno):
        self._grafo.clear()
        listRetailers = DAO.getRetailersCountry(country)
        for r in listRetailers:
            self._grafo.add_node(r.Retailer_code)
            self.idMapRetailers[r.Retailer_code]=r.Retailer_name
        self.addEdges(anno, country)

    def addEdges(self, anno, country):
        connessioni = DAO.getConnessioni(anno, country)
        for c in connessioni:
            self._grafo.add_edge(c.R1, c.R2)
            self._grafo[c.R1][c.R2]["weight"] = c.product_count
    def getNumberOfNodes(self):
        return self._grafo.number_of_nodes()
    def getNumberOfEdges(self):
        return self._grafo.number_of_edges()

    def getVolumeVendita(self):
        mappaVolumi = {}
        for nome in self._grafo.nodes:
            mappaVolumi[self.idMapRetailers[nome]] = 0
        for n1 in self._grafo.nodes:
            vicini = self._grafo.neighbors(n1)
            for n2 in vicini:
                mappaVolumi[self.idMapRetailers[n1]] += self._grafo[n1][n2]["weight"]
        return dict(sorted(mappaVolumi.items(), key=lambda item: item[1], reverse=True))
    def getPath(self, n):
        pass

    def ricorsione(self,):
        pass