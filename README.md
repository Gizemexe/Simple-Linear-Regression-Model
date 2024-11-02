## House Price Prediction with Linear Regression

<h2>Introduction</h2>
<p>This project aims to build a linear regression model for forecasting house prices. The model measures prediction performance by standardizing features over a dataset and using the root mean square error (RMSE) metric.</p>

<h2> Data Preprocessing </h2>
<p>In the dataset, floor area was used as a feature for price prediction. Before training the model, a bias term was added to each sample and the data was standardized with the mean and standard deviation values calculated on the training set.</p>

<h2> Model Training</h2>
<p>The model was trained for 500 epochs with a learning rate of 0.1. At each epoch, the cost function was calculated and optimized.</p>

**Cost Function Graph**
<p>The graph below shows how the cost function decreases with the number of epochs. This is an indication of the learning process of the model and the reduction in the cost function shows that the model is making progress towards better results.</p>

![image](https://github.com/user-attachments/assets/94983bdc-78d7-49fb-8dde-cd462bbf2de9)

<h2> Model Performance</h2>
<p>The RMSE metric is used to evaluate the performance of the model. The RMSE value in training and test sets are as follows:</p>

![Adsız](https://github.com/user-attachments/assets/f0a8a230-f3bc-4fd5-a4ea-8c72ed547f64)

A low RMSE value indicates that the model predicts close to the actual values. And If the training and test RMSE values are close to each other, your model performs well overall.

**RMSE (Root Mean Squared Error)** 
 is an error metric that measures the difference between predicted values and actual values.
RMSE is commonly used to evaluate the predictive performance of a model because:
- It is more sensitive to large errors: Since it sums errors squared, large errors are penalized more.
- It prevents positive and negative errors from canceling each other out: Since errors are squared, positive and negative deviations do not cancel each other out.

![image](https://github.com/user-attachments/assets/2b034301-19e8-4b04-8b86-68b8f54735b0)

<p>𝑦𝑖:  Actual values</p>
<p>^𝑦𝑖: Values predicted by the model</p>
<p>𝑛: Number of samples</p>

**Actual vs. Predicted Prices Graph**
<p>The graph below compares the prices predicted by the model (linear solution) and the actual prices (training and test data).</p>

![image](https://github.com/user-attachments/assets/468bb871-a3c1-4948-954a-98221e426212)

**Standardization Formula**
These rows standardize the Xtrain and Xtest data using the formula

![image](https://github.com/user-attachments/assets/853f5f94-0ecc-42ee-9b4e-3edd7269a5e9)

<p>mean: The mean value of the features of the training data (train set).</p>
<p>std: The standard deviation of the features of the training data.</p>

**Standardization**, in particular:

- Faster and more stable operation of optimization algorithms such as Gradient Descent,
- More consistent learning of model parameters,
- It helps prevent features of different scales (e.g. one with a price in the hundreds of thousands, another with a small square meter) from negatively affecting model performance.
<p>If you don't apply standardization, large-scale features can take on more weight and the model can ignore the impact of small-scale features.</p>

<h2> Conclusion</h2>
<p>The linear regression model developed in this study was able to predict house prices with reasonable accuracy based on floor area data. The RMSE values of the trained model are reasonable, and the addition of different features or the use of more complex models to improve the prediction accuracy can be evaluated in future studies.</p>

