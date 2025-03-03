""" Export comment & submissions Supabase tables to JSON files. """

from redditharbor.utils import download

from modules.config import DB_CONFIG, SUPABASE_CLIENT

download.comment(supabase_client=SUPABASE_CLIENT, db_name=DB_CONFIG["comment"]).to_json(
    columns="all", file_name="comments"
)
download.submission(
    supabase_client=SUPABASE_CLIENT, db_name=DB_CONFIG["submission"]
).to_json(columns="all", file_name="submissions")
