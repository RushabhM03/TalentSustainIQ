from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
import flask_monitoringdashboard as dashboard
import pandas as pd
import os
from flask_cors import CORS, cross_origin
from apps.training.train_model import TrainModel
from apps.prediction.predict_model import PredictModel
from apps.core.config import Config
from utils import *


app = Flask(__name__)
dashboard.bind(app)
CORS(app)

UPLOAD_FOLDER = './data/training_data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def homeRouteClient():
    return render_template('index.html')


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/api', methods=['GET'])
def api_page():
    return render_template('api.html')

@app.route("/news", methods=['GET'])
def news():
    data, len = getnews()
    return render_template("news.html", data=data, len=len)

@app.route("/models", methods=['GET'])
def models():
    return render_template('models.html')

@app.route('/guide', methods=['GET'])
def guidePage():
    return render_template('guide.html')

@app.route('/predict_client', methods=['GET', 'POST'])
def predictRouteClient():
    return render_template('predict.html')

@app.route('/train_client', methods=['GET', 'POST'])
def trainclient():
    return render_template('train.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if not any(request.files):
        return render_template('train.html', alertmsg="No part file")
    
    file = list(request.files.values())[0]
    
    if file.filename == '':
        return render_template('train.html', alert_msg="No file selected")
    
    if file:
        relative_path = 'data/training_data/' + file.filename  
        file.save(relative_path)
        return render_template('train.html', alertmsg="File uploaded successfully.")
    
@app.route('/training', methods=['POST'])
@cross_origin()
def training_route_client():
    try:
        config = Config()
        #get run id
        run_id = config.get_run_id()
        data_path = config.training_data_path
        #trainmodel object initialization
        trainModel=TrainModel(run_id,data_path)
        #training the model
        trainModel.training_model()
        return Response("Training successfull! and its RunID is : "+str(run_id))
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)



@app.route('/batchprediction', methods=['POST'])
@cross_origin()
def batch_prediction_route_client():
    try:
        config = Config()
        #get run id
        run_id = config.get_run_id()
        data_path = config.prediction_data_path
        #prediction object initialization
        predictModel=PredictModel(run_id, data_path)
        #prediction the model
        predictModel.batch_predict_from_model()
        return Response("Prediction successfull! and its RunID is : "+str(run_id))
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)


@app.route('/prediction', methods=['POST'])
@cross_origin()
def single_prediction_route_client():
    try:
        config = Config()
        #get run id
        run_id = config.get_run_id()
        data_path = config.prediction_data_path
        print('Test')

        if request.method == 'POST':
            satisfaction_level = request.form['satisfaction_level']
            last_evaluation = request.form["last_evaluation"]
            number_project = request.form["number_project"]
            average_montly_hours = request.form["average_montly_hours"]
            time_spend_company = request.form["time_spend_company"]
            work_accident = request.form["work_accident"]
            promotion_last_5years = request.form["promotion_last_5years"]
            salary = request.form["salary"]

            data = pd.DataFrame(data=[[0 ,satisfaction_level, last_evaluation, number_project,average_montly_hours,time_spend_company,work_accident,promotion_last_5years,salary]],
                              columns=['empid','satisfaction_level', 'last_evaluation', 'number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','salary'])
            # using dictionary to convert specific columns
            convert_dict = {'empid': int,
                            'satisfaction_level': float,
                            'last_evaluation': float,
                            'number_project': int,
                            'average_montly_hours': int,
                            'time_spend_company': int,
                            'Work_accident': int,
                            'promotion_last_5years': int,
                            'salary': object}

            data = data.astype(convert_dict)

            # object initialization
            predictModel = PredictModel(run_id, data_path)
            # prediction the model
            output = predictModel.single_predict_from_model(data)
            print('output : '+str(output))
            return Response("Predicted Output is : "+str(output))
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404

if __name__=="__main__":
    #app.run()
    '''
    host = '0.0.0.0'
    port = 5000
    print("Server running on http://0.0.0.0:5000/")
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
    '''
    app.run(host='0.0.0.0', port=5000, debug=True)
    