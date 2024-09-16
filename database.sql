-- Create a new database music_recommendation if not exist
CREATE DATABASE IF NOT EXISTS music_recommendation;

-- Use the new database
USE music_recommendation;

-- Create the users table if it does not exist
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the songs table if it does not exist
CREATE TABLE IF NOT EXISTS songs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    year INT
);

-- Create the user_song_interactions table if it does not exist
CREATE TABLE  IF NOT EXISTS user_song_interactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    song_id INT,
    interaction_type ENUM('listen', 'like', 'skip') NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (song_id) REFERENCES songs(id)
);
