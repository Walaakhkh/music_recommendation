CREATE DATABASE IF NOT EXISTS music_recommendation;
USE music_recommendation;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS songs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS user_song_interaction (
    user_id INT,
    song_id INT,
    rating FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (song_id) REFERENCES songs(id)
);
