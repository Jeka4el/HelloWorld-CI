import unittest
from io import StringIO
import sys
from hello_world import main

class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            main()
            output = out.getvalue().strip()
            self.assertEqual(output, "Hello, World!")
        finally:
            sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main()
