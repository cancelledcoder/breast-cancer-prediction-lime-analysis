# Breast Cancer Prediction Using Decision Tree and LIME

## Introduction
Breast cancer is a significant health issue, with early detection being crucial for effective treatment and improved survival rates. Machine learning models can provide valuable assistance in predicting the likelihood of breast cancer, aiding healthcare professionals in diagnosis and treatment planning. This project focuses on developing a breast cancer prediction model using a Decision Tree classifier and employing LIME to interpret the model's predictions.

## Objectives
- **Model Development:** Create a robust breast cancer prediction model using a Decision Tree classifier.
- **Performance Evaluation:** Assess the model's performance using accuracy and classification metrics.
- **Model Interpretation:** Utilize LIME to provide insights into the model's decision-making process, enhancing transparency and understanding.

## Dataset
The dataset used for this project, `nimbu.csv`, includes various features related to breast cancer. It was cleaned by removing any missing values to ensure data integrity. The features for prediction were selected from the dataset, excluding the initial columns assumed to be patient ID and diagnosis. The target variable represents the diagnosis, with categories such as malignant (M) and benign (B).

## Methodology
1. **Data Preparation:**
   - The dataset was loaded and cleaned to remove any missing values.
   - The data was split into features (X) and the target variable (y).
   - Further, the dataset was divided into training and testing sets using an 80-20 split to ensure reliable evaluation.
   
2. **Model Development:**
   - A Decision Tree classifier was trained using the training data.
   - This model was chosen for its simplicity and interpretability, making it suitable for understanding decision boundaries.
   
3. **Model Evaluation:**
   - The model's performance was evaluated on the test data, providing metrics such as accuracy and a detailed classification report.
   - Accuracy provided an overall measure of the model's performance, while precision, recall, and F1-score offered insights into the classification capabilities for each class.
   
4. **Model Interpretation with LIME:**
   - LIME was employed to interpret the predictions of the Decision Tree model. It works by perturbing the input data around a specific instance and observing the changes in the model's predictions.
   - The LIME explainer was initialized with the training data, feature names, and class names, allowing for a local approximation of the model's decision-making process.
   
5. **Visualization:**
   - The Decision Tree was visualized to understand its structure and the decision rules applied.
   - LIME explanations for a selected sample instance were visualized, showing the contribution of each feature to the prediction through a bar plot.

## Results
- **Model Performance:** The Decision Tree classifier achieved an accuracy of XX% on the test set. The classification report highlighted the model's ability to distinguish between malignant and benign cases, providing detailed metrics such as precision, recall, and F1-score for both classes.
- **LIME Interpretation:** LIME provided local explanations for individual predictions, indicating the importance of various features in the model's decision-making process. These local explanations were visualized using bar plots, helping to understand the impact of each feature on the prediction.

## Discussion
The use of LIME in this project demonstrated the value of interpretability in machine learning models, particularly in sensitive applications like healthcare. By providing insights into the model's decision-making process, LIME helps build trust and understanding among users and stakeholders. The Decision Tree model, combined with LIME, offered a powerful tool for breast cancer prediction, balancing accuracy with interpretability.

## Conclusion
This project successfully developed a breast cancer prediction model using a Decision Tree classifier and demonstrated the utility of LIME for model interpretation. The LIME analysis provided clear and interpretable explanations for individual predictions, enhancing the transparency and trustworthiness of the model. This approach underscores the importance of interpretable machine learning models in healthcare, where understanding the reasoning behind predictions is as critical as the predictions themselves.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
