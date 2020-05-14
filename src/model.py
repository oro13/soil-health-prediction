import pandas as pd


from pathlib import Path
from brukeropusreader import read_file
from tqdm.notebook import tqdm

def load_spectra_df(SPECTRA_DIR, AFSIS_PATH):
    names = []
    spectra = []

    for path in tqdm(AFSIS_PATH.glob(SPECTRA_DIR)):
        if path.is_file():
            spect_data = read_file(path)
            spectra.append(spect_data["AB"])
            names.append(path.stem)
    wave_nums = spect_data.get_range()


    column_names = ['{:.3f}'.format(x) for x in wave_nums]
    spectra_df = pd.DataFrame(spectra, index=names, columns=column_names)
    return spectra_df

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold

import numpy as np
from xgboost import XGBRegressor

def basic_xgboost(spectra_df, WET_CHEM_PATH, Y_COLUMN):
    
    wet_chem_df = pd.read_csv(WET_CHEM_PATH, index_col='SSN')
    data_df = spectra_df.merge(wet_chem_df, left_index=True, right_index=True)

    print(f'Training model for {Y_COLUMN}.')
    print(f'{data_df.shape[0]} samples available.')


    y = data_df[Y_COLUMN]
    y_mask = y.notnull()
    y = y[y_mask]
    y = np.log1p(y)

    column_names = spectra_df.columns
    
    x = data_df[column_names]
    x = x[y_mask]
    x = np.apply_along_axis(np.gradient, 1, x)

    kfold = KFold(shuffle=True, random_state=0, n_splits=4)
    model = XGBRegressor(n_estimators=500, min_child_weight=20, n_jobs=-1, objective='reg:squarederror')

    cv_result = cross_validate(model, x, y, scoring='r2', cv=kfold)['test_score']
    print(f'CV r^2 score: {np.mean(cv_result)}')
    
    return model

def basic_xgboost2(X, y):
    
    '''
    X the spectra data frame
    y, the specified target column
    '''
    
#     wet_chem_df = pd.read_csv(WET_CHEM_PATH, index_col='SSN')
#     data_df = spectra_df.merge(wet_chem_df, left_index=True, right_index=True)

    print(f'Training model for {y.name}.')
    print(f'{y.shape[0]} samples available.')


    #y = data_df[Y_COLUMN]
    y_mask = y.notnull()
    y = y[y_mask]
    y = np.log1p(y)

    #column_names = X.columns
    
    #x = data_df[column_names]
    X = X[y_mask]
    X = np.apply_along_axis(np.gradient, 1, X)

    kfold = KFold(shuffle=True, random_state=0, n_splits=4)
    model = XGBRegressor(n_estimators=500, min_child_weight=20, n_jobs=-1, objective='reg:squarederror')

    cv_result = cross_validate(model, X, y, scoring='r2', cv=kfold)['test_score']
    print(f'CV r^2 score: {np.mean(cv_result)}')
    
    return model

def basic_xgboost3(X, y):
    
    '''
    X the spectra data frame
    y, the specified target column
    '''
    
#     wet_chem_df = pd.read_csv(WET_CHEM_PATH, index_col='SSN')
#     data_df = spectra_df.merge(wet_chem_df, left_index=True, right_index=True)

    print(f'Training model for {y.name}.')
    print(f'{y.shape[0]} samples available.')

    print('model initializing')
    kfold = KFold(shuffle=True, random_state=0, n_splits=4)
    model = XGBRegressor(n_estimators=500, min_child_weight=20, n_jobs=-1, objective='reg:squarederror')

    print('done')
    
    print('begin cross validation')
    cv_result = cross_validate(model, X, y, scoring='r2', cv=kfold)['test_score']
    print(f'CV r^2 score: {np.mean(cv_result)}')
    
    return model, np.mean(cv_result)