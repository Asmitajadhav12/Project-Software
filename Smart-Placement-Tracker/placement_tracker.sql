CREATE DATABASE placement_tracker;

USE placement_tracker;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    department VARCHAR(30),
    cgpa FLOAT,
    placed BOOLEAN DEFAULT FALSE
);

CREATE TABLE companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(50),
    min_cgpa FLOAT
);

CREATE TABLE interviews (
    interview_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    company_id INT,
    result VARCHAR(10),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
