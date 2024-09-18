#!/usr/bin/python3

import mysql.connector
import pandas as pd

# Data Preprocessing Script
def get_user_song_interaction():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="music_recommendation"
    )
    
    query = """
    SELECT user_id, song_id, rating
    FROM user_song_interaction;
    """
    df = pd.read_sql(query, connection)
    return df

# Training Script
if _name_ == '_main_':
    from collaborative_filtering import CollaborativeFilteringModel
    
    user_song_interaction_df = get_user_song_interaction()
    
    model = CollaborativeFilteringModel(user_song_interaction_df)
    model.train()
    
    # Save the trained model using joblib for later use
    import joblib
    joblib.dump(model, 'model.pkl')
