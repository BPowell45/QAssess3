import sqlite3
conn = sqlite3.connect('assessDB.db')
cursor = conn.cursor()

# Category: History
cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

# Category: Management
cursor.execute('''CREATE TABLE IF NOT EXISTS management (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

# Category: Database
cursor.execute('''CREATE TABLE IF NOT EXISTS database (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

# Category: Python
cursor.execute('''CREATE TABLE IF NOT EXISTS python (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')

# Category: Accounting
cursor.execute('''CREATE TABLE IF NOT EXISTS accounting (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL
                )''')


history_data = [
    ("Who was the first President of the United States?", "George Washington"),
    ("When did World War II end?", "1945"),
    ("What year was the Declaration of Independence signed?", "1776"),
    ("What was the name of the first permanent English settlement in America?","Jamestown Virginia"),
    ("Who was the main author of the Declaration of Independence?","Thomas Jefferson"),
    ("Who served as the first Secretary of the Treasury under President George Washington?","Alexander Hamilton"),
    ("Who was the primary author of the Bill of Rights?","James Madison"),
    ("Who was the commander-in-chief of the Continental Army during the American Revolutionary War?","George Washington"),
    ("What was the name of the document that established the framework for government in the newly independent United States before the Constitution?","Articles of Confederation"),
    ("What event led to the Boston Tea Party?","British Taxes")
]

management_data = [
    ("What trait involves inspiring and motivating others?", "Charisma"),
    ("What skill involves effectively communicating with team members?", "Communication"),
    ("What quality involves being honest and transparent?", "Integrity"),
    ("What attribute involves making decisions confidently?","Decisiveness"),
    ("What characteristic involves being open to feedback and learning?","Adaptability"),
    ("What trait involves having a clear vision for the team or organization?","Visionary"),
    ("What skill involves empowering and trusting others to take initiative?","Delegation"),
    ("What quality involves remaining calm and composed under pressure?","Resilience"),
    ("What attribute involves being empathetic and understanding towards others?","Empathy"),
    ("What characteristic involves being accountable and taking responsibility for actions?","Accountability")
]

database_data = [
    ("What is 'red light' in the stoplight analogy", "Many to many"),
    ("What is 'yellow light'?", "One to One"),
    ("What is 'green light'?", "Many to one"),
    ("An attribute or collection of attributes that could be the primary key","Candidate Key"),
    ("An Attribute or collection of attributes that can be used to uniquely identify a row (example T#) (Underline it), the chosen candidate key","Primary Key"),
    ("(do not have to be unique): Used to access data or group data in a particular order. Example: Indexes, sorting by major","Secondary Key"),
    ("An attribute in one table that contains the value of a primary key in another table (Used to create relationships to other tables)","Foreign Key"),
    ("key made of more than one attribute","Compound Key"),
    ("1 entity relates to itself","Unary"),
    ("2 entities in relationship","Binary")
]

python_data = [
    ("What is Python?", "Language"),
    ("What is Python's primary use?", "Programming"),
    ("How are Python programs executed?", "Interpreted"),
    ("What type of language is Python?", "High-level"),
    (" What is Python's syntax known for?", "Readability"),
    ("What are Python files typically saved with?", ".py"),
    ("What is Python's built-in documentation system?", "Docstrings"),
    ("What is the primary data structure in Python?", "List"),
    ("What is the name of Python's package manager?", "Pip"),
    ("What is Python's object-oriented programming feature called?", "Classes")
]

accounting_data = [
    ("What is the process of recording financial transactions?", "Recording"),
    ("What is the term for the systematic classification and summarization of financial data?", "Analysis"),
    ("What type of account reflects a company's assets, liabilities, and equity at a specific point in time?", "Balance"),
    ("What do we call the monetary amount owed by a business to its suppliers for goods or services purchased on credit?", "Accounts Payable"),
    ("What term refers to the difference between a company's revenue and its expenses?", "Profit"),
    ("What financial statement provides a snapshot of a company's financial position?", "Balance Sheet"),
    ("What term describes the process of matching revenues with the expenses incurred to generate them?", "Matching"),
    ("What do we call the process of examining financial statements to ensure accuracy and compliance with regulations?", "Auditing"),
    ("What type of account records the revenue earned by a business from its normal business operations?", "Income"),
    ("What term refers to the systematic process of communicating financial information to internal and external users?", "Reporting")
]

cursor.executemany("INSERT INTO history (question, answer) VALUES (?, ?)", history_data)
cursor.executemany("INSERT INTO management (question, answer) VALUES (?, ?)", management_data)
cursor.executemany("INSERT INTO database (question, answer) VALUES (?, ?)", database_data)
cursor.executemany("INSERT INTO python (question, answer) VALUES (?, ?)", python_data)
cursor.executemany("INSERT INTO accounting (question, answer) VALUES (?, ?)", accounting_data)

conn.commit()
conn.close()

print("Database 'assessDB.db' with multiple tables created successfully!")