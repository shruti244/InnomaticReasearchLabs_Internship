import pandas as pd
import sqlite3
from flask import Flask, render_template, request
import os

# Check if database exists
DB_PATH = "eng_subtitles_database (1).db"
print("Database exists:", os.path.exists(DB_PATH))

app = Flask(__name__)

# Load database into a Pandas DataFrame
df = None  # Initialize df

try:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT num, name, content FROM zipfiles", conn)
    conn.close()
    print("Database loaded successfully!")
except Exception as e:
    print(f"Error loading database: {e}")

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_text = request.form.get("search_text")

        if search_text and df is not None:
            # Ensure 'content' column exists and perform a case-insensitive search
            if "content" in df.columns:
                df["content"] = df["content"].str.decode("latin-1")  # Convert bytes to string
                results = df[df['content'].str.contains(search_text, case=False, na=False)]['name'].tolist()

            else:
                results = ["Error: 'content' column missing in database"]
            
            return render_template("results.html", search_text=search_text, results=results)
        else:
            return render_template("results.html", search_text="Nothing", results=None)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
