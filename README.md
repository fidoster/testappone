# Paper Roughness Prediction Challenge

This GitHub repository contains code and resources for a project developed in Azure Machine Learning Studio aimed at identifying which measurements affect the paper's roughness (Sensor Name: Roughness) and creating a prediction model for roughness. Roughness is a quality measurement made in a laboratory every time a roll of paper is finished. However, the factory would like to know what the value could be based on the sensor data.

![PMSensor Model](https://github.com/fidoster/sensorapp/assets/99990278/1763beff-b1fd-4099-9fda-531e319876bd)

## Repository Structure

- `.github/workflows`: Contains the Azure App Service build and deployment workflow configuration for automating the deployment of the prediction model.

- `static`: This directory contain static assets or files related to the web app's user interface.

- `templates`: Any HTML or template files used in the development of the Azure web app.

- `app.py`: The Python script for the web application that interacts with the deployed prediction model.

- `requirements.txt`: This file lists the required Python libraries and dependencies for running the web application and the model.

## Model Evaluation Metrics

The paper roughness prediction model has been evaluated using various metrics to assess its performance. Here are the evaluation metrics and their respective values:

### Mean Absolute Error (MAE)
- MAE measures the average absolute difference between the predicted and actual values. Lower values indicate better accuracy.

### Root Mean Squared Log Error (RMSLE)
- RMSLE measures the logarithmic difference between predicted and actual values. It's useful when the target variable has a wide range of values.

### Explained Variance
- Explained Variance quantifies the proportion of variance in the target variable that is explained by the model. Higher values indicate a better fit.

### Mean Absolute Percentage Error (MAPE)
- MAPE calculates the percentage difference between predicted and actual values. It's useful for understanding the relative error.

### Root Mean Squared Error (RMSE)
- RMSE measures the average squared difference between predicted and actual values. It penalizes larger errors more heavily.

### Median Absolute Error
- Median Absolute Error is similar to MAE but based on the median absolute difference.

### R-squared (R2) Score
- R2 measures the proportion of the variance in the dependent variable that is predictable from the independent variables. A higher R2 indicates a better fit.

### Normalized Metrics
- Some of the metrics may be normalized to provide a standardized view of performance.

### Spearman Correlation
- Spearman Correlation measures the strength and direction of the monotonic relationship between predicted and actual values. It's useful when the relationship is not necessarily linear.

These metrics provide insights into the model's performance in predicting paper roughness based on sensor data. It's important to analyze these metrics in the context of your specific application to determine if the model meets the desired level of accuracy and reliability.

## Getting Started

To get started with this Azure ML Studio project, follow these steps:

1. Refer to the documentation within the `.github/workflows` directory for information on the Azure App Service build and deployment workflow configuration.

2. Explore the `static` and `templates` directories for any static assets or user interface components used in the web app.

3. Review the `app.py` script for details on how the web application interacts with the deployed model.

4. Ensure you have the required Python libraries listed in `requirements.txt` installed to run the web application and the model.

## Contributors

- Farhan Ahmed

## License

This project is licensed under the MIT License -- see the [LICENSE.md](LICENSE.md) file for details.

We welcome any suggestions, improvements, or bug fixes to enhance the paper roughness prediction model and Azure web app developed in Azure ML Studio.