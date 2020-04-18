import unittest

import wiki_population_list_ca1

class TestWiki_Population(unittest.TestCase):

    def setUp(self):
        self.contents = wiki_population_list_ca1.get_page_contents()
#Test of get page by knowing it contains more than 5 char
    def test_get_page(self):
        self.assertTrue(len(self.contents) > 5)
#Test of converion to beautiful Soup
    def test_convert_to_soup(self):
        self.assertTrue(wiki_population_list_ca1.convert_to_soup(self.contents) is not None)
#Test to get table from website        
    def test_get_table(self):
        soup = wiki_population_list_ca1.convert_to_soup(self.contents)
        self.assertTrue(wiki_population_list_ca1.get_gdp_table(soup) is not None)
#Test to get data from the table, knowing it would have more than 100 char        
    def test_get_table_data(self):
        soup = wiki_population_list_ca1.convert_to_soup(self.contents)
        table = wiki_population_list_ca1.get_gdp_table(soup)
        self.assertTrue(len(wiki_population_list_ca1.get_gdp_table_data(table)) > 100)
#Testing that program returned 6 different headers.         
    def test_heading(self):
        soup = wiki_population_list_ca1.convert_to_soup(self.contents)
        table = wiki_population_list_ca1.get_gdp_table(soup)
        data = wiki_population_list_ca1.get_gdp_table_data(table)
        self.assertTrue(len(wiki_population_list_ca1.heading(data)) == 6)
                
                
        
if __name__ == '__main__':
    unittest.main()
