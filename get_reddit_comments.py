""" Collect submissions (posts) from Reddit. """

from redditharbor.utils import fetch

from modules.config import COLLECTION_CLIENT, DB_CONFIG, SUPABASE_CLIENT


existing_submissions = fetch.submission(
    supabase_client=SUPABASE_CLIENT, db_name=DB_CONFIG["submission"]
)
COLLECTION_CLIENT.comment_from_submission(
    submission_ids=existing_submissions.id(), level=2
)
