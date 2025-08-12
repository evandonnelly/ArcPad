from typing import List
from datetime import datetime
import uuid
import streamlit as st
from Match import Match
from Session import Session
import json
from Warmup import Warmup
from Focus import Focus
import sqlite3

st.title("Arc Pad v0.0.1")

conn = sqlite3.connect("sessiondata.db")
cursor = conn.cursor()

# ---------------------------------------------------------------------------------
# SQL TABLES
# ---------------------------------------------------------------------------------

# Warmups table
cursor.execute('''
CREATE TABLE IF NOT EXISTS warmups (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
)
''')

# Focuses table
cursor.execute('''
CREATE TABLE IF NOT EXISTS focuses (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    cue TEXT,
    action TEXT
)
''')

# Gametitles table
cursor.execute('''
CREATE TABLE IF NOT EXISTS gametitles (
   id TEXT PRIMARY KEY,
   title TEXT NOT NULL UNIQUE
)
''')

# Sessions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,
    date TEXT NOT NULL,
    game_id TEXT,
    warmup_id TEXT,
    focus_id TEXT,
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (warmup_id) REFERENCES warmups(id),
    FOREIGN KEY (focus_id) REFERENCES focuses(id)
)
''')

# Matches table
cursor.execute('''
CREATE TABLE IF NOT EXISTS matches (
    match_id TEXT PRIMARY KEY,
    session_id TEXT,
    outcome TEXT,
    mental TEXT,
    FOREIGN KEY (session_id) REFERENCES sessions(id)
)
''')

# Observations table
cursor.execute('''
CREATE TABLE IF NOT EXISTS observations (
    observation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id TEXT,
    content TEXT NOT NULL,
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
)
''')

# Analysis table
cursor.execute('''
CREATE TABLE IF NOT EXISTS analysis (
    analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id TEXT,
    content TEXT NOT NULL,
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
)
''')

conn.commit()

# ---------------------------------------------------------------------------------
# POPULATE TABLES WITH TEST DATA
# ---------------------------------------------------------------------------------

def populateTestData():
    # Warmups
    warmup_id = str(uuid.uuid4())
    cursor.insert("INSERT INTO warmups VALUES (?, ?, ?)", (warmup_id, ))

def newUUID():
    return str(uuid.uuid4())

def defaultMatchID():
    return datetime.now().strftime("%Y.%m.%d.%H.%M.%S")

populateTestData()