from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in the app







@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO User (NAME, WEIGHT, HEIGHT, AGE, ALLERGIES) VALUES (?, ?, ?, ?, ?)",
                   (data['name'], data['weight'], data['height'], data['age'], data['allergies']))
    cursor.execute('SELECT * FROM User ORDER BY ROWID DESC LIMIT 1')
    data = cursor.fetchone()
    #conn.commit()
    conn.close()
    return jsonify(data), 201

@app.route('/get_users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users), 200





@app.route('/send_diet', methods=['POST'])
def get_food_items():

    food_data = request.get_json()
    food_group = food_data.get('food_group')  # Access the 'food_group' value

    print('Received food group:', food_group)
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()


    if food_group:
        cursor.execute('SELECT * FROM FOOD WHERE food_group = ?', (food_group,))
    else:
        cursor.execute('SELECT * FROM FOOD')
    
    data = cursor.fetchall()
    foods = []
    conn.close()
    return jsonify(data)


 
@app.route('/send_workouts', methods=['POST'])
def send_workouts():
    # Get the JSON data sent from the frontend
    selected_workouts = request.json
    workouts = []
    days_and_workouts = []

    # Print the received data for debugging
    print('Received selected workouts:', selected_workouts)
    #Received selected workouts: {'monday': ['Shoulder', 'Legs']}
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()


    for day, body_parts in selected_workouts.items():
        for body_part in body_parts:
            cursor.execute('''
                SELECT * FROM EXERCISES
                WHERE BODY_PART = ?''', (body_part,))
            exercises = cursor.fetchall()
            workouts.extend(exercises)
        days_and_workouts.append({day : workouts})
        

    print(workouts)
    print(days_and_workouts)
    # Process the received workouts here (e.g., save to database)
    # For demonstration purposes, let's just return a success message
    return jsonify({'workouts': days_and_workouts})











if __name__ == '__main__':
    app.run(debug=True)


































































































"""conn = sqlite3.connect('gym.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Function to check if a table exists
def table_exists(table_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name =?", (table_name,))
    return cursor.fetchone() 

if not table_exists('User'):    
# Execute the CREATE TABLE statement for User
    cursor.execute('''
        CREATE TABLE User (
            CWID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(255),
            WEIGHT INTEGER,
            HEIGHT INTEGER,
            AGE INTEGER,
            ALLERGIES VARCHAR(255)
        )
    ''')

if not table_exists('DIET'):
    #relationship for user and food, 1 to N
    cursor.execute('''
        CREATE TABLE DIET (
            FWID INTEGER,
            FFID INTEGER,
            FOREIGN KEY (FWID) REFERENCES User(CWID) ON DELETE CASCADE,
            FOREIGN KEY (FFID) REFERENCES FOOD(FOOD_ID) ON DELETE CASCADE
        )
    ''')
if not table_exists('DAYS'):
    #multivalue attribute for Days in User
    cursor.execute('''
        CREATE TABLE DAYS (
            FWID INTEGER,
            DAY VARCHAR(255),
            FOREIGN KEY (FWID) REFERENCES User(CWID) ON DELETE CASCADE
        )
    ''')
if not table_exists('FOOD'):
# Execute the CREATE TABLE statement for FOOD
    cursor.execute('''
        CREATE TABLE FOOD (
            FOOD_NAME VARCHAR(255),
            FOOD_ID INT NOT NULL PRIMARY KEY,
            CALORIES INT,
            CARBS INT,
            FATS INT,
            PROTEINS INT,
            FIBER INT,
            FOOD_GROUP CHAR(9),
            RESTRICTION VARCHAR(255)
        )
    ''')

if not table_exists('EXERCISES'):
    #create table for exercise
    cursor.execute('''
        CREATE TABLE EXERCISES (
            EXERCISE_ID INT NOT NULL PRIMARY KEY,
            EXERCISE_NAME VARCHAR(255),
            REPS INT,
            SETS INT

        )
    ''')
if not table_exists('WORKOUT'):
    #create relationship between exercises and user
    cursor.execute('''
        CREATE TABLE WORKOUT (
            FWID INTEGER,
            F_EXERCISES INTEGER,
            FOREIGN KEY (FWID) REFERENCES User(CWID) ON DELETE CASCADE,
            FOREIGN KEY (F_EXERCISES) REFERENCES EXERCISES(EXERCISE_ID) ON DELETE CASCADE
        )
    ''')
if not table_exists('MUSCLE_GROUP'):
    #create multivalue for muscle group for exercise
    cursor.execute('''
        CREATE TABLE MUSCLE_GROUP (
            FEX_ID INTEGER,
            MUSCLE VARCHAR,
            FOREIGN KEY (FEX_ID) REFERENCES EXERCISES(EXERCISE_ID) ON DELETE CASCADE

        )
    ''')


# Insert sample data into FOOD table
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Oatmeal w/ friut', 1001, 187, 34, 2, 5, 4, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Toast w/ eggs & OJ', 1002, 508, 46, 11, 11, 2, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Toast w/ sausage & OJ', 1003, 447, 59, 18, 13, 2, 'Hight-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('English muffin w/ sausage', 1004, 322, 27, 18, 12, 2, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Granola w/ fruit & yogurt', 1005, 125, 24, 2, 5, 2, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Whole-wheat pancakes w/ syrup', 1006, 324, 38, 14, 11, 5, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Green smoothie', 1007, 120, 30, 0, 3, 5, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Açaí bowl', 1008, 70, 4, 5, 1, 3, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Avocado toast', 1009, 179, 16, 14, 4, 8, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Mixed berries & banana smoothie', 1010, 168, 38, 1, 0, 3, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Mango smoothie', 1011, 120, 22, 2, 5, 2, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Egg & cheese omelet', 1012, 177, 1, 15, 10, 0, 'Hight-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Veggie omelet', 1013, 620, 19, 44, 37, 3, 'Vegetarian')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('English muffin w/ veggie4-sausage', 1014, 202, 29, 4, 14, 2, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Toast w/ veggie-sausage & OJ', 1015, 327, 61, 4, 15, 2, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Yogurt w/ banana', 1016, 113, 21, 2, 5, 0, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Bagel w/ peanut butter & sliced banana', 1017, 385, 74, 10, 13, 10, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Bagel w/ cream cheese & sliced banana', 1018, 114, 18, 0, 11, 2, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Begel w/ cream cheese & yogurt', 1019, 528, 68, 19, 22, 2, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Breakfast burrito w/ eggs & sausage', 1020, 277, 21, 16, 11, 1, 'Vegetarian')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Breakfast burrito w/ eggs & veggie-sausage', 1021, 157, 23, 2, 13, 1, 'Vegetarian')")

cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Taco salad', 1022, 400, 25, 20, 25, 8, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Baked salmon', 1023, 250, 0, 15, 30, 0, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Grilled shrimp w/ rice & veggies', 1024, 350, 0, 15, 30, 0, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Cauliflower fried rice', 1025, 200, 15, 10, 5, 5, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Vegetarian enchiladas', 1026, 350, 30, 15, 20, 8, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Pizza w/ tomato, mozzarella & basil', 1027, 300, 30, 15, 15, 3, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Sweet & tangy chicken burger', 1028, 350, 30, 15, 25, 4, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Kale & apple salad', 1029, 200, 20, 10, 5, 5, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Chicken ranch salad', 1030, 300, 15, 20, 25, 4, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Chicken caesar salad', 1031, 350, 20, 25, 25, 3, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Caesar salad', 1032, 250, 15, 20, 10, 3, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Asian chopped chicken salad', 1033, 300, 25, 15, 20, 6, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Tuscan kale salad', 1034, 200, 20, 10, 5, 7, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Turkey tacos', 1035, 300, 20, 15, 20, 5, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Healthy BBQ salmon sheet pan dinner', 1036, 350, 30, 15, 25, 4, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Hummus & grilled Veggie wrap', 1037, 300, 35, 15, 10, 8, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Grilled chicken and veggie wrap', 1038, 350, 30, 15, 20, 6, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Chicken noodle soup', 1039, 250, 20, 10, 15, 3, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Asian chicken rice bowl', 1040, 400, 40, 15, 25, 5, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Tuna salad sandwich', 1041, 350, 25, 20, 20, 4, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Ham & cheese sandwich on wheat w/ light mayo, lettuce & tomato', 1042, 350, 30, 15, 20, 4, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Chili', 1043, 300, 25, 15, 20, 8, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Veggie chili', 1044, 250, 20, 10, 15, 10, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Vegetable soup', 1045, 200, 20, 5, 10, 8, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Green smoothie', 1046, 150, 25, 5, 5, 5, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Açaí bowl', 1047, 300, 40, 10, 10, 8, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Energy bar', 1048, 250, 30, 10, 15, 5, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Beefy baked potato', 1049, 400, 30, 20, 20, 6, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Baked potato', 1050, 250, 40, 5, 5, 6, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Turkey burger', 1051, 300, 20, 15, 25, 4, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Beyond burger', 1052, 300, 20, 20, 20, 5, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Chicken, rice, & veggie stir-fry', 1053, 400, 35, 10, 25, 6, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Vegan pasta', 1054, 350, 40, 15, 15, 6, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Chicken pasta w/ bread', 1055, 450, 50, 20, 20, 5, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Pasta w/ veggies', 1056, 300, 40, 10, 10, 8, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Homemade mac & cheese', 1057, 400, 30, 20, 15, 2, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Orange chicken & veggie stir-fry', 1058, 350, 30, 15, 20, 5, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Ants on a log', 1059, 150, 15, 5, 5, 3, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Stir-fried brown rice w/ chicken', 1060, 350, 40, 15, 20, 5, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Salmon w/ kale & apple salad', 1061, 350, 25, 20, 25, 6, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Tai basil chicken', 1062, 350, 30, 15, 25, 4, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Vegetable noodle soup', 1063, 200, 25, 5, 10, 6, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Turkey & cheese wrap w/ mayo, lettuce & tomato in a flour tortilla', 1064, 400, 30, 20, 20, 4, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Turkey & cheese sandwich on wheat w/ light mayo, lettuce & tomato', 1065, 350, 30, 15, 20, 4, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Beans, rice, & veggie bowl', 1066, 350, 50, 5, 15, 10, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Turkey meatballs', 1067, 300, 10, 15, 25, 2, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Veggie meatballs', 1068, 250, 20, 10, 15, 8, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Vegetable & tofu stir-fry', 1069, 250, 25, 10, 15, 8, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Egg salad lettuce wrap', 1070, 250, 10, 20, 15, 3, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Grilled turkey panini on wheat', 1071, 400, 30, 20, 25, 4, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Grilled veggie panini on wheat', 1072, 350, 40, 15, 10, 6, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Whole wheat pita pizza w/ veggies', 1073, 300, 35, 10, 15, 5, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Thai peanet tofu w/ rice', 1074, 400, 45, 15, 20, 6, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Lentil & vegetable curry', 1075, 300, 40, 10, 15, 10, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Beef stew', 1076, 350, 20, 15, 25, 5, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Fruit salad (strawberries, blueberries, banana, etc)', 1077, 150, 35, 0, 2, 5, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Fruit salad w/ granola & yogurt (strawberries, blueberries, banana, etc)', 1078, 250, 40, 5, 10, 6, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Turkey & greens', 1079, 300, 15, 15, 25, 5, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Caprese salad w/ grilled chicken', 1080, 350, 10, 20, 30, 3, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Whole wheat pita pizza w/ grilled chicken & veggies', 1081, 400, 40, 15, 25, 6, 'Balanced')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Sushi (Califfornia roll)', 1082, 300, 45, 5, 15, 3, 'Low-carb')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Vegetable shushi roll', 1083, 250, 40, 5, 10, 6, 'Vegan')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Mediterranean-style meatballs', 1084, 350, 10, 25, 20, 5, 'High-protein')")
cursor.execute("INSERT INTO FOOD (FOOD_NAME, FOOD_ID, CALORIES, CARBS, FATS, PROTEINS, FIBER, FOOD_GROUP) VALUES ('Spaghetti & turkey meatballs', 1085, 400, 40, 15, 25, 6, 'Balanced')")


# User table input
#cursor.execute("INSERT INTO USER (CWID, NAME, WEIGHT, HEIGHT, AGE, ALLERGIES) VALUES (000000001, 'Christopher Contreras', 170, 70, 21, 'NONE')")
#cursor.execute("INSERT INTO USER (CWID, NAME, WEIGHT, HEIGHT, AGE, ALLERGIES) VALUES (000000002, 'Mason Jennings', 165, 67, 23, 'NONE')")
#cursor.execute("INSERT INTO USER (CWID, NAME, WEIGHT, HEIGHT, AGE, ALLERGIES) VALUES (000000003, 'Vamsi Mannava', 160, 69, 22, 'NONE')")
#cursor.execute("INSERT INTO USER (CWID, NAME, WEIGHT, HEIGHT, AGE, ALLERGIES) VALUES (000000004, 'Kush Patel', 175, 67, 21, 'NONE')")
#cursor.execute("INSERT INTO USER (CWID, NAME, WEIGHT, HEIGHT, AGE, ALLERGIES) VALUES (000000005, 'Moksh Patel', 175, 65, 22, 'NONE')")
#cursor.execute("INSERT INTO USER (CWID, NAME, WEIGHT, HEIGHT, AGE, ALLERGIES) VALUES (885269381, 'Mark Perez', 170, 67, 32, 'EGGS')")

# EXERCISES table input
            #EXERCISE_ID INT NOT NULL PRIMARY KEY,
            #EXERCISE_NAME VARCHAR(255),
            #REPS INT,
            #SETS INT
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0101, 'Standing Military Press', 12, 3)")

cursor.execute("SELECT * FROM FOOD")


rows = cursor.fetchall()

def connect_db():
    return rows

conn.close()

















@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    #conn = sqlite3.connect('gym.db')
    #cursor = conn.cursor()
    cursor.execute("INSERT INTO User (NAME, WEIGHT, HEIGHT, AGE, ALLERGIES) VALUES (?, ?, ?, ?, ?)",
                   (data['name'], data['weight'], data['height'], data['age'], data['allergies']))
    #conn.commit()
    #conn.close()
    return jsonify({"message": "User created successfully"}), 201

@app.route('/get_users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('gym.db')
    #cursor = conn.cursor()
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    #conn.close()
    return jsonify(users), 200

@app.route('/update_user/<int:cwid>', methods=['PUT'])
def update_user(cwid):
    data = request.json
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE User SET NAME=?, WEIGHT=?, HEIGHT=?, AGE=?, ALLERGIES=? WHERE CWID=?",
                   (data['name'], data['weight'], data['height'], data['age'], data['allergies'], cwid))
    conn.commit()
    conn.close()
    return jsonify({"message": "User updated successfully"}), 200

@app.route('/delete_user/<int:cwid>', methods=['DELETE'])
def delete_user(cwid):
    #conn = sqlite3.connect('gym.db')
    #cursor = conn.cursor()
    cursor.execute("DELETE FROM User WHERE CWID=?", (cwid,))
    ##conn.commit()
    #conn.close()
    return jsonify({"message": "User deleted successfully"}), 200

#@app.route('/createworkoutplan', methods = ['POST'])
@app.route('/generate_workout_plan', methods=['POST'])
def generate_workout_plan():
    data = request.json  # Assuming the request contains the selected workouts data
    # Process the selected workouts and generate the workout plan here
    
    # For demonstration purposes, let's just echo back the received data
    workout_plan = {
        "monday": data.get("monday", []),
        "tuesday": data.get("tuesday", []),
        "wednesday": data.get("wednesday", []),
        "thursday": data.get("thursday", []),
        "friday": data.get("friday", []),
        "saturday": data.get("saturday", []),
        "sunday": data.get("sunday", []),
    }
    
    return jsonify(workout_plan), 200




@app.route('/get_diet', methods=['GET'])
def create_diet(food_group, restriction):
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM FOOD WHERE FOOD_GROUP = ? AND RESTRICTION IS NOT = ? ", (food_group, restriction,))
    users = cursor.fetchall()
    conn.close()
    return jsonify(users), 200
conn = sqlite3.connect('gym.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM FOOD ")
rows = cursor.fetchall()
print("Len ", len(rows))
for row in rows:
    print(row)'''
@app.route('/create_diet', methods=['POST'])
def create_diet():
    data = request.get_json()
    print(data)
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM FOOD WHERE FOOD_GROUP = ?", (data['food_group'],))
    food_items = cursor.fetchall()
    conn.close()

    # Print the fetched data
    for food_item in food_items:
        print(food_item)

    num_items = len(food_items)
    print("num items: ", num_items)

    return jsonify({"message": "User Diet created successfully", "num_items": num_items}), 201

    
"""

"""@app.route('/get_diet', methods=['GET'])
def get_diet():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM FOOD")
    food = cursor.fetchall()
    conn.close()
    return jsonify(food), 200"""
    
"""@app.route('/print_database', methods=['GET'])
def print_database():
    #conn = sqlite3.connect('gym.db')
    #cursor = conn.cursor()
    cursor.execute("SELECT * FROM FOOD ")
    rows = cursor.fetchall()
    print("Len ", len(rows))
    for row in rows:
        print(row)
    #conn.close()
    return "Database printed in console"
 
 # cursor.execute("DELETE FROM User WHERE CWID=?", (cwid,))
if __name__ == '__main__':
    app.run(debug=True)"""