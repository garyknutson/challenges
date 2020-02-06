class Challenge1 (unittest.TestCase) :
    def setUp (self) :
        #code to startup webdriver

    def tearDown (self)
        #code to close webdiver

     def test_challenge1 (self) :
         #code for our test steps

     def test_challengel (self) :
         self.driver.get ("https://www.google.com")
         self.assertIn ("Google", self.driver.title)


if __name__ == '__main__':
    unittest.main()
    



