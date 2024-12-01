import unittest

def frozen_check(method):
    def wrapper(self, *args, **kwargs):
        if getattr(self, "is_frozen", False):
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False
    @frozen_check
    def test_run(self):
        self.assertTrue(True)

    @frozen_check
    def test_walk(self):
        self.assertTrue(True)

    @frozen_check
    def test_challenge(self):
        self.assertTrue(True)
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @frozen_check
    def test_first_tournament(self):
        self.assertTrue(True)

    @frozen_check
    def test_second_tournament(self):
        self.assertTrue(True)

    @frozen_check
    def test_third_tournament(self):
        self.assertTrue(True)

