import  pandas as pd
import pickle



if __name__=='__main__':

    df=pd.read_csv('data.csv')
    x=df['text']
    y=df['label']

    # Handle Input text data

    from sklearn.feature_extraction.text import TfidfVectorizer

    cv = TfidfVectorizer(min_df=1, stop_words='english')
    X = cv.fit_transform(x).toarray()
    print(X[1])

    with open("vocab.pkl", 'wb') as handle:
        pickle.dump(cv, handle)


    from sklearn.model_selection import GridSearchCV

    # Train our model
    # using grid search method for select a proper hiperperamiter
    param_grid = {
        'C': [1,52,5,65],

    }
    from sklearn.svm import LinearSVC

    lin = LinearSVC(loss='hinge')
    grid_search = GridSearchCV(estimator=lin, param_grid=param_grid,
                               cv=2, n_jobs=-1, verbose=2)
    grid_search.fit(X, y)
    print('Final Loss', grid_search.best_params_, "Final accuracy :", grid_search.best_score_ * 100, "%")

    from sklearn.metrics import accuracy_score

    best_grid = grid_search.best_estimator_


    # save model
    from sklearn.externals import joblib
    # joblib.dump(best_grid, 'model.pkl')

