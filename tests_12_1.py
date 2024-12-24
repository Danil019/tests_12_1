import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj1 = runner.Runner('TestTimosha')
        for _ in range(10):
            obj1.walk()
        self.assertEqual(obj1.distance, 50)

    def test_run(self):
        obj2 = runner.Runner('TestRoma')
        for _ in range(10):
            obj2.run()
        self.assertEqual(obj2.distance, 100)

    def test_challenge(self):
        obj1_chall = runner.Runner('TestTimosha')
        obj2_chall = runner.Runner('TestRoma')
        for _ in range(10):
            obj1_chall.walk()
            obj2_chall.run()
        self.assertNotEqual(obj1_chall.distance, obj2_chall.distance)