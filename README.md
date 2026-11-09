AI-Based Predictive Maintenance of Machines
Project overview
This project demonstrates an academic predictive-maintenance prototype that estimates the likelihood of machine failure from operating-condition inputs. A Random Forest classifier is trained on the AI4I 2020 Predictive Maintenance Dataset and is exposed through a Flask web dashboard.
Objectives
- Predict the binary machine-failure target (0 = normal, 1 = failure).
- Use machine type, air temperature, process temperature, rotational speed, torque and tool wear as model inputs.
- Evaluate the model using accuracy, precision, recall, F1-score and ROC-AUC.
- Apply a probability threshold of 0.25 to classify high-risk cases.
- Provide an interactive dashboard with a maintenance recommendation.
Dataset
AI4I 2020 Predictive Maintenance Dataset, UCI Machine Learning Repository (Dataset ID 601; DOI: 10.24432/C5HS5C). The dataset contains 10,000 records and 14 columns. The project uses six operating-condition features and the Machine failure target. Identifier columns and direct failure-mode indicator columns are excluded from model inputs.

Dataset page: https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset
Model and reported results
- Algorithm: Random Forest Classifier
- Training/test split: 80:20, stratified
- Number of trees: 200
- random_state: 42
- class_weight: balanced
- Decision threshold: 0.25
Reported held-out test results:
Metric	Result
Accuracy	98.05%
Precision	69.86%
Recall	75.00%
F1-score	72.34%
ROC-AUC	95.87%


Confusion matrix at threshold 0.25: TN = 1910, FP = 22, FN = 17, TP = 51.

These are the results documented in the supplied project report and presentation. They should be reproduced from the final training script/notebook before claiming a fresh run.
Project structure
Predictive_Maintenance_Final_Submission/
├── README.md
├── requirements.txt
└── source_code/
    ├── app.py
    ├── predictive_maintenance_model.pkl
    ├── template/
    │   └── index.html
    ├── static/
    │   ├── style.css
    │   └── script.js
    └── notebooks_training_implementation.ipynb
Installation
1. Install Python.
2. Open a terminal in the folder containing app.py.
3. Create and activate a virtual environment (recommended):
   - Windows: python -m venv .venv
   - PowerShell: .venv\\Scripts\\Activate.ps1
4. Install dependencies:
   pip install -r requirements.txt
Run the dashboard
From the source_code directory:
python app.py

Open the local address printed by Flask, usually http://127.0.0.1:5000/.
Dashboard inputs
- Machine type (L, M or H)
- Air temperature (K)
- Process temperature (K)
- Rotational speed (rpm)
- Torque (Nm)
- Tool wear (min)
The application calls predict_proba() and classifies a machine as HIGH RISK when the estimated failure probability is greater than or equal to 0.25. Otherwise it displays LOW RISK.
Important implementation note
The uploaded Flask source snapshot uses predictive_maintenance_model.pkl and the template/ directory (singular). The user's later VS Code screenshot shows a newer/different working project layout using a .joblib model, train_model.py, generate_sample_data.py, metadata.json and templates/ (plural). Those newer files were not included as attachments in this conversation. Therefore, this README and the included source snapshot describe the ZIP actually supplied here, not the newer folder shown in the screenshot. Before publishing to GitHub, replace source_code/ with the exact latest working folder and update this README's structure/model filename if needed.
Limitations
- The AI4I 2020 dataset is synthetic; results may not transfer directly to a specific industrial environment.
- The current target is binary failure prediction, not detailed failure-mode prediction or Remaining Useful Life estimation.
- False positives and false negatives remain possible.
- The model has not been validated with live industrial sensor streams.
- Real deployment requires domain validation, sensor integration, monitoring, safety review and cybersecurity controls.
Team
- Saniya Shah Zama
- Kota Rakesh
- Chinthoju Sai Manikanta
- Jabilli Chava
Project Faculty Mentor: Mr. Joydeep Roy, Assistant Professor, Department of Computer Science and Engineering.
