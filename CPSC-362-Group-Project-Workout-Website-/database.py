import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('gym.db')
cursor = conn.cursor()

# Create a table to store food items
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FOOD (
        id INTEGER PRIMARY KEY,
        name TEXT,
        calories INTEGER,
        carbohydrates FLOAT,
        proteins FLOAT,
        fats FLOAT,
        food_group TEXT
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS USER (
        CWID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(255),
        WEIGHT INTEGER,
        HEIGHT INTEGER,
        AGE INTEGER,
        ALLERGIES VARCHAR(255)
    )
''')




cursor.execute('''
    CREATE TABLE IF NOT EXISTS EXERCISES (
        CWID INTEGER PRIMARY KEY AUTOINCREMENT,
        BODY_PART VARCHAR(255),
        EXERCISE_NAME VARCHAR(255),
        REPS INTEGER,
        SETS INTEGER
    )
''')



exercise_data = [
    ('Legs', 'Squats', 10, 3),
    ('Chest', 'Bench Press', 8, 4),
    ('Back', 'Deadlifts', 12, 3),
    ('Shoulders', 'Military Press', 10, 3)
    # Additional exercises can be added here
]

# Insert sample data into the table
sample_data = [
    ('Oatmeal w/ fruit', 187, 34, 2, 5, 'Balanced'),
    ('Toast w/ eggs & OJ', 508, 46, 11, 11, 'Balanced'),
    ('Toast w/ sausage & OJ', 447, 59, 18, 13, 'High-protein'),
    ('Veggie omelet', 1013, 620, 37, 3, 'Vegetarian'),
    ('English muffin w/ veggie4-sausage', 1014, 4, 14, 2, 'Low-carb'),
    ('Toast w/ veggie-sausage & OJ', 1015, 61, 15, 2, 'Low-carb'),
    ('Yogurt w/ banana', 1016, 2, 5, 0, 'Vegan'),
    ('Bagel w/ peanut butter & sliced banana', 1017, 10, 13, 10, 'Vegan'),
    ('Breakfast burrito w/ eggs & sausage', 1020, 16, 11, 1, 'Vegetarian')

    # More data entries...
]

cursor.executemany('''
    INSERT INTO FOOD (name, calories, carbohydrates, proteins, fats, food_group)
    VALUES (?, ?, ?, ?, ?, ?)
''', sample_data)



cursor.executemany('''
    INSERT INTO EXERCISES (BODY_PART, EXERCISE_NAME, REPS,SETS)
    VALUES (?, ?, ?, ?)
''', exercise_data)

# Commit changes and close the connection
conn.commit()
conn.close()
