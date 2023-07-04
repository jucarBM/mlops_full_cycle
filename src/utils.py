from sklearn.pipeline import Pipeline
from joblib import dump
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def update_model(model: Pipeline) -> None:
    dump(model, 'model/model.pkl')


def save_simple_model_report(train_score: float, test_score: float, validation_score: float, model: Pipeline) -> None:

    with open("report.txt", "w") as report_file:
        report_file.write("# Model pipeline description\n")

        for key, value in model.named_steps.items():
            report_file.write(f"### {key}: {value.__repr__()}\n")

        report_file.write(f"### Train score: {train_score}\n")
        report_file.write(f"### Test score: {test_score}\n")
        report_file.write(f"### Validation score: {validation_score}\n")

        report_file.write("![](./prediction_behavior.png)")


def get_model_performance_test_set(y_test: pd.DataFrame, y_test_pred: pd.DataFrame) -> None:

    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(10)

    sns.regplot(x=y_test, y=y_test_pred, ax=ax)
    ax.set_xlabel('Predicted worldwide gross')
    ax.set_ylabel('Actual worldwide gross')
    ax.set_title('Model performance on test set')
    fig.savefig('prediction_behavior.png')
