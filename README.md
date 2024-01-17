# dagshub-test

Test för dagshub integration

## Installation

```bash

pip install virtualenv
python3.11 -m venv env
```

För att aktivera enviren:

```bash
//mac
source env/bin/activate

//CMD
env\Scripts\activate.bat

//Powershell
env\Scripts\activate.ps1
```

För att installera paket:

```bash
pip install -r requirements.txt
```

För att deaktivera enviren:

```bash
deactivate
```

De paket som installeras är:

```bash
pip install mlflow 
pip install dagshub
pip install xgboost
pip install scikit-learn
pip install numpy
pip install python-dotenv 
```

Detta behövs bara ifall man inte kör i en environment.

## Hämta data

Ladda ner data här: [diabetes](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv). Kopiera och lägg i repot som 'pima-indians-diabetes.data.csv'.

## Set up credentials

Ditt username är ditt användarnamn på dagshub och password är ditt token. Detta kan du hitta på dagshub under settings långt ner.

```bash
export MLFLOW_TRACKING_USERNAME=<username>
export MLFLOW_TRACKING_PASSWORD=<password/token>
```
