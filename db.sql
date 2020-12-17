CREATE DATABASE happiness;
USE happiness;
CREATE TABLE user(
					user_username VARCHAR(15) NOT NULL UNIQUE,
					user_fullname VARCHAR(100) NOT NULL,
					user_password VARCHAR(100) NOT NULL,
					PRIMARY KEY(user_username));
CREATE TABLE doctor(
					doctor_username VARCHAR(15) NOT NULL UNIQUE,
					doctor_fullname VARCHAR(100) NOT NULL,
					doctor_field VARCHAR(100) NOT NULL,
					doctor_hospital VARCHAR(100) NOT NULL,
					doctor_graduation VARCHAR(100) NOT NULL,
					doctor_experience VARCHAR(100) NOT NULL,
					PRIMARY KEY(doctor_username));

INSERT INTO doctor VALUES ('rajesh', 'Rajesh Kumar', 
                    'Ophthalmology', 'Aster MediCity, Cochin','Calicut Medical College',
                    '12 years of experience');
INSERT INTO doctor VALUES ('rithesh', 'Rithesh Raj', 
                    'Ophthalmology', 'Aster MediCity, Cochin','Calicut Medical College',
                    '10 years of experience'); 
INSERT INTO doctor VALUES ('amal', 'Amal KV', 
                    'Radiology', 'Aster MediCity, Cochin','Calicut Medical College',
                    '2 years of experience'); 
INSERT INTO doctor VALUES ('basil', 'Basil Jiji', 
                    'ENT', 'Aster MediCity, Cochin','Calicut Medical College',
                    '12 years of experience'); 
INSERT INTO doctor VALUES ('latheef', 'Latheef J', 
                    'Audiology & Speech-Language Pathology', 'Aster MediCity, Cochin','Calicut Medical College',
                    '7 years of experience'); 
INSERT INTO doctor VALUES ('waseem', 'Waseem T', 
                    'Physiology', 'Aster MediCity, Cochin','Calicut Medical College',
                    '12 years of experience'); 
INSERT INTO doctor VALUES ('vishnu', 'Vishnu Vijayan', 
                    'Clinical Pharmacology', 'Aster MediCity, Cochin','Calicut Medical College',
                    '4 years of experience'); 
INSERT INTO doctor VALUES ('rahul', 'Rahul R', 
                    'Cardiac & Cardiovascular Systems', 'Aster MediCity, Cochin','Calicut Medical College',
                    '10 years of experience'); 
INSERT INTO doctor VALUES ('manu', 'Manu Mohan', 
                    'Anesthesiology & Pain Medicine', 'Aster MediCity, Cochin','Calicut Medical College',
                    '12 years of experience'); 
INSERT INTO doctor VALUES ('tijin', 'Tijin Kumar', 
                    'Biomedical Engineering', 'Aster MediCity, Cochin','Calicut Medical College',
                    '12 years of experience'); 
INSERT INTO doctor VALUES ('anupeter', 'Anu Peter', 
                    'Clinical Pharmacology', 'Aster MediCity, Cochin','Calicut Medical College',
                    '12 years of experience'); 
INSERT INTO doctor VALUES ('aparna', 'Aparna LT', 
                    'Forensic Medicine', 'Aster MediCity, Cochin','Calicut Medical College',
                    '12 years of experience'); 
INSERT INTO doctor VALUES ('keerthana', 'Keerthana Rajesh', 
                    'Ophthalmology', 'Aster MediCity, Cochin','Calicut Medical College',
                    '12 years of experience'); 