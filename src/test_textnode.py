import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("foo", TextType.TEXT, "url.exmple.cm")
        node2 = TextNode("bar",TextType.TEXT, "url.exmple.cm")
        node3 = TextNode("foo",TextType.TEXT,"usb")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)

    def test_repr(self):
        node = TextNode("'foo'", TextType.CODE)
        self.assertEqual(repr(node), "TextNode('foo', TextType.CODE, None)")

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()