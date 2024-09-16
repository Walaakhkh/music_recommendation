from django.shortcuts import render
from .models import User
from .recommender import recommend_songs

def recommend_view(request, user_id):
    user = User.objects.get(id=user_id)
    recommended_songs = recommend_songs(user.id)

    return render(request, 'recommend/recommendations.html', {
        'user': user,
        'recommended_songs': recommended_songs
    })
