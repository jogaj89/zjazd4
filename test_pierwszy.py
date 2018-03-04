#! /usr/bin/python

import unittest
import kato, random

class Test_Pierwszy(unittest.TestCase):

    def test_test(self):
        self.assertTrue(True)

    def test_f1_1(self):
        k=kato.f1(0)
        self.assertEqual(k, 0)

    def test_f1_2(self):
        k1=kato.f1(1)
        self.assertEqual(k1,1)

    def test_f1_3(self):
        k2=kato.f1(2)
        self.assertEqual(k2,4)

    def test_f1_4(self):
        k3=kato.f1(2,1)
        self.assertEqual(k3, 5)

    def test_f1_5(self):
        k4=kato.f1(2,3)
        self.assertEqual(k4,7)

    def test_f2_1(self):
        a1=kato.f2('ala')
        self.assertEqual(a1,'a')

    def test_f2_2(self):
        a2=kato.f2([1,2,3])
        self.assertEqual(a2, 1)

    def test_f2_3(self):
        a3=kato.f2([])
        self.assertEqual(a3, 'BUUUM')

    def test_f3_1(self):
        b1=kato.f3(1)
        self.assertEqual(b1, 'jeden')

    def test_f3_2(self):
        b2=kato.f3(2)
        self.assertEqual(b2, 'dwa')

    def test_f3_3(self):
        b3=kato.f3(3)
        self.assertEqual(b3, 'trzy')

    def test_f3_4(self):
        b4=kato.f3(random.choice(range(4,1000)))
        self.assertEqual(b4, 'other')

    def test_f4_1(self):
        c1=kato.f4("ala")
        self.assertEqual(c1, "ala ma kota")

    def test_f4_2(self):
        c2=kato.f4("kot")
        self.assertEqual(c2, "kot ma kota")

    def test_f4_3(self):
        c3=kato.f4("kot", "psa")
        self.assertEqual(c3, "kot ma kota i psa")

    def test_f4_4(self):
        c4=kato.f4("kot", "mysz")
        self.assertEqual(c4, "kot ma kota i mysz")

    def test_f5_1(self):
        d1=kato.f5(0)
        self.assertEqual(d1, [])

    def test_f5_2(self):
        d2=kato.f5(1)
        self.assertEqual(d2,[0])

    def test_f5_3(self):
        d3=kato.f5(2)
        self.assertEqual(d3,[0,1])

    def test_f5_4(self):
        d4=kato.f5(7)
        self.assertEqual(d4,[0,1,2,3,4,5,6])

    def test_f5_5(self):
        d5=kato.f5(7,2)
        self.assertEqual(d5, [0,2,4,6])

    def test_f5_6(self):
        d6=kato.f5(17,2)
        self.assertEqual(d6, [0,2,4,6,8,10,12,14,16])

    def test_f5_7(self):
        d7=kato.f5(17,5)
        self.assertEqual(d7,[0, 5, 10,15])

    def test_f6_1(self):
        e1=kato.f6(1, "*")
        self.assertEqual(e1, "*")

    def test_f6_2(self):
        e2=kato.f6(7, "*")
        self.assertEqual(e2,"*******")

    def test_f7_1(self):
        f1=kato.f7("ala")
        self.assertEqual(f1,"slowo")

    def test_f7_2(self):
        f2=kato.f7("1")
        self.assertEqual(f2,"cyfra")

    def test_f7_3(self):
        f3=kato.f7("11111")
        self.assertEqual(f3,"liczba")

    def test_f7_4(self):
        f4=kato.f7("-11111")
        self.assertEqual(f4,"liczba ze znakiem")

    def test_f7_5(self):
        f5=kato.f7("Ala ma kota.")
        self.assertEqual(f5,"zdanie")

if __name__ == '__main__':
    unittest.main()
