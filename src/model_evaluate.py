import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, auc
import seaborn as sns
import numpy as np

class ModelEvaluator:
    def __init__(self,y_pred,y_pred_proba,y_test,random_search,categorical_cols,numerical_cols):
        self.y_test = y_test
        self.y_pred = y_pred
        self.y_pred_proba = y_pred_proba
        self.categorical_cols = categorical_cols
        self.numerical_cols = numerical_cols
        self.best_model = random_search.best_estimator_

    def evaluate(self):

        print("Classification Report:\n", classification_report(self.y_test, self.y_pred))
        print(self.__analyse_conversion_rate())
        self.__plot_feature_importance()
        self.__plot_confusion_matrix()

    def __plot_confusion_matrix(self):
        cm = confusion_matrix(self.y_test, self.y_pred, labels=[0,1])
        cm_percent = cm / cm.sum() * 100

        labels = np.array([f"{v}\n({p:.1f}%)" for v, p in zip(cm.flatten(), cm_percent.flatten())])
        labels = labels.reshape(cm.shape)
        plt.figure(figsize=(6,4))
        sns.heatmap(cm, annot=labels, fmt='', cmap="Reds", cbar=False)
        plt.xlabel('Predicted')
        plt.ylabel('Real')
        plt.title('Confusion Matrix')
        plt.show()


    def __plot_feature_importance(self):
        encoder = self.best_model.named_steps['preprocess'].transformers_[0][1] 
        ohe_columns = encoder.get_feature_names_out(self.categorical_cols)
        all_columns = list(ohe_columns) + self.numerical_cols

        model = self.best_model.named_steps['model']

        importances = model.feature_importances_

        plt.figure(figsize=(10, 6))
        plt.barh(all_columns, importances, color='#f44f39')
        for index, value in enumerate(importances):
            plt.text(value, index, f'{value:.2f}', va='center', ha='left')

        plt.title('Feature Importance')
        plt.xlabel('Importance')
        plt.tight_layout()
        plt.show()

    def __analyse_conversion_rate(self):
        y_test_dist = pd.Series(self.y_test).value_counts(normalize=True)
        y_pred_dist = pd.Series(self.y_pred).value_counts(normalize=True)

        y_test_rate = y_test_dist[1]
        y_pred_rate = y_pred_dist[1]

        impact = (y_pred_rate - y_test_rate) * 100
        if impact >= 0:
            conclusion = (f"The model increased the conversion rate by +{impact:.1f}% compared to the actual base.")
        else:
            conclusion = (f"The model reduced the conversion rate by {abs(impact):.1f}% compared to the actual base.")  
        return conclusion