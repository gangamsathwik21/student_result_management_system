CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(20),
    name VARCHAR(50),
    math_marks FLOAT,
    science_marks FLOAT,
    english_marks FLOAT,
    total_marks FLOAT,
    average_marks FLOAT,
    status VARCHAR(10)
);