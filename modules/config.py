import os

from dotenv import load_dotenv

from redditharbor import login
from redditharbor.dock.pipeline import collect

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
REDDIT_PUBLIC = os.environ["REDDIT_PUBLIC"]
REDDIT_SECRET = os.environ["REDDIT_SECRET"]
REDDIT_USER_AGENT = os.environ["REDDIT_USER_AGENT"]

DB_CONFIG = {
    "user": "test_redditor",
    "submission": "test_submission",
    "comment": "test_comment",
}

REDDIT_CLIENT = login.reddit(
    public_key=REDDIT_PUBLIC, secret_key=REDDIT_SECRET, user_agent=REDDIT_USER_AGENT
)

SUPABASE_CLIENT = login.supabase(url=SUPABASE_URL, private_key=SUPABASE_KEY)

COLLECTION_CLIENT = collect(
    reddit_client=REDDIT_CLIENT, supabase_client=SUPABASE_CLIENT, db_config=DB_CONFIG
)
