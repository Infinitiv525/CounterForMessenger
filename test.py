import unittest
import sys
from Main import MasterWindow,StatisticsPopup


class TestExtractData(unittest.TestCase):

    def setUp(self):
        self.controller = MasterWindow()
        #title, participants, room, total_msgs, total_chars, calltime, sent_msgs, start_date, total_photos
        self.testGroup = ("TitleGroup",{'User1':1,'User2':2,'User3':3},"Group chat",6,209,0,1,1,1)
        self.testPrivate = ("TitlePrivate",{'User1':2,'User2':3},"Private chat",5,310,100,2,0,2)
        self.testMultiple = ("Time",{'User1':5,'User2':9},"Private chat",14,209,0,5,1,0)
    def tearDown(self):
        pass
    
    def test_extract_data(self):
        with self.subTest(msg="Extract data group chat check"):
            self.assertEqual(self.controller.extract_data("test1Group"),self.testGroup)
        with self.subTest(msg="Extract data private chat check"):
            self.assertEqual(self.controller.extract_data("test2Private"),self.testPrivate)
        with self.subTest(msg="Extract data multiple files check"):
            self.assertEqual(self.controller.extract_data("test3Multiple"),self.testMultiple)

    def test_load_data(self):
        self.controller.load_data()
        with self.subTest(msg="Load config directory check"):
            self.assertEqual(self.controller.directory,"C:/Users/lukas/Desktop/Skola/ING/2rocnik/ZS/ESS/CounterForMessenger-master/stubs/")
        with self.subTest(msg="Load config user check"):
            self.assertEqual(self.controller.username,"User1")
        with self.subTest(msg="Load config language check"):
            self.assertEqual(self.controller.language,"English")

    def test_statistics_popup(self):
        popup=StatisticsPopup(self.controller,"test1Group")
        with self.subTest(msg="Statistics pop-up group check"):
            self.assertEqual(len(popup.children),13)
            self.assertEqual(popup._last_child_ids,{'label': 10, 'scrollbar': 1, 'listbox': 2})
        popup.destroy()
        popup=StatisticsPopup(self.controller,"test2Private")
        with self.subTest(msg="Statistics pop-up private check"):
            self.assertEqual(len(popup.children),12)
            self.assertEqual(popup._last_child_ids,{'label': 10, 'listbox': 2})
    
    def test_update_data(self):
        self.controller.update_data("User1", "C:/Users/lukas/Desktop/Skola/ING/2rocnik/ZS/ESS/CounterForMessenger-master/stubs/", "English")
        with self.subTest(msg="Update data directory check"):
            self.assertEqual(self.controller.directory,"C:/Users/lukas/Desktop/Skola/ING/2rocnik/ZS/ESS/CounterForMessenger-master/stubs/")
        with self.subTest(msg="Update data user check"):
            self.assertEqual(self.controller.username,"User1")
        with self.subTest(msg="Update data language check"):
            self.assertEqual(self.controller.language,"English")
        with self.subTest(msg="Update data config file check"):
            with open("config.txt",'r') as file:
                self.assertEqual(file.read(),"User1\nC:/Users/lukas/Desktop/Skola/ING/2rocnik/ZS/ESS/CounterForMessenger-master/stubs/\nEnglish")

    def test_get_language(self):
        with self.subTest(msg="Valid language check"):
            self.controller.language="Polski"
            self.assertEqual(self.controller.get_language(),"Polski")
        with self.subTest(msg="Invalid language check"):
            self.controller.language="Nonsense"
            self.assertEqual(self.controller.get_language(),"English")
    
    
if __name__ == '__main__':
    sys.tracebacklimit = 0
    unittest.main()
