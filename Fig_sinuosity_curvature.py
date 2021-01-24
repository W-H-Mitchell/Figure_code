import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Get the data
ChSev = pd.read_csv('Niger_ChSev.csv')
ChOne = pd.read_csv('Niger_ChOne.csv')
compiled = pd.concat([ChOne, ChSev], ignore_index='True') # concatenate data from channels


# Check for missing values
missing_values = compiled.isnull().sum() 
total_cells = np.product(compiled.shape) 
percent_missing = (missing_values/total_cells) * 100 
print(percent_missing) # percent of data that is missing
compiled = compiled.dropna() # drop missing values


# Sinuosity and curvature plot against downstream distance.
def downstream_sin_curv(data):
    dist = data.downstream_distance_km # downstream distance (x axis)
    sin = data.sinuosity # sinuosity and curvature (y axis)
    data['curvature'] = data.max_curv.map(lambda c:(c**2)**(1/2)) # map a new column with positive curvature
    curv = data.curvature

    # creating a figure with two y axis for sinuosity and curvature
    fig1 = plt.figure(figsize=(10.0, 5.0))
    fig1, ax1 = plt.subplots()

    # sinuosity plot
    ax1.set_xlabel('Downstream Distance (km)')
    ax1.set_ylabel('Sinuosity', color='k')
    ax1.plot(dist, sin, linestyle='solid', color='k', marker='o', markersize=4, linewidth=1)
    ax1.tick_params(axis='y', labelcolor='k')

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    # curvature plot
    ax2.set_ylabel('Curvature', color= 'tab:blue')  # we already handled the x-label with ax1
    ax2.plot(dist, curv, linestyle='solid', color='tab:blue', marker='d', markersize=4, linewidth=1)
    ax2.tick_params(axis='y', labelcolor= 'tab:blue')

    fig1.tight_layout()  # otherwise the right y-label is slightly clipped
    fig1.savefig("Downstream_SinCurvature.pdf", format='pdf')
    plt.show()


# Sinuosity and curvature scatter plot 
def scatter_SinCurv(df):
    # Scatter plot of sinuosity curvature
    df['curvature'] = df['max_curv'].map(lambda c:(c**2)**(1/2)) # map a new column with positive curvature
    df = df.dropna() # drop any NaNs
    
    # Remove outlier curvatures
    anomalous_curv = df.loc[df.curvature >= 0.02] 
    df = df.drop(df[df.curvature >= 0.02].index)
    # df.to_csv(r'/Users/whamitchell/Documents/python/channel_sinuosities/ChC_sin_curv.csv', index = False)
    y_sin = np.array(df['sinuosity']).reshape(-1, 1)
    X_curv = np.array(df['curvature']).reshape(-1, 1)

    # split df into unstructured and structured data
    structured_data = df.loc[df.structured != False]
    unstructured_data = df.loc[df.structured == False]
    structured_sinuosity = np.array(structured_data['sinuosity'])
    structured_curvature = np.array(structured_data['curvature'])
    y_sinuosity = np.array(unstructured_data['sinuosity']).reshape(-1, 1)
    X_curvature = np.array(unstructured_data['curvature']).reshape(-1, 1)
    y_sinuosity.shape
    X_curvature.shape
    
    
    # Plots
    fig2 = plt.figure(figsize=(20.0, 8.0))
    axes1 = fig2.add_subplot(1, 2, 1)
    axes2 = fig2.add_subplot(1, 2, 2)

    axes1.set_xlabel("Curvature")
    axes1.set_ylabel("Sinuosity")
    axes1.plot(X_curv, y_sin, c = 'k', marker = '.', Label='All data', linewidth=0)
    # calculate the trendline 
    lin_reg = LinearRegression()
    lin_reg.fit(X_curv, y_sin)
    predictions = lin_reg.predict(X_curv)
    # Coefficients
    coef = "Coefficients: " + str(lin_reg.coef_)
    mse = "Mean squared error: " + str(mean_squared_error(y_sin, predictions)) # The mean squared error
    r2 = "Coefficient of determination: "+ str(r2_score(y_sin, predictions)) # The coefficient of determination: 1 is perfect prediction
    axes1.plot(X_curv, predictions, Label='Linear Regression Model', c='k')
    axes1.annotate(coef, (0,0))
    axes1.annotate(mse, (2,0))
    axes1.annotate(r2, (4,0))


    
    axes2.set_xlabel("Curvature")
    axes2.set_ylabel("Sinuosity")
    axes2.plot(structured_curvature, structured_sinuosity, Label='Structured Slope Values', c = 'tab:red', marker = 'x', markersize=1, linewidth=0)
    axes2.plot(X_curvature, y_sinuosity, Label='Unstructured Slope Values', c = 'tab:blue', marker = '.', markersize=6, linewidth=0)
    # calculate the trendline 
    l_reg = LinearRegression()
    l_reg.fit(X_curvature, y_sinuosity)
    pred = l_reg.predict(X_curvature)
    axes2.plot(X_curvature, pred, Label='Linear Regression Model', c='k')
    axes2.legend()  
    # Coefficients
    coefs = "Coefficients: " + str(l_reg.coef_)
    mserr = "Mean squared error: " + str(mean_squared_error(y_sin, pred)) # The mean squared error
    r2_1 = "Coefficient of determination: "+ str(r2_score(y_sin, pred)) # The coefficient of determination: 1 is perfect prediction
    axes2.plot(X_curvature, predictions, Label='Linear Regression Model', c='k')
    axes2.annotate(coefs, (0,10))
    axes2.annotate(mserr, (2,10))
    axes2.annotate(r2_1, (4,10))
    plt.show()



# Call figure functions
downstream_sin_curv(ChSev)
downstream_sin_curv(ChOne)
scatter_SinCurv(compiled)

#m, b = np.polyfit(unstructured_curvature, unstructured_sinuosity, 1)
#axes2.plot(unstructured_curvature, m*unstructured_curvature + b, c='r', linewidth=0.5)  