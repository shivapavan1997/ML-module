from src.logger import logging
from src.exception import CustomException
import os, sys
import pickle
from sklearn.metrics import r2_score

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj,file_obj )
    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
    
            test_model_score = r2_score(y_test, y_pred)
            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e,sys)