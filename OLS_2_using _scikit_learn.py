from sklearn.linear_model import LinearRegression

LR=LinearRegression()

# define your X and Y as NumPy Arrays (column vectors)
X = np.array([1,3,5]).reshape(-1,1)
Y = np.array([4.8,12.4,15.5]).reshape(-1,1)

LR.fit(X,Y) # calculate the model coefficients
LR.intercept_ # the bias or the intercept term (w0*)

#OUTPUT -->  array([2.875])    COMPARE IT WITH THE FILE ols.py

LR.coef_ # the slope term (w1*)

# OUTPUT --> array([[2.675]]) COMPARE IT WITH THE FILE ols.py
