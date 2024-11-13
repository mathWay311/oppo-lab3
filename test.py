import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_type_in_list_1(self):
        elem = main.Cuboid(100, "random", 10, 20 ,30)
        types = ["cuboid", "sphere", "cylind"]

        ans = main.type_in_list(elem, types)

        self.assertTrue(ans)


    def test_type_in_list_2(self):
        elem = main.Figure(100, "random")
        types = ["cuboid", "sphere", "cylind"]

        ans = main.type_in_list(elem, types)

        self.assertFalse(ans)


    def test_handle_add_command_1(self):
        string = "ADD -t none -d 10 -a me1"
        args = string.split()
        main.handle_add_command(args)
        self.assertEqual(len(main.collection), 1)


    def test_handle_add_command_2(self):
        string = "ADD -t sphere -d 12 -a me2 -r 100"
        args = string.split()
        main.handle_add_command(args)
        self.assertEqual(len(main.collection), 2)


    def test_handle_add_command_3(self):
        string = "ADD -t cuboid -d 14 -a me3 -A 1 -B 2 -C 3"
        args = string.split()
        main.handle_add_command(args)
        self.assertEqual(len(main.collection), 3)


    def test_handle_add_command_4(self):
        string = "ADD -t cylind -d 16 -a me4 -r 20 -h 20"
        args = string.split()
        main.handle_add_command(args)
        self.assertEqual(len(main.collection), 4)
        main.handle_print_command()


    def test_handle_rem_1(self):
        string = "REM -t cylind"
        args = string.split()
        main.handle_rem_command(args)
        self.assertEqual(len(main.collection), 3)
        main.handle_print_command()


    def test_handle_rem_2(self):
        string = "REM -d >12"
        args = string.split()
        main.handle_rem_command(args)
        self.assertEqual(len(main.collection), 2)
        main.handle_print_command()


    def test_handle_rem_3(self):
        string = "REM -a me1"
        args = string.split()
        main.handle_rem_command(args)
        self.assertEqual(len(main.collection), 1)
        main.handle_print_command()


    def test_handle_rem_4(self):
        string = "REM -m <10000000"
        args = string.split()
        main.handle_rem_command(args)
        self.assertEqual(len(main.collection), 0)
        main.handle_print_command()



if __name__ == '__main__':
    unittest.main()
