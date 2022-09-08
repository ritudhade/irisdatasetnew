import json
import pickle
import numpy as np
import config
import sys
sys.path.append(r"D:\Mock_group_practise\Dataset_Solved\Classification\Iris_Prediction")


class Iris_Data():
    def __init__(self, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def load_model(self):
        with open(config.JSON_FILE_PATH,'r')as f:
            self.json_data = json.load(f)

        with open(config.MODEL_FILE_PATH,'rb')as f:
            self.logistic_model = pickle.load(f)

    def get_irisclass(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.SepalLengthCm
        test_array[1] = self.SepalWidthCm
        test_array[2] = self.PetalLengthCm
        test_array[3] = self.PetalWidthCm

        pred = self.logistic_model.predict([test_array])[0]
        return pred


