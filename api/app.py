#!/usr/bin/python3

from flask import Flask, jsonify, request
import joblib
import mysql.connector

app = Flask(_name_)

# Load the model
model = joblib.load('model.pkl')

# Connect to the database
def get_song_details(song_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="music_recommendation"
    )
    
    cursor = connection.cursor()
    query = f"SELECT title, artist FROM songs WHERE id = {song_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        return {"id": song_id, "title": result[0], "artist": result[1]}
    else:
        return None

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    num_recommendations = int(request.args.get('n', 5))
    recommendations = model.recommend(user_id, num_recommendations)
    
    result = []
    for song_id, rating in recommendations:
        song_details = get_song_details(song_id)
        if song_details:
            result.append({"song": song_details, "predicted_rating": rating})
    
    return jsonify(result)

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
