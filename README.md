# Supabase Database Demo

A simple Python application demonstrating cloud-managed PostgreSQL database operations using Supabase.

## Features

- ✨ Connect to Supabase PostgreSQL database
- 📝 Insert new messages
- 📖 Read all messages
- 🗑️ Delete messages
- ☁️ Data stored in the cloud

## Prerequisites

- Python 3.8+
- Free Supabase account ([supabase.com](https://supabase.com))

## Supabase Setup

### 1. Create a Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign up/login
2. Click **"New Project"**
3. Enter project name: `database-demo`
4. Set a database password
5. Select a region close to you
6. Click **"Create new project"**

### 2. Create the Messages Table

Go to **SQL Editor** in your Supabase dashboard and run:

```sql
-- Create messages table
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable Row Level Security (RLS)
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;

-- Create policy to allow all operations (for demo purposes)
CREATE POLICY "Allow all operations" ON messages
    FOR ALL
    USING (true)
    WITH CHECK (true);
```

### 3. Get Your API Credentials

1. Go to **Settings** > **API**
2. Copy:
   - **Project URL** (e.g., `https://xxxxx.supabase.co`)
   - **anon/public key** (under "Project API keys")

## Local Setup

### 1. Install Dependencies

```bash
cd supabase-database-demo
pip install -r requirements.txt
```

### 2. Configure Credentials

Edit `database_demo.py` and replace:

```python
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"
```

With your actual credentials from Supabase dashboard.

### 3. Run the Demo

```bash
python database_demo.py
```

## Expected Output

```
============================================================
🚀 Supabase Database Demo
============================================================

📝 Step 1: Inserting a new message...
✅ Message inserted successfully!
   ID: 1
   Text: Hello from Python! This is my first cloud database message.
   Created: 2025-12-27T19:00:00.000000

📝 Step 2: Inserting another message...
✅ Message inserted successfully!
   ID: 2
   Text: Supabase + Python = ❤️
   Created: 2025-12-27T19:00:01.000000

📖 Step 3: Reading all messages from cloud database...

📬 Found 2 message(s):

------------------------------------------------------------
  ID: 2
  Text: Supabase + Python = ❤️
  Created: 2025-12-27T19:00:01.000000
------------------------------------------------------------
  ID: 1
  Text: Hello from Python! This is my first cloud database message.
  Created: 2025-12-27T19:00:00.000000
------------------------------------------------------------

============================================================
✅ Demo completed! Check your Supabase dashboard to see the data.
============================================================
```

## Verify in Supabase Dashboard

1. Go to your Supabase project
2. Click **"Table Editor"** in the sidebar
3. Select the **"messages"** table
4. You should see your inserted messages! 📊

## Code Snippet Summary

### Insert a Message
```python
from supabase import create_client

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Insert
data = {"text": "Hello World!", "created_at": datetime.now().isoformat()}
result = supabase.table("messages").insert(data).execute()
```

### Read All Messages
```python
# Read
result = supabase.table("messages").select("*").execute()
for msg in result.data:
    print(msg['text'])
```

## Project Structure

```
supabase-database-demo/
├── database_demo.py    # Main Python script
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technologies Used

- **Supabase** - Cloud PostgreSQL database
- **Python** - Programming language
- **supabase-py** - Python client library

## License

MIT License - Feel free to use for learning!
