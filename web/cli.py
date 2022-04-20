import argparse

import sys

from app.presentation import article_by_id_to_stdout

# Create the parser
article_parser = argparse.ArgumentParser(description='Fetch article')

# Add the arguments
article_parser.add_argument('article_id',
                    metavar='id',
                    type=str,
                    help='article id ')

# Execute the parse_args() method
args = article_parser.parse_args()

article_id = args.article_id

article_by_id_to_stdout(article_id)