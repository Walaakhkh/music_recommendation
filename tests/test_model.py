#!/usr/bin/python3

import unittest
from model.collaborative_filtering import CollaborativeFilteringModel
import pandas as pd

class TestCollaborativeFilteringModel(unittest.TestCase):
    
    def setUp(self):
        data = {'user_id': [1, 2, 3], 'song_id': [1, 2, 3], 'rating': [4, 5, 3]}
        self.df = pd.DataFrame(data)
        self.model = CollaborativeFilteringModel(self.df)
        self.model.train()

    def test_recommend(self):
        recommendations = self.model.recommend(1, num_recommendations=2)
        self.assertEqual(len(recommendations), 2)

if _name_ == "_main_":
    unittest.main()
