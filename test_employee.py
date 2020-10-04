import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Bob', 'Thebuilder', 3000)
        self.emp_2 = Employee('Simon', 'Says', 9000)

    def tearDown(self):
        print('teardown/n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Bob.Thebuilder@company.com')
        self.assertEqual(self.emp_2.email, 'Simon.Says@company.com')

        self.emp_1.first = 'Jamie'
        self.emp_2.first = 'Cersei'

        self.assertEqual(self.emp_1.email, 'Jamie.Thebuilder@company.com')
        self.assertEqual(self.emp_2.email, 'Cersei.Says@company.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Bob Thebuilder')
        self.assertEqual(self.emp_2.fullname, 'Simon Says')

        self.emp_1.first = 'Jamie'
        self.emp_2.first = 'Cersei'

        self.assertEqual(self.emp_1.fullname, 'Jamie Thebuilder')
        self.assertEqual(self.emp_2.fullname, 'Cersei Says')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 3150)
        self.assertEqual(self.emp_2.pay, 9450)

if __name__ == '__main__':
    unittest.main()