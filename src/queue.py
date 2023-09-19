class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """

        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None  # Fronta má dva atributy: head a tail. Tyto atributy začínají jako None,
        self.tail = None  # protože enqueue/fronta je prázdná.

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь

        Metoda enqueue přidá prvek na konec fronty. Vytvoří
        nový uzel (new_node) se zadanými údaji a nastaví jeho next_node na None.
        Pokud je fronta aktuálně prázdná (tj. self.head je None), nastaví self.head i self.tail na nový node.
        Pokud fronta není prázdná, aktualizuje next_node aktuálního uzlu tail tak, aby ukazoval na nový uzel,
        a poté aktualizuje self.tail na nový uzel, čímž se stane novým ocasem fronty.
        """
        new_node = Node(data,None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.data))
            current = current.next_node

        return "\n".join(result)
