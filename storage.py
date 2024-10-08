import sqlite3
import os

DB_FILE = 'ayum_game.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS game_state (
        id INTEGER PRIMARY KEY,
        health INTEGER,
        health_limit INTEGER,
        hunger REAL,
        hunger_limit INTEGER,
        age INTEGER,
        sleep REAL,
        sleep_limit INTEGER,
        attack INTEGER,
        attack_limit INTEGER,
        food_inventory TEXT
    )
    ''')
    conn.commit()
    conn.close()

def save_game(ayum):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Convert food_inventory to a string representation
    food_inventory = ','.join([food.name if food is not None else 'Empty' for food in ayum.food_inventory])
    
    cursor.execute('''
    INSERT OR REPLACE INTO game_state 
    (id, health, health_limit, hunger, hunger_limit, age, sleep, sleep_limit, attack, attack_limit, food_inventory) 
    VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ayum.health, ayum.health_limit, ayum.hunger, ayum.hunger_limit, ayum.age, 
          ayum.sleep, ayum.sleep_limit, ayum.attack, ayum.attack_limit, food_inventory))
    
    conn.commit()
    conn.close()

def load_game():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM game_state WHERE id = 1')
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return {
            'health': row[1],
            'health_limit': row[2],
            'hunger': row[3],
            'hunger_limit': row[4],
            'age': row[5],
            'sleep': row[6],
            'sleep_limit': row[7],
            'attack': row[8],
            'attack_limit': row[9],
            'food_inventory': [name if name != 'Empty' else None for name in row[10].split(',') if row[10]]
        }
    return None

def reset_game():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    init_db()

# Initialize the database when this module is imported
init_db()