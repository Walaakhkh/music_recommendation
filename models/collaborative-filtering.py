#!/usr/bin/python3

import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

class CollaborativeFilteringModel:
    def _init_(self, user_song_interaction_df):
        self.data = user_song_interaction_df
        self.model = SVD()

    def train(self):
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(self.data[['user_id', 'song_id', 'rating']], reader)
        trainset, testset = train_test_split(data, test_size=0.25)
        self.model.fit(trainset)

    def recommend(self, user_id, num_recommendations=5):
        song_ids = self.data['song_id'].unique()
        recommendations = []
        for song_id in song_ids:
            prediction = self.model.predict(user_id, song_id)
            recommendations.append((song_id, prediction.est))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:num_recommendations]
