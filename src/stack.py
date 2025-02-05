class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""

        self.top = None  # Zásobník je zpočátku prázdný, je nastaven na hodnotu None.

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """

        data = Node(data, self.top)  # Tento řádek vytvoří nový objekt Node se zadanými daty a aktuálním vrcholem zásobníku
                                     # jako next_node. Tím se nový uzel vloží na vrchol zásobníku a stane se novým vrchním prvkem.
        self.top = data  # Nově přidaný uzel, který se stane novým horním prvkem zásobníku.

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:  # Kontrolujeme jestli je zásobník je prázdný, pokud je, vrací None,
            return None       # což říka, že z prázdného zásobníku není co vybírat.
        else:
            data = self.top.data  # Pokud zásobník není prázdný, načte tento řádek data z nejvyššího prvku zásobníku.
                                  # self.top představuje nejvyšší prvek (objekt Node) a self.top.data zpřístupní data
                                  # uložená v tomto prvku, která jsou poté přiřazena proměnné data.

            self.top = self.top.next_node  # Po načtení dat tento řádek aktualizuje self.top tak,
                                           # aby ukazoval na další prvek v zásobníku.
                                           # Tím se aktuální horní prvek ze zásobníku odstraní.

            return data  # Vracíme data, která byla právě odstraněna z vrcholu zásobníku.

