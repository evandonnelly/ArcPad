from typing import List
import streamlit as st
from Match import Match
from Session import Session
import json
from Warmup import Warmup
from Focus import Focus
import sqlite3

st.title("Adjester")

conn = sqlite3.connect("sessiondata.db")
cursor = conn.cursor()

# ---------------------------------------------------------------------------------
# SQL TABLES
# ---------------------------------------------------------------------------------


