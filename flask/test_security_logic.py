import re
import unittest

def validate_subpath(subpath: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9./_-]+$", subpath))

class TestSecurityLogic(unittest.TestCase):
    def test_valid_subpaths(self):
        self.assertTrue(validate_subpath("foo/bar"))
        self.assertTrue(validate_subpath("valid-path_123.txt"))
        self.assertTrue(validate_subpath("a/b/c"))
        self.assertTrue(validate_subpath("index.html"))

    def test_invalid_subpaths(self):
        self.assertFalse(validate_subpath("<script>"))
        self.assertFalse(validate_subpath("foo;bar"))
        self.assertFalse(validate_subpath("foo|bar"))
        self.assertFalse(validate_subpath("$(whoami)"))
        self.assertFalse(validate_subpath("`ls`"))
        self.assertFalse(validate_subpath(" "))
        self.assertFalse(validate_subpath("foo\nbar"))

if __name__ == '__main__':
    unittest.main()
