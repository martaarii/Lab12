import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        listOfCountries = self._model.getCountries()
        for c in listOfCountries:
            self._view.ddcountry.options.append(ft.dropdown.Option(c))
        self._view.update_page()


    def handle_graph(self, e):
        country = self._view.ddcountry.value
        anno = self._view.ddyear.value
        self._model.buildGraph(country, anno)
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumberOfNodes()}\n"
                                                      f"Numero di archi: {self._model.getNumberOfEdges()}"))

        self._view.update_page()


    def handle_volume(self, e):
        volumiVendita = self._model.getVolumeVendita()
        for key, value in volumiVendita.items():
            self._view.txtOut2.controls.append(ft.Text(f"{key} --> {value}"))
        self._view.update_page()

    def handle_path(self, e):
        numArchi = self._view.txtN.value
        try: int(numArchi) >= 2
        except ValueError:
            self._view.txtOut2.controls.append(ft.Text(f"immettere un numero intero maggiore di 2"))
            return


