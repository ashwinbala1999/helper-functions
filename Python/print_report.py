from sklearn.metrics import confusion_matrix, classification_report

# just send the y_test and pred values with comparable shapes
def generate_report(actual, pred, thresh=0.5):
    pred = pred>thresh
    
    print("Confusion Matrix:")
    print(confusion_matrix(actual, pred))
    print("\nClassification Report:")
    print(classification_report(actual, pred))
