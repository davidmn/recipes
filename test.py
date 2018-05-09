import unittest, os

class RecipeTests(unittest.TestCase):
    def test_title_match(self):
        directories = ['main','dessert','breakfast']
        for directory in directories:
            files = os.listdir(directory)
            for file in files:
                path = directory + "/" + file
                with open(path) as file :
                    firstLine = file.readline().rstrip()
                    print firstLine
                    self.assertTrue(firstLine.startswith('# '), 'Title in file {} did not start with h1'.format(path))
                    expectedFilename = firstLine[2:].lower().replace(' ','-') + '.md'
                    print expectedFilename
                    self.assertEqual(expectedFilename, file, 'File {} does not have expected filename {}'.format(path,expectedFilename))



if __name__ == '__main__':
    unittest.main()
