# test_queue.py
# be Jacob Wolf
#
# Testing harness to rtest the functionality of an implementation of a queue structure.
# Tests the interfaces as defined by the python deque.
#
# =============================================================================
#  More-Than-You-Need-To-Know Lounge
# =============================================================================
# Welcome to the More-Than-You-Need-To-Know Lounge, a chill place for code that
# you don't need to understand.

# Thanks for stopping by, we hope you find something that catches your eye.
# But don't worry if this stuff doesn't make sense yet -- as long as we know
# how to use code, we don't have to understand everything about it.

# Of course, if you really like this place, stay a while. You can ask a
# teacher about it if you're interested.
#
# =============================================================================

import unittest
from student_queue import Queue


class TestMin(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_constructor(self):
        self.assertEqual(type(self.q), Queue)

    def test_fifo_append_all_then_pop(self):
        for i in range(10):
            self.q.append(i)
        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(self.q.popleft(), i)

    def test_fifo_concerrent_append_and_pop(self):
        for i in range(10):
            with self.subTest(i=i):
                self.q.append(i)
                self.assertEqual(self.q.popleft(), i)

class TestAppendMethod(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_append_to_empty(self):
        self.q.append(0)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next, None)

    def test_append_with_1_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 1)
        self.assertEqual(self.q.head.next.next, None)

    def test_append_duplicate_data(self):
        self.q.append(0)
        self.q.append(0)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 0)
        self.assertEqual(self.q.head.next.next, None)

class TestPopleftMethod(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_pop_from_empty(self):
        with self.assertRaises(IndexError):
            self.q.popleft()
        self.assertEqual(self.q.head, None)
    
    def test_pop_with_1_elem(self):
        self.q.append(0)
        self.assertEqual(self.q.popleft(), 0)
        self.assertEqual(self.q.head, None)

    def test_pop_with_multiple_elem(self):
        for i in range(10):
            self.q.append(i)
        for i in range(10):
            with self.subTest(i=i):
                self.assertEqual(self.q.popleft(), i)
        self.assertEqual(self.q.head, None)

class TestRemoveMethod(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_remove_0th_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.remove(0)
        self.assertEqual(self.q.head.data, 1)
        self.assertEqual(self.q.head.next.data, 2)
        self.assertEqual(self.q.head.next.next, None)

    def test_remove_last_element(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.remove(2)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 1)
        self.assertEqual(self.q.head.next.next, None)

    def test_remove_middle_element(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.remove(1)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 2)
        self.assertEqual(self.q.head.next.next, None)
        
    def test_remove_nonexistent_element(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        with self.assertRaises(ValueError):
            self.q.remove(3)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 1)
        self.assertEqual(self.q.head.next.next.data, 2)
        self.assertEqual(self.q.head.next.next.next, None)

    def test_remove_duplicate_data(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.append(1)
        self.q.remove(1)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 2)
        self.assertEqual(self.q.head.next.next.data, 1)
        self.assertEqual(self.q.head.next.next.next, None)

    def test_remove_from_empty_queue(self):
        with self.assertRaises(ValueError):
            self.q.remove(3)
        self.assertEqual(self.q.head, None)

    def test_remove_only_elem_from_queue(self):
        self.q.append(0)
        self.q.remove(0)
        self.assertEqual(self.q.head, None)

class TestInsertMethod(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_insert_at_start(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.insert(0, -1)
        self.assertEqual(self.q.head.data, -1)
        self.assertEqual(self.q.head.next.data, 0)
        self.assertEqual(self.q.head.next.next.data, 1)
        self.assertEqual(self.q.head.next.next.next.data, 2)
        self.assertEqual(self.q.head.next.next.next.next, None)

    def test_insert_at_end(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.insert(3, 3)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 1)
        self.assertEqual(self.q.head.next.next.data, 2)
        self.assertEqual(self.q.head.next.next.next.data, 3)
        self.assertEqual(self.q.head.next.next.next.next, None)

    def test_insert_in_middle(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.insert(2, 1.5)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 1)
        self.assertEqual(self.q.head.next.next.data, 1.5)
        self.assertEqual(self.q.head.next.next.next.data, 2)
        self.assertEqual(self.q.head.next.next.next.next, None)

    def test_insert_where_index_out_of_range(self):
        """ Note: The Python Deque object in the collections module
        append any elements inserted with an index out of range
        to the end of the queue.
        """
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.insert(4, 4)
        self.assertEqual(self.q.head.data, 0)
        self.assertEqual(self.q.head.next.data, 1)
        self.assertEqual(self.q.head.next.next.data, 2)
        self.assertEqual(self.q.head.next.next.next.data, 4)
        self.assertEqual(self.q.head.next.next.next.next, None)

class TestLenBuiltin(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_len_of_empty(self):
        self.assertEqual(len(self.q), 0)

    def test_len_of_1(self):
        self.q.append(0)
        self.assertEqual(len(self.q), 1)

    def test_len_of_multiple(self):
        for i in range(10):
            self.q.append(i)
        self.assertEqual(len(self.q), 10)

class TestIndexMethod(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_index_of_0th_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.assertEqual(self.q.index(0), 0)

    def test_index_of_last_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.assertEqual(self.q.index(2), 2)

    def test_index_of_middle_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.assertEqual(self.q.index(1), 1)

    def test_index_of_nonexistent_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        with self.assertRaises(ValueError):
            self.q.index(3)

    def test_index_of_duplicate_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.q.append(1)
        self.assertEqual(self.q.index(1), 1)

    def test_index_with_1_elem_queue(self):
        self.q.append(0)
        self.assertEqual(self.q.index(0), 0)

    def test_index_with_0_elem_queue(self):
        with self.assertRaises(ValueError):
            self.assertEqual(self.q.index(0), 0)
        
class TestCountMethod(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_count_elem_at_start(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(0)
        self.assertEqual(self.q.count(0), 2)

    def test_count_elem_at_end(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.assertEqual(self.q.count(2), 1)

    def test_count_nonexistent_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.assertEqual(self.q.count(3), 0)

    def test_count_queue_with_1_elem(self):
        self.q.append(0)
        self.assertEqual(self.q.count(0), 1)
        self.assertEqual(self.q.count(1), 0)

    def test_count_queue_with_0_elem(self):
        self.assertEqual(self.q.count(0), 0)

class TestGetItemBuiltin(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_get_0th_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.assertEqual(self.q[0], 0)

    def test_get_1st_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.assertEqual(self.q[1], 1)

    def test_get_last_elem(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        self.assertEqual(self.q[2], 2)

    def test_get_elem_from_queue_with_len_1(self):
        self.q.append(0)
        self.assertEqual(self.q[0], 0)

    def test_get_elem_from_queue_with_len_0(self):
        with self.assertRaises(IndexError):
            self.q[0]

    def test_get_elem_with_index_out_of_range(self):
        self.q.append(0)
        self.q.append(1)
        self.q.append(2)
        with self.assertRaises(IndexError):
            self.q[3]

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run functionality tests on your queue implementation.')
    parser.add_argument('tests', metavar='TEST_TYPE', type=str, nargs=1,
                    help='the tests you want to run',
                    choices=['min', 'basic', 'extension', 'all'])
    args = parser.parse_args()
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    if args.tests[0] == 'min':
        suite.addTest(loader.loadTestsFromTestCase(TestMin))
    elif args.tests[0] == 'basic':
        suite.addTest(loader.loadTestsFromTestCase(TestMin))
        suite.addTest(loader.loadTestsFromTestCase(TestAppendMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestPopleftMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestInsertMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestLenBuiltin))
    elif args.tests[0] == 'extension':
        suite.addTest(loader.loadTestsFromTestCase(TestIndexMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestCountMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestGetItemBuiltin))
    elif args.tests[0] == 'all':
        suite.addTest(loader.loadTestsFromTestCase(TestMin))
        suite.addTest(loader.loadTestsFromTestCase(TestAppendMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestPopleftMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestInsertMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestLenBuiltin))
        suite.addTest(loader.loadTestsFromTestCase(TestIndexMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestCountMethod))
        suite.addTest(loader.loadTestsFromTestCase(TestGetItemBuiltin))
    unittest.TextTestRunner().run(suite)

