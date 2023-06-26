from dvc import api
import pandas as pd
from io import StringIO
import sys
import logging

# basic logging config
logging.basicConfig(
    format='astime:%(asctime)s - level:%(levelname)s - message:%(message)s',
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr
)

# logger

logger = logging.getLogger(__name__)

logger.info("Fetching data from remote storage")

# recovering data from remote dvc
movie_data_path = api.read(
    'dataset/movies.csv', remote='dataset-track', encoding='utf-8')
finantials_data_path = api.read(
    'dataset/finantials.csv', remote='dataset-track', encoding='utf-8')
opening_gross_path = api.read(
    'dataset/opening_gross.csv', remote='dataset-track', encoding='utf-8')

fin_data = pd.read_csv(StringIO(finantials_data_path))
print(fin_data.columns)
movie_data = pd.read_csv(StringIO(movie_data_path))
print(movie_data.columns)
opening_gross = pd.read_csv(StringIO(opening_gross_path))
print(opening_gross.columns)

# preparing data
numeric_columns_mask = (movie_data.dtypes == float) | (
    movie_data.dtypes == int)
numeric_columns = [
    column for column in numeric_columns_mask.index if numeric_columns_mask[column]]
movie_data = movie_data[numeric_columns+['movie_title']]

fin_data = fin_data[['movie_title', 'production_budget', 'worldwide_gross']]

fin_movie_data = pd.merge(fin_data, movie_data, on='movie_title', how='left')

full_movie_data = pd.merge(
    fin_movie_data, opening_gross, on='movie_title', how='left')

full_movie_data = full_movie_data.drop(['gross', 'movie_title'], axis=1)
print(full_movie_data.columns)

# saving data
logger.info("Saving data to local storage")

full_movie_data.to_csv('dataset/full_data.csv', index=False)

logger.info("Data fetch and prepared successfully")
