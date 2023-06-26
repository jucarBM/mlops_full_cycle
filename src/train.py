from utils import update_model, save_simple_model_report, get_model_performance_test_set
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingRegressor

import logging
import sys
import numpy as np
import pandas as pd

# basic logging config
logging.basicConfig(
    format='astime:%(asctime)s - level:%(levelname)s - message:%(message)s',
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr
    )

logger = logging.getLogger(__name__)

logger.info("Loading Data ...")
data = pd.read_csv('dataset/full_data.csv')

logger.info("Splitting Data ...")
model = Pipeline([
    ('imputer', SimpleImputer(strategy='median', missing_values=np.nan)),
    ('core_model', GradientBoostingRegressor())
])

logger.info("Separating dataset intro train and test")

X = data.drop('worldwide_gross', axis=1)
y = data['worldwide_gross']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

logger.info("Setting Hyperparameter to tune")

param_tuning = {'core_model__n_estimators': range(20, 350, 10)}

grid_search = GridSearchCV(model, param_grid= param_tuning, cv=5, scoring='r2')

logger.info("Starting grid search ...")
grid_search.fit(X_train, y_train)
logger.info("Grid search finished")

logger.info("Cross validating best model ...")
final_results = cross_validate(grid_search.best_estimator_, X_train, y_train, cv=5, return_train_score=True)

train_score = final_results['train_score'].mean()
test_score = final_results['test_score'].mean()

assert train_score > 0.7
assert test_score > 0.65

logger.info(f"Train Score: {train_score}")
logger.info(f"Test Score: {test_score}")

logger.info("Updating model ...")
update_model(grid_search.best_estimator_)

logger.info("Generating model report ...")
validation_score = grid_search.best_estimator_.score(X_test, y_test)
save_simple_model_report(train_score, test_score, validation_score, grid_search.best_estimator_)

y_test_pred = grid_search.best_estimator_.predict(X_test)

get_model_performance_test_set(y_test, y_test_pred)