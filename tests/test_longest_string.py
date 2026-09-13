#!/usr/bin/env python3

import unittest

from src.longest_string import longest


class TestLongest(unittest.TestCase):

    def test_worked_example(self):
        strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
        result = longest(strings)
        self.assertEqual(
            result, "howdydoody",
            msg="longest(%s) should be 'howdydoody' (10 characters, the "
                "longest string in the list). Got %r." % (strings, result))

    def test_return_type_is_str(self):
        result = longest(["ab", "a"])
        self.assertIsInstance(
            result, str,
            msg="longest(['ab', 'a']) should return a str, not %s. Got %r."
                % (type(result).__name__, result))

    def test_various_word_lists(self):
        test_cases = [
            "first second third",
            "ab abcd abc acbdefg a abcd aa",
            "orange apple milkshake banana pear",
            "sheila sells seashells on the seashore",
        ]
        for sentence in test_cases:
            words = sentence.split()
            with self.subTest(words=words):
                expected = max(words, key=len)
                result = longest(words)
                self.assertEqual(
                    result, expected,
                    msg="longest(%s) should be %r (the longest word is %d "
                        "characters). Got %r." % (words, expected,
                                                   len(expected), result))

    def test_single_word_list(self):
        result = longest(["solo"])
        self.assertEqual(
            result, "solo",
            msg="longest(['solo']) should be 'solo': with only one word, it "
                "is automatically the longest. Got %r." % (result,))


if __name__ == "__main__":
    unittest.main()
