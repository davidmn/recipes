import os
import unittest
from subprocess import call


class RecipeTests(unittest.TestCase):
    # methods to make unittest happy
    def test_has_title(self):
        self.iterate_over_files(self.has_title)

    def test_title_matches_file_name(self):
        self.iterate_over_files(self.title_matches_file_name)

    def test_has_method(self):
        self.iterate_over_files(self.has_method)

    def test_has_ingredients(self):
        self.iterate_over_files(self.has_ingredients)

    def test_method_non_zero(self):
        self.iterate_over_files(self.method_non_zero)

    def test_ingredients_non_zero(self):
        self.iterate_over_files(self.ingredients_non_zero)

    # implmentation of tests
    def ingredients_non_zero(self, file):
        self.distance_betwix_lines(file, '## Ingredients\n', '## Notes\n')

    def method_non_zero(self, file):
        self.distance_betwix_lines(file, '## Method\n', '## Notes\n')

    def has_method(self, file):
        self.does_file_contain_string(file, "## Method\n")

    def has_ingredients(self, file):
        self.does_file_contain_string(file, "## Ingredients\n")

    def title_matches_file_name(self, file):
        first_line = file.readline().rstrip()
        expected_file_name = first_line[2:].lower().replace(' ', '-') + '.md'
        print(expected_file_name)
        actual_file_name = os.path.basename(file.name)
        self.assertEqual(expected_file_name, actual_file_name, 'File {} does not have expected filename {}'.format(file.name, expected_file_name))

    def has_title(self, f):
        firstLine = f.readline().rstrip()
        print(firstLine)
        self.assertTrue(firstLine.startswith('# '), 'Title in file {} did not start with h1'.format(f.name))

    # helper functions
    def distance_betwix_lines(self, file, firstLine, secondLine):
        full_text = file.readlines()
        a = full_text.index(firstLine)
        b = full_text.index(secondLine)

        self.assertTrue((b - a) > 3, "File {} has empty field {}".format(file.name, firstLine))

    def iterate_over_files(self, test_assertion):
        directories = ['main', 'dessert', 'breakfast']
        for directory in directories:
            files = os.listdir(directory)
            for file in files:
                path = directory + "/" + file
                with open(path) as f:
                    test_assertion(f)

    def does_file_contain_string(self, file, string):
        full_text = file.readlines()
        self.assertTrue(string in full_text, "File {} does not contain {}".format(file.name, string))


class ScriptTests(unittest.TestCase):
    def test_run_without_args_fails(self):
        return_code = call(["python3", "./mk-recipe.py"])
        self.assertEqual(return_code, 1, "Return code was {} when expected 1")

    def test_run_with_wrong_type_fails(self):
        return_code = call(["python3", "./mk-recipe.py", "--name", "test", "--type", "wrong"])
        self.assertEqual(return_code, 1, "Return code was {} when expected 1")

    def test_creates_file_correctly(self):
        test_file = "main/test-file-please-ignore.md"
        if os.path.exists(test_file):
            os.remove(test_file)

        return_code = call(["python3", "./mk-recipe.py", "--name", "Test File Please Ignore", "--type", "main", "--serves", "7734"])

        self.assertEqual(return_code, 0, "Return code was {} when expected 0".format(return_code))

        with open(test_file) as file:
            full_text = file.readlines()
            self.assertTrue("7734\n" in full_text, "File {} does not contain {}".format(file.name, "7734"))

            self.assertTrue("# Test File Please Ignore\n" in full_text, "File {} does not contain {}".format(file.name, "# Test File Please Ignore"))

        os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
