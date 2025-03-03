""" Collect submissions (posts) from Reddit. """

from modules.config import COLLECTION_CLIENT

SUBREDDITS = ["all"]
QUERY = ["impact of AI and automation in the job market"]
LIMIT = 200

COLLECTION_CLIENT.submission_by_keyword(subreddits=SUBREDDITS, query=QUERY, limit=LIMIT)
