""" Export submissions Supabase tables to JSON files. """

from redditharbor.utils import download

from modules.config import DB_CONFIG, SUPABASE_CLIENT

download.submission(
    supabase_client=SUPABASE_CLIENT, db_name=DB_CONFIG["submission"]
).to_json(columns="all", file_name="submissions")
