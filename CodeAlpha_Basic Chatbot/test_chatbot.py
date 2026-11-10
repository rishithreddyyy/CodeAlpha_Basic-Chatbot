import unittest
from chatbot import get_response

class TestBasicChatbot(unittest.TestCase):
    def test_greetings(self):
        self.assertIn("Hi!", get_response("hello"))
        self.assertIn("Hi!", get_response("HELLO"))
        self.assertIn("Hi!", get_response("  hi  "))
        self.assertIn("Hi!", get_response("hey"))

    def test_how_are_you(self):
        self.assertIn("I'm fine, thanks!", get_response("how are you"))
        self.assertIn("I'm fine, thanks!", get_response("How Are You?"))
        self.assertIn("I'm fine, thanks!", get_response("how are you doing"))

    def test_identity(self):
        self.assertIn("simple rule-based chatbot", get_response("what is your name"))
        self.assertIn("simple rule-based chatbot", get_response("who are you?"))

    def test_farewells(self):
        self.assertIn("Goodbye!", get_response("bye"))
        self.assertIn("Goodbye!", get_response("BYE"))
        self.assertIn("Goodbye!", get_response("goodbye"))
        self.assertIn("Goodbye!", get_response("exit"))

    def test_help(self):
        self.assertIn("You can talk to me with simple phrases", get_response("help"))
        self.assertIn("You can talk to me with simple phrases", get_response("what can you do"))

    def test_fallback(self):
        self.assertIn("I'm sorry, I don't understand that", get_response("random gibberish 12345"))
        self.assertIn("I'm sorry, I don't understand that", get_response("what is the weather on Mars?"))

if __name__ == "__main__":
    unittest.main()

