import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Load user-song interactions from the database
def load_interactions():
    # Use Django ORM to get interaction data
    from .models import UserSongInteraction
    interactions = UserSongInteraction.objects.all().values('user_id', 'song_id', 'interaction_type')
    df = pd.DataFrame(list(interactions))
    df = df[df['interaction_type'] == 'like']  # Filter by 'like' interactions only
    return df

# Create recommendation model using Collaborative Filtering (SVD)
def train_model():
    data = load_interactions()
    reader = Reader(rating_scale=(1, 5))
    dataset = Dataset.load_from_df(data[['user_id', 'song_id', 'rating']], reader)
    trainset, testset = train_test_split(dataset, test_size=0.2)

    # Use SVD algorithm
    algo = SVD()
    algo.fit(trainset)

    return algo


def recommend_songs(user_id, n=10):
    algo = train_model()  # Train the model
    from .models import Song

    # Predict ratings for all songs the user hasn't listened to
    songs = Song.objects.all()
    predictions = []
    for song in songs:
        pred = algo.predict(user_id, song.id)
        predictions.append((song, pred.est))

    # Sort by predicted rating and return top N recommendations
    predictions.sort(key=lambda x: x[1], reverse=True)
    recommended_songs = [p[0] for p in predictions[:n]]
    return recommended_songs
