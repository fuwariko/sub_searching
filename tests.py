import unittest
import brute_force
import rabin_karp
import knut_morris_pratt
import aho_corasick
import z_function


class TestMethods(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(brute_force.find_substring("DDDDDDDDDDDDDA", "DA"), True)
        self.assertEqual(brute_force.find_substring("AABAACAADAAAABDAADB", "AABA"), True)
        self.assertEqual(brute_force.find_substring("ABABDABACDABABCABAB", "ABABCABAB"), True)
        self.assertEqual(brute_force.find_substring("ABABDABACDABABCABAB", "AA"), False)
        self.assertEqual(brute_force.find_substring("bc" * 1000000 + "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"), True)
        self.assertEqual(brute_force.find_substring("D"*10000 + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDA",
                                                  "DA"),  True)
        self.assertEqual(brute_force.find_substring("D"*1000000 + "FMDAK          LSNFUANNVNSDKVNS      NSDNVSNJKVNSAIVNKSANVKJNDDDDDDDDA",
                                                  "SAI"), True)

    def test_robin_karp(self):
        self.assertEqual(rabin_karp.find_substring("DDDDDDDDDDDDDA", "DA"), True)
        self.assertEqual(rabin_karp.find_substring("AABAACAADAAAABDAADB", "AABA"), True)
        self.assertEqual(rabin_karp.find_substring("ABABDABACDABABCABAB", "ABABCABAB"), True)
        self.assertEqual(rabin_karp.find_substring("ABABDABACDABABCABAB", "AA"), False)
        self.assertEqual(rabin_karp.find_substring("bc" * 1000000 + "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"), True)
        self.assertEqual(rabin_karp.find_substring("D"*10000 + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDA",
                                                 "DA"), True)
        self.assertEqual(rabin_karp.find_substring("D"*1000000 + "FMDAK          LSNFUANNVNSDKVNS      NSDNVSNJKVNSAIVNKSANVKJNDDDDDDDDA",
                                                 "SAI"), True)

    def test_knut_morris_pratt(self):
        self.assertEqual(knut_morris_pratt.find_substring("DDDDDDDDDDDDDA", "DA"), True)
        self.assertEqual(knut_morris_pratt.find_substring("AABAACAADAAAABDAADB", "AABA"), True)
        self.assertEqual(knut_morris_pratt.find_substring("ABABDABACDABABCABAB", "ABABCABAB"), True)
        self.assertEqual(knut_morris_pratt.find_substring("ABABDABACDABABCABAB", "AA"), False)
        self.assertEqual(
            knut_morris_pratt.find_substring("bc" * 1000000 + "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"),
            True)
        self.assertEqual(
            knut_morris_pratt.find_substring("D" * 10000 + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDA",
                                           "DA"), True)
        self.assertEqual(knut_morris_pratt.find_substring(
            "D" * 1000000 + "FMDAK          LSNFUANNVNSDKVNS      NSDNVSNJKVNSAIVNKSANVKJNDDDDDDDDA",
            "SAI"), True)

    def test_aho_corasick(self):
        self.assertEqual(aho_corasick.find_substring("DDA", "DA"), True)
        self.assertEqual(aho_corasick.find_substring("AABAACAADAAAABDAADB", "AABA"), True)
        self.assertEqual(aho_corasick.find_substring("ABABDABACDABABCABAB", "ABABCABAB"), True)
        self.assertEqual(aho_corasick.find_substring("ABABDABACDABABCABAB", "AA"), False)
        self.assertEqual(
            aho_corasick.find_substring("bc" * 1000000 + "abcdefghijklmnopqrstuvwxyz",
                                             "abcdefghijklmnopqrstuvwxyz"),
            True)
        self.assertEqual(
            aho_corasick.find_substring("D" * 10000 + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDA",
                                             "DA"), True)

    def test_z_function(self):
        self.assertEqual(z_function.find_substring("DDA", "DA"), True)
        self.assertEqual(z_function.find_substring("AABAACAADAAAABDAADB", "AABA"), True)
        self.assertEqual(z_function.find_substring("ABABDABACDABABCABAB", "ABABCABAB"), True)
        self.assertEqual(z_function.find_substring("ABABDABACDABABCABAB", "AA"), False)
        self.assertEqual(
            z_function.find_substring("bc" * 1000000 + "abcdefghijklmnopqrstuvwxyz",
                                             "abcdefghijklmnopqrstuvwxyz"),
            True)
        self.assertEqual(
            z_function.find_substring("D" * 10000 + "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDA",
                                             "DA"), True)


if __name__ == "__main__":
    unittest.main()
