import sqlite3
import requests
from bs4 import BeautifulSoup
import time 

def fetch_and_store_problem_info(url):
    def fetch_problem_title_and_difficulty(url):
        # Fetch the HTML content of the URL
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
        response = requests.get(url,headers=headers)
        time.sleep(0.3)
        
        # Check if the request was successful
        problem_title=None
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the problem title
            title_div = soup.find('div', class_='problemindexholder')
            if title_div:
                typography_div = title_div.find('div', class_='ttypography')
                if typography_div:
                    header_div = typography_div.find('div', class_='header')
                    if header_div:
                        title_div_in_header = header_div.find('div', class_='title')
                        if title_div_in_header:
                            problem_title = title_div_in_header.get_text().strip()
                            # Remove characters from the front until the first period
                            problem_title = problem_title.split('.', 1)[-1].strip()
            
            # Find the difficulty level
            if(problem_title==None):
                return None , None
            difficulty = None
            roundbox_divs = soup.find_all('div', class_='roundbox')
            for roundbox_div in roundbox_divs:
                span_difficulty = roundbox_div.find('span', class_='tag-box', title='Difficulty')
                if span_difficulty:
                    difficulty_text = span_difficulty.get_text().strip()
                    # Remove the first character
                    difficulty = difficulty_text[1:] if difficulty_text else None
                    break
            
            return problem_title, difficulty
        
        else:
            print("Failed to fetch URL:", url)
            return None, None

    def create_db_and_table():
        # Connect to the database (or create it if it doesn't exist)
        conn = sqlite3.connect('CFproblems.db')
        cursor = conn.cursor()
        
        # Create the table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS problem_table 
                          (probName TEXT UNIQUE, link TEXT UNIQUE, rating TEXT )''')
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    def insert_into_db(prob_name, link, rating):
        # Connect to the database
        conn = sqlite3.connect('CFproblems.db')
        cursor = conn.cursor()
        
        try:
            # Insert values into the table
            cursor.execute("INSERT INTO problem_table VALUES (?, ?, ?)", (prob_name, link, rating))
            conn.commit()
        except sqlite3.IntegrityError:
            print("Integrity error occurred. Skipping insertion for:", prob_name, link, rating)
            conn.rollback()
        
        # Close the connection
        conn.close()

    # Test the functions with the provided URL
    prob_name, rating = fetch_problem_title_and_difficulty(url)

    if prob_name:
        print("Problem Title:", prob_name)
    else:
        print("Problem Title not found.")

    if rating:
        print("Difficulty:", rating)
    else:
        print("Difficulty not found.")

    # Create the database and table if they don't exist
    create_db_and_table()

    # Insert values into the table only when both probName and rating are available
    if prob_name and rating:

        try:
            insert_into_db(prob_name, url, rating)
        except:
            print("failed for ",url[len(url)-1])

for i in range(1950,1971):
    url = f"https://codeforces.com/problemset/problem/{i}/"
    for j in ["A","A1","A2","B","B1","B2","C","C1","C2","D","D1","D2","E","E1","E2","F","F1","F2","G","G1","G2","H","H1","H2","J","J1","J2" ]:
        nurl=url+j
        try:
            fetch_and_store_problem_info(nurl)
        except Exception as e:
            print(e)
            break
