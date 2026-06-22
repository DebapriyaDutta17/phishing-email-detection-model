# 🛡️ Phishing Email Detection Model

## 📌 Project Overview

Phishing attacks remain one of the most common cybersecurity threats, targeting users through deceptive emails designed to steal sensitive information such as passwords, banking details, and personal data.

This project presents a **Machine Learning-based Phishing Email Detection System** developed using **Python** and **Scikit-learn**. The model analyzes email content and URL-based features to automatically classify emails as **Phishing** or **Safe (Legitimate)**.

By leveraging Natural Language Processing (NLP) techniques and machine learning algorithms, the system helps identify potentially malicious emails with high accuracy, providing an additional layer of protection against cyber threats.

---

## 🎯 Objectives

* Detect phishing emails using Machine Learning.
* Extract meaningful features from email text.
* Analyze URL patterns commonly found in phishing attacks.
* Classify emails as:

  * ⚠️ Phishing
  * ✅ Safe
* Evaluate model performance using industry-standard metrics.

---

## 🚀 Features

✅ Email Text Analysis using TF-IDF

✅ URL Detection and Analysis

✅ Machine Learning Classification

✅ Real-Time Email Prediction

✅ Accuracy Score Evaluation

✅ Confusion Matrix Visualization

✅ Classification Report Generation

✅ Easy-to-Use Command Line Interface

---

## 🛠️ Technologies Used

| Technology               | Purpose                        |
| ------------------------ | ------------------------------ |
| Python                   | Programming Language           |
| Pandas                   | Data Processing                |
| NumPy                    | Numerical Operations           |
| Scikit-learn             | Machine Learning               |
| TF-IDF Vectorizer        | Text Feature Extraction        |
| Random Forest Classifier | Classification Model           |
| Matplotlib               | Data Visualization             |
| Seaborn                  | Confusion Matrix Visualization |

---

## 📊 Machine Learning Workflow

### 1️⃣ Data Collection

The dataset contains phishing and legitimate email samples labeled as:

| Label | Meaning  |
| ----- | -------- |
| 1     | Phishing |
| 0     | Safe     |

---

### 2️⃣ Data Preprocessing

* Text Cleaning
* URL Extraction
* Feature Engineering
* TF-IDF Vectorization

---

### 3️⃣ Model Training

The project uses:

**Random Forest Classifier**

Reasons for selection:

* High Accuracy
* Robust Performance
* Handles Text Features Efficiently
* Less Overfitting Compared to Single Decision Trees

---

### 4️⃣ Model Evaluation

Performance metrics include:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 📈 Sample Output

```text
Accuracy: 97.80%

Classification Report:

              precision    recall    f1-score
Safe             0.98      0.97      0.97
Phishing         0.98      0.99      0.98
```

---

## 🧪 Example Predictions

### Input

```text
Congratulations! Click here to claim your free prize now.
```

### Output

```text
⚠️ Phishing Email Detected
```

---

### Input

```text
Meeting scheduled for tomorrow at 10 AM.
```

### Output

```text
✅ Safe Email
```

---

## 📉 Confusion Matrix

The confusion matrix provides a visual representation of:

* True Positives
* True Negatives
* False Positives
* False Negatives

This helps evaluate the model's effectiveness in detecting phishing attempts.

---

## 🔐 Real-World Applications

* Email Security Systems
* Corporate Email Monitoring
* Spam Detection Platforms
* Cybersecurity Research
* Threat Intelligence Solutions
* Educational Cybersecurity Projects

---

## 💡 Future Enhancements

* Deep Learning (LSTM/BERT)
* Email Header Analysis
* Attachment Scanning
* URL Reputation Checking
* Web-Based User Interface
* Browser Extension Integration
* Real-Time Email Monitoring

---

## 📚 Key Learning Outcomes

Through this project, I gained hands-on experience in:

* Machine Learning Classification
* Natural Language Processing
* Feature Engineering
* Cybersecurity Analytics
* Model Evaluation Techniques
* Data Visualization
* Python-Based Security Applications

---

## 🤝 Contribution

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit pull requests.

---

## 📜 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Debapriya Dutta**

B.Tech CSE (Big Data Analytics)
SRM Institute of Science and Technology, Ramapuram

Aspiring Data Scientist | Machine Learning Enthusiast | Full Stack Developer | Cybersecurity Learner

---

⭐ If you found this project useful, consider giving it a star on GitHub!
