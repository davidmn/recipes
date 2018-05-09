import unittest, os

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

    # implmentation of tests
    def has_method(self, file):
        self.does_file_contain_string(file, "## Method\n")

    def has_ingredients(self, file):
        self.does_file_contain_string(file, "## Ingredients\n")

    def title_matches_file_name(self, file):
        first_line = firstLine = file.readline().rstrip()
        expected_file_name = first_line[2:].lower().replace(' ','-') + '.md'
        print(expected_file_name)
        actual_file_name = os.path.basename(file.name)
        self.assertEqual(expected_file_name, actual_file_name, 'File {} does not have expected filename {}'.format(file.name,expected_file_name))

    def has_title(self, f):
        firstLine = f.readline().rstrip()
        print(firstLine)
        self.assertTrue(firstLine.startswith('# '), 'Title in file {} did not start with h1'.format(f.name))

    # helper functions
    def iterate_over_files(self, test_assertion):
        directories = ['main','dessert','breakfast']
        for directory in directories:
            files = os.listdir(directory)
            for file in files:
                path = directory + "/" + file
                with open(path) as f :
                    test_assertion(f)

    def does_file_contain_string(self, file, string):
        full_text = file.readlines()
        self.assertTrue(string in full_text, "File {} does not contain {}".format(file.name, string))

if __name__ == '__main__':
    unittest.main()
