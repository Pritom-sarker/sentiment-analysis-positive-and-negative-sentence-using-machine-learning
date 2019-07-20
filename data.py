import re
import pickle



# data preprocessing 

f=open('data/negative.txt','r')
neg=[]
val=[]

for i in f:
    st=i.lower()
    st=re.sub(r"[-./,']+", " ", st)
    neg.append(st)
    val.append(0)


f=open('data/positive.txt','r')
pos=[]
p_val=[]

for i in f:
    st = i.lower()
    st = re.sub(r"[-./,']+", " ", st)
    pos.append(st)
    p_val.append(1)

y=val+p_val
x=neg+pos

print(x[0])

#
# if __name__=='__main__':
#
#     # Handle Input text data
#     from sklearn.feature_extraction.text import TfidfVectorizer
#
#     cv = TfidfVectorizer(min_df=1, stop_words='english')
#     X = cv.fit_transform(x).toarray()
#
#     with open("vocab.pkl", 'wb') as handle:
#         pickle.dump(cv, handle)
#
#
#     from sklearn.model_selection import GridSearchCV
#
#     # Train our model
#     # using grid search method for select a proper hiperperamiter
#     param_grid = {
#         'C': [1],
#
#     }
#     from sklearn.svm import LinearSVC
#
#     lin = LinearSVC(loss='hinge')
#     grid_search = GridSearchCV(estimator=lin, param_grid=param_grid,
#                                cv=2, n_jobs=-1, verbose=2)
#     grid_search.fit(X, y)
#     print('Final Loss', grid_search.best_params_, "Final accuracy :", grid_search.best_score_ * 100, "%")
#
#     from sklearn.metrics import accuracy_score
#
#     best_grid = grid_search.best_estimator_
#
#
#     # save model
#     from sklearn.externals import joblib
#     # joblib.dump(best_grid, 'model.pkl')
#
#
