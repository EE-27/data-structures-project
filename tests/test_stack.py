"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class testNode(unittest.TestCase):
    def test_node_cls(self):
        node = Node("ABC")
        self.assertEqual(node.data, "ABC")
        self.assertEqual(node.next_node, None)
        n1 = Node(5, None)
        n2 = Node ("a", n1)
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, "a")
        self.assertEqual(n1, n2.next_node)


class testStack(unittest.TestCase):
    def test_push(self):
        stack_push = Stack()
        stack_push.push("A")
        stack_push.push("B")
        stack_push.push("C")
        self.assertEqual(stack_push.top.data, "C")
        self.assertEqual(stack_push.top.next_node.data, "B")
        self.assertEqual(stack_push.top.next_node.next_node.data, "A")
        self.assertIsNone(stack_push.top.next_node.next_node.next_node)

    def test_pop(self):
        stack = Stack()
        stack.push("A")
        data = stack.pop()
        self.assertIsNone(stack.top)
        self.assertEqual(data, "A")

        stack = Stack()
        stack.push("A")
        stack.push("B")
        data = stack.pop()
        self.assertEqual(stack.top.data, "A")
        self.assertEqual(data, "B")