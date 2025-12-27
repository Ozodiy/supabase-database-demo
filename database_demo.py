"""
Supabase Database Demo
Demonstrates cloud-managed PostgreSQL database operations:
- Insert new messages
- Read all messages
"""

from supabase import create_client, Client
from datetime import datetime
import os

# ============================================
# CONFIGURATION - Replace with your Supabase credentials
# ============================================
# Get these from: Supabase Dashboard > Settings > API
SUPABASE_URL = "YOUR_SUPABASE_URL"  # e.g., "https://xxxxx.supabase.co"
SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"  # Your anon/public key

# Alternative: Use environment variables (more secure)
# SUPABASE_URL = os.environ.get("SUPABASE_URL")
# SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def insert_message(text: str) -> dict:
    """
    Insert a new message into the messages table.
    
    Args:
        text: The message text to insert
        
    Returns:
        The inserted message data
    """
    data = {
        "text": text,
        "created_at": datetime.now().isoformat()
    }
    
    result = supabase.table("messages").insert(data).execute()
    
    if result.data:
        print(f"✅ Message inserted successfully!")
        print(f"   ID: {result.data[0]['id']}")
        print(f"   Text: {result.data[0]['text']}")
        print(f"   Created: {result.data[0]['created_at']}")
        return result.data[0]
    else:
        print("❌ Failed to insert message")
        return None


def read_all_messages() -> list:
    """
    Read all messages from the messages table.
    
    Returns:
        List of all messages
    """
    result = supabase.table("messages").select("*").order("created_at", desc=True).execute()
    
    if result.data:
        print(f"\n📬 Found {len(result.data)} message(s):\n")
        print("-" * 60)
        for msg in result.data:
            print(f"  ID: {msg['id']}")
            print(f"  Text: {msg['text']}")
            print(f"  Created: {msg['created_at']}")
            print("-" * 60)
        return result.data
    else:
        print("📭 No messages found in database")
        return []


def delete_message(message_id: int) -> bool:
    """
    Delete a message by ID.
    
    Args:
        message_id: The ID of the message to delete
        
    Returns:
        True if deleted successfully
    """
    result = supabase.table("messages").delete().eq("id", message_id).execute()
    
    if result.data:
        print(f"🗑️ Message {message_id} deleted successfully")
        return True
    return False


# ============================================
# MAIN DEMO
# ============================================
if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Supabase Database Demo")
    print("=" * 60)
    
    # Step 1: Insert a new message
    print("\n📝 Step 1: Inserting a new message...")
    insert_message("Hello from Python! This is my first cloud database message.")
    
    # Step 2: Insert another message
    print("\n📝 Step 2: Inserting another message...")
    insert_message("Supabase + Python = ❤️")
    
    # Step 3: Read all messages
    print("\n📖 Step 3: Reading all messages from cloud database...")
    messages = read_all_messages()
    
    print("\n" + "=" * 60)
    print("✅ Demo completed! Check your Supabase dashboard to see the data.")
    print("=" * 60)
