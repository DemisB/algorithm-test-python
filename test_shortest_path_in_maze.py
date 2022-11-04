import unittest
from mazes import mazes
from shortest_path_in_maze import shortest_path


# Having fun with a metaclass...
# Don't do this at home, it makes everything unreadable.

class TestClassCreator(type):
    def __new__(mcs, *args, **kwargs):
        test_class = super().__new__(mcs, *args, **kwargs)

        for i, (test_case_input, expected_path) in enumerate(mazes):
            def _test_func(test_instance: unittest.TestCase):
                test_instance.assertEqual(expected_path,
                                          shortest_path(test_case_input["start"],
                                                        test_case_input["end"],
                                                        test_case_input["maze"]))

            setattr(test_class, f"test_case_{i}", _test_func)

        return test_class


class TestShortestPathInMaze(unittest.TestCase, metaclass=TestClassCreator):
    pass
