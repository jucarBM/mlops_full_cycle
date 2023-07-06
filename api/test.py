from flask import Flask, request
from app.utils import get_data, save_data
from app.views import make_model_prediction
from app.utils import conection_daris, conection_cl
from app.utils import verify_cloud_run

app = Flask(__name__)


@app.route("/", methods=['POST'])
def main():
    # config enviroment
    conection_daris = conection_daris()
    verify_cloud_run(conection_daris)

    if test == 1:
        # get data
        conection_cl = conection_cl()
        data = get_data(param1, conection_daris)
        # make prediction
        result = make_model_prediction(data, conection_cl)
        # save data
        save_data(result)
    else:
        return "no"
