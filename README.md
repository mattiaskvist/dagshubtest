# dagshub-test

Test för dagshub integration

## Vad är XGBoost?

XGBoost står för eXtreme Gradient Boosting, och det är en populär maskininlärningsalgoritm som används för att lösa problem inom områden som klassificering, regression och ranking.

1. **Gradient Boosting:**
   - Gradient Boosting är en teknik inom maskininlärning där modeller byggs successivt för att korrigera misstag från tidigare modeller. Varje ny modell fokuserar på att korrigera de fel som gjordes av de tidigare modellerna.

2. **Xtreme Gradient Boosting (XGBoost):**
   - XGBoost är en kraftigt förbättrad version av Gradient Boosting. Det optimerar och accelererar processen genom att använda tekniker som trädbaserade ensemblemetoder.

3. **Trädbaserad Modell:**
   - Istället för att använda en enda modell, använder XGBoost flera träd (decision trees) för att göra sina förutsägelser. Varje träd bidrar med en liten bit till den totala förutsägelsen. Träden byggs successivt, där varje nytt träd fokuserar på att korrigera misstag från de tidigare träden.

4. **Funktioner och Fördelar:**
   - XGBoost har flera fördelar, såsom hantering av brusiga data, möjligheten att hantera både numeriska och kategoriska funktioner, samt att undvika överanpassning (overfitting). Algoritmen har också visat sig vara mycket effektiv och vinnare av många kaggle-tävlingar.

### Varför XGBoost?

Det problem vi har framför oss är ett så kallat multiclass classification problem, där vi ska gissa vilken spelare som spelar. Det som gör det till multiclass är att vi har flera möjliga outputs, jämfört med binary classification där vi bara har två möjliga outputs. XGBoost är en algoritm som är bra på att lösa multiclass classification problem. XGBoost är mer effektivt än andra algoritmer och är bra på att hantera stora mängder data.

Läs mer om XGBoost här: [simplilearn](https://www.simplilearn.com/what-is-xgboost-algorithm-in-machine-learning-article) och här [Nvidia](https://www.nvidia.com/en-us/glossary/xgboost/).

## Kom igång

Vi börjar med en binary classification för att komma igång. Vi ska gissa om en person har diabetes eller inte. Vi har en csv-fil med data som vi ska använda för att träna vår modell. Vi kommer att använda oss av XGBoost för att träna modellen.

### Förberedelser och Installation

Först behöver du klona detta repo:

```bash
git clone <repo>
```

Installera python 3.11. Detta kan du göra [här](https://www.python.org/downloads/).

Sedan behöver du installera virtualenv. Detta kan du göra med pip (pip borde installeras automatiskt med python):

```bash
pip install virtualenv
```

Sedan behöver du navigera till mappen för repot och skapa en environment:

```bash
virtualenv env
```

För att aktivera enviren, kör:

```bash
//mac
source env/bin/activate

//CMD
env\Scripts\activate.bat

//Powershell
env\Scripts\activate.ps1
```

För att installera de paket som krävs, kör:

```bash
pip install -r requirements.txt
```

Om du skulle vilja deaktivera ditt venv, kör:

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
pip install pandas
pip install mysql-connector-python
```

Dessa behöver installeras manuellt ifall man inte kör i en environment. Det kan skapa problem för du kan behöva lägga till dem i din specifika path, och kan vara krångligt. Därför rekommenderar jag att du kör i en environment.

På Windows kan det vara enklare att installera allt manuellt.

Om ni får ett felmeddelande "ModuleNotFoundError: No module named 'pkg_resources'" testa att köra:

``` pip install setuptools ```

#### Hämta data

Ladda ner data här: [diabetes](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv). Kopiera och lägg i repot som 'pima-indians-diabetes.csv'. Namnet är viktigt att det är exakt, annars kommer inte koden att fungera och den kommer inte att ignoreras av git (vilket vi vill).

#### Set up credentials

För att kunna pusha till dagshub behöver du skapa en .env fil i repot. I denna fil behöver du lägga till dina credentials. Detta gör du genom att i filen skriva:

```
DAGSHUB_REPO_OWNER = 'mattiaskvist'
DAGSHUB_REPO_NAME = 'dagshubtest' 
DAGSHUB_TOKEN = '<din token>'
DAGSHUB_USERNAME = '<ditt användarnamn>'
```

Enbart collaborators kan pusha till ett repo, så hit me up om du inte är collaborator.

Din token kan du hitta [här](https://dagshub.com/user/settings/tokens). Kopiera din default token som autogenereras när du skapar ett konto. Ditt användarnamn är det du loggar in med på dagshub.

Se till att .env filen inte pushas till github. Detta är en säkerhetsrisk. Kontrollera att .gitignore innehåller .env och att .env är lite grått i VSCode. Vi vill inte heller att data pushas till github. Därför är även data filen ignorerad i .gitignore.

#### Klar att köra

Nu är du redo att köra koden!
Jag rekommenderar att köra koden via VSCode. Då kan du köra koden genom att trycka på play-knappen i filen du vill köra. Fungerar det inte direkt, testa att byta interpreter till din environment. Detta kan du göra genom att trycka på interpreter längst ner till höger i VSCode. Välj din environment. Det ser ut något i stil med: 'Python 3.11.0 64-bit ('env': venv)'. Du kan också prova att i dropdownen bredvid play-knappen välja "run python file".

### Köra kod

Vill du skriva egen kod kan du följa den tutorial jag följde [här](https://machinelearningmastery.com/develop-first-xgboost-model-python-scikit-learn/) och börja från punkt 2. Kom igåg att köra i ditt venv. Följer du enbart denna tutorial så kommer inte koden eller resultaten att loggas till MLflow eller DagsHub, men du kommer kunna träna en modell och få en accuracy score i terminalen.

Vill du inte skriva egen kod kan du köra diabetes_test.py. Detta gör du genom att i VSCode trycka på play-knappen i diabetes_test.py. Skulle det inte fungera behöver du kontrollera att du aktiverat ditt venv och att du har installerat alla paket som krävs samt att du valt rätt interpreter i VSCode. Det gör du nere till höger och det ser ut något i stil med: 'Python 3.11.0 64-bit ('env': venv)'. Du kan också prova att i dropdownen bredvid play-knappen välja "run python file".

### Dagshub

När du kör koden och mlflow är aktiverat så kommer körningen att loggas till DagsHub och på en mlflow-server som hör till repot. Du kan se din körning under filken "Experiments" på DagsHub. Du kan också se den på mlflow-servern. För att komma åt den, klicka på "Go to MLflow UI" under fliken "Experiments" i repot på DagsHub. Där kan du se alla körningar som har gjorts.

För att se till experimentet och dess accuracy loggas till DagsHub, se till att du har följande kod i din fil:

```python
# Load environment variables
from dotenv import load_dotenv
from sklearn.metrics import recall_score
load_dotenv()

import os
repo_name_var = os.getenv("DAGSHUB_REPO_NAME")
repo_owner_var = os.getenv("DAGSHUB_REPO_OWNER")
dagshub_token_var = os.getenv("DAGSHUB_TOKEN")
dagshub_username_var = os.getenv("DAGSHUB_USERNAME")

os.environ['MLFLOW_TRACKING_USERNAME'] = dagshub_username_var
os.environ['MLFLOW_TRACKING_PASSWORD'] = dagshub_token_var

# Set up Dagshub and MLflow
import dagshub
import mlflow
from mlflow.tracking import MlflowClient

dagshub.init(repo_owner=repo_owner_var, repo_name=repo_name_var, mlflow=True)
mlflow.xgboost.autolog(log_input_examples=False, log_datasets=False, log_model_signatures=True, disable=False)
with mlflow.start_run() as run:
    ....
    ....
    # Kod för att ladda in data och träna modellen
    ....
    ....
    # make predictions for test data
    y_pred = model.predict(X_test)

    # evaluate predictions
    accuracy = accuracy_score(y_test, y_pred)
    run_id = run.info.run_id
    mlflow.end_run()
    
    # Log metrics
    # Här loggar vi metrics till MLflow. Accuracy, recall och precision loggas automatiskt innan
    MlflowClient().log_artifact(run_id, '<namn på filen som du kör>')
```

Log artifact är viktigt för att koden du gör ska loggas till DagsHub. Detta gör att du kan se koden som kördes. Detta är viktigt för att kunna reproducera körningen. Om du inte har med denna kod, kommer inte koden att loggas till DagsHub. Detta är bra för att vi kan spara koden som körs utan att hela tiden pusha till GitHub. Koden kan sedan hittas i MLflow UI, klicka på en körning, och sedan under "Artifacts".

Om du i DagsHub väljer "Experiments" och sedan klickar på kodsymbolen för en körning, kommer du till den commit som körningen gjordes på. Det är lite missvisande, eftersom att man testar först och pushar sen, och den commiten hela tiden kommer vara en version bakom. Att använda artifacts är därför bättre.

```python
mlflow.log_artifact("<namn på filen som du kör>")
```

## Multiclass classification

Här följde jag följande tutorial: [tutorial](https://forecastegy.com/posts/xgboost-multiclass-classification-python/) för att skriva filen multiclass_test.py

För att köra multiclass_test.py måste du ladda ner data här: [wine](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009?select=winequality-red.csv). Kopiera datan och spara som 'winequality-red.csv' i repot. Namnet är viktigt att det är exakt, annars kommer inte koden att fungera och den kommer inte att ignoreras av git (vilket vi vill).

Denna fungerar ungefär likadant som diabetes_test.py, men modellen måste gissa vilket utan 6 vin det är, jämfört med sant eller falskt som diabetes_test.py gör. Därför är det en multiclass classification.

Multiclass clasification skilljer sig från binary classification genom att den använder sig av en annan loss function, eller objective function. En loss function används för att beräkna skillnaden mellan predictions och den faktiska datan. Vi använder oss här av "multi:softprob" som är en objective function som används för multiclass classification. Den ger oss en sannolikhet för varje klass(möjlig output). Den klass med högst sannolikhet blir den som modellen gissar på.

Denna fil använder pandas för att läsa in datan, vilket även Rasmus gjorde i sin demo. Här läses också datan in från en csv-fil, men kommer att jobba med en sql-fil som vi kommer querya.


## MYSQL

För att kunna köra querys från en lokal databas behöver du installera mysql. Detta kan du göra [här](https://dev.mysql.com/downloads/installer/). En guide för mac hittar du [här](https://flaviocopes.com/mysql-how-to-install/), och en för windows [här](https://www.w3schools.com/mysql/mysql_install_windows.asp).

Du kan stöta på problem om mysql inte är tillags till din path (iallafall på mac). Detta kan du lösa genom att lägga till mysql till din path. En guide för hur du gör detta på mac hittar du [här](https://stackoverflow.com/questions/10577374/mysql-command-not-found-in-os-x-10-7). För windows hittar du en guide [här](https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho).

När du installerat mysql behöver du skapa en databas. Detta kan du göra genom att köra följande kommando i terminalen:

```bash
mysql -u root -p
```

Logga sedan in med det lösenord du angav när du installerade mysql. Skapa en databas genom att köra:

```bash
CREATE DATABASE <databasnamn>;
```

Navigera till databasen genom att köra:

```bash
USE <databasnamn>;
```

Du kan sedan skapa en tabell genom att köra exempelvis:

```bash
CREATE TABLE cats
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
  name            VARCHAR(150) NOT NULL,                # Name of the cat
  owner           VARCHAR(150) NOT NULL,                # Owner of the cat
  birth           DATE NOT NULL,                        # Birthday of the cat
  PRIMARY KEY     (id)                                  # Make the id the primary key
);
```

För att skapa tabeller och fylla dem med data genom att köra en sql-fil, anslut och navigera till databasen du vill skapa tabellerna i. Kör sedan:

```bash
source <path till sql-fil>
```

Du borde nu ha skapat en databas med tabeller och lite data. För att se att tabellerna skapats, kör:

```bash
SHOW TABLES;
```

För att querya databasen, se till att du har installerat mysql-connector-python. Detta kan du göra genom att köra:

```bash
pip install mysql-connector-python
```

eller genom att i en environment köra:

```bash
pip install -r requirements.txt
```

Nu har jag skapat en databas i MySQL som heter "data". Jag har importerat en tabell och data från filen ```table.sql``` genom att göra som jag beskrivit ovan. Här är ett exempel på hur du kan querya databasen och få ut datan i en pandas dataframe. Kom ihåg att du måste ha en .env fil med dina credentials, där du har lagt till ditt lösenord för MySQL:

```python
import mysql.connector
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

import os
password_var = os.getenv("MYSQL_PASSWORD")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=password_var,
  database="data"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, email, id FROM users")

myresult = mycursor.fetchall()

df = pd.DataFrame(myresult, columns=['name', 'email', 'id'])

print(df)
```

Output:

```bash
           name                     email  id
0      John Doe      john.doe@example.com   1
1    Jane Smith    jane.smith@example.com   2
2  Mike Johnson  mike.johnson@example.com   3
```
