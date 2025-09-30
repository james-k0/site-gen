import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(
            repr(node),
            '<a  href="https://example.com" target="_blank"> children: None \n Click here </a>'
        )
        node_no_props = HTMLNode(tag="p", value="hello")
        self.assertEqual(
            repr(node_no_props),
            '<p > children: None \n hello </p>'
        )
    
    def test_props(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://example.com" target="_blank"'
        )
        self.assertEqual(HTMLNode().props_to_html(), "")

    def test_leaf_to_html(self):
        self.assertEqual(LeafNode(None, "plain").to_html(), "plain")
        self.assertEqual(LeafNode("p", "hello").to_html(), "<p>hello</p>")
        node = LeafNode("a", "Click", {"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Click</a>')
        with self.assertRaises(ValueError):
            LeafNode("span", None).to_html()

    def test_to_html_with_children(self):
        # renders multiple children
        parent = ParentNode("div", [LeafNode("p", "Hello"), LeafNode("span", "World")])
        self.assertEqual(parent.to_html(), "<div><p>Hello</p><span>World</span></div>")
        parent_with_props = ParentNode("ul", [LeafNode("li", "One"), LeafNode("li", "Two")], {"class": "list"})
        self.assertEqual(parent_with_props.to_html(), '<ul class="list"><li>One</li><li>Two</li></ul>')
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "x")]).to_html()
