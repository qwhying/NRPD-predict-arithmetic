# mvpa_utils.py

import numpy as np
import scipy.stats as sci
from sklearn.svm import SVR
from sklearn.model_selection import StratifiedKFold

kernel = 'linear'
max_iter = int(1e5)

def train_and_evaluate_model(input, target_label):
    cv = StratifiedKFold(n_splits=5, shuffle=True)
    SVR_decoder = SVR(kernel=kernel, max_iter=max_iter)
    prediction = np.zeros(target_label.shape)
    r = np.array([])

    for train, test in cv.split(input, target_label):
        SVR_decoder.fit(input[train], target_label[train])
        prediction[test] = SVR_decoder.predict(input[test])
        ri, _ = sci.pearsonr(prediction[test], target_label[test])
        if np.isnan(ri):
            ri = 0
        r = np.append(r, ri)

    r_all, _ = sci.pearsonr(prediction, target_label)
    return r.mean(), r_all, prediction

def train_model(input, target_label):
    SVR_decoder = SVR(kernel=kernel, max_iter=max_iter)
    SVR_decoder.fit(input,target_label)
    return SVR_decoder

def evaluate_model(Decoder,input, target_label):

    prediction = np.zeros(target_label.shape)

    prediction = Decoder.predict(input)
    r, _ = sci.pearsonr(prediction, target_label)
    if np.isnan(r):
        r = 0

    return r
