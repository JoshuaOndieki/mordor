import unittest
from functions import *

class TestMordor(unittest.TestCase):
    def test_add_skills(self):
        skills=add_skill("Coding")
        self.assertTrue(isinstance(skills,dict))
        self.assertEqual(skills["Coding"],"Incomplete")

    def test_complete_skill(self):
        skills=complete_skill("Coding")
        self.assertEqual(skills["Coding"],"Complete")

    def test_view_skills(self):
        skills=view_skills()
        self.assertTrue(isinstance(skills,dict))

    def test_progress(self):
        skills={"Skill":"Complete","Skill1":"Incomplete","Skill3":"Complete","skill4":"Complete"}
        percent_progress=progress(skills)
        self.assertEqual(percent_progress,75)

if __name__=="__main":
    unittest.main()
