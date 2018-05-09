import unittest, os

class RecipeTests(unittest.TestCase):
    # methods to make unittest happy
    def test_has_title(self):
        self.iterate_over_files(self.has_title)

    def test_title_matches_file_name(self):
        self.iterate_over_files(self.title_matches_file_name)

    def test_has_method(self):
        self.iterate_over_files(self.has_method)

    # implmentation of tests
    def has_method(self, file):
        full_text = file.readlines()
        self.assertTrue('## Method\n' in full_text, "File {} does not contain a method".format(file.name))

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

    # helper function to iterate over all our recipe files
    def iterate_over_files(self, test_assertion):
        directories = ['main','dessert','breakfast']
        for directory in directories:
            files = os.listdir(directory)
            for file in files:
                path = directory + "/" + file
                with open(path) as f :
                    test_assertion(f)


if __name__ == '__main__':
    unittest.main()
