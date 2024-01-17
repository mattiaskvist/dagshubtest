# dagshub-test

Test för dagshub integration

## Installation

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
```

Dessa behöver installeras manuellt ifall man inte kör i en environment. Det kan skapa problem för du kan behöva lägga till dem i din specifika path, och kan vara krångligt. Därför rekommenderar jag att du kör i en environment.

### Hämta data

Ladda ner data här: [diabetes](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv). Kopiera och lägg i repot som 'pima-indians-diabetes.data.csv'. Namnet är viktigt att det är exakt, annars kommer inte koden att fungera och den kommer inte att ignoreras av git (vilket vi vill).

### Set up credentials

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

### Klar att köra

Nu är du redo att köra koden!
Jag rekommenderar att köra koden via VSCode. Då kan du köra koden genom att trycka på play-knappen i filen du vill köra. Fungerar det inte direkt, testa att byta interpreter till din environment. Detta kan du göra genom att trycka på interpreter längst ner till vänster i VSCode. Välj din environment. Det ser ut något i stil med: 'Python 3.11.0 64-bit ('env': venv)'. Du kan också prova att i dropdownen bredvid play-knappen välja "run python file".

### Dagshub

När du kör koden och mlflow är aktiverat så kommer körningen att loggas till DagsHub och på en mlflow-server som hör till repot. Du kan se din körning under filken "Experiments" på DagsHub. Du kan också se den på mlflow-servern. För att komma åt den, klicka på "Go to MLflow UI" under fliken "Experiments" i repot på DagsHub. Där kan du se alla körningar som har gjorts.

För att se till experimentet och dess accuracy loggas till DagsHub, se till att du har följande kod i din fil:

```python
dagshub.init(repo_owner=repo_owner_var, repo_name=repo_name_var, mlflow=True)
with mlflow.start_run():'
    ...
    # Kod för att träna modellen
    ...
    mlflow.log_param('accuracy', accuracy)
    mlflow.log_artifact("<namn på filen som du kör>")

    mlflow.end_run()
```

Log artifact är viktigt för att koden du gör ska loggas till DagsHub. Detta gör att du kan se koden som kördes. Detta är viktigt för att kunna reproducera körningen. Om du inte har med denna kod, kommer inte koden att loggas till DagsHub. Detta är bra för att vi kan spara koden som körs utan att hela tiden pusha till GitHub. Koden kan sedan hittas i MLflow UI, klicka på en körning, och sedan under "Artifacts".

Om du i DagsHub väljer "Experiments" och sedan klickar på kodsymbolen för en körning, kommer du till den commit som körningen gjordes på. Det är lite missvisande, eftersom att man testar först och pushar sen, och den commiten hela tiden kommer vara en version bakom. Att använda artifacts är därför bättre.

```python
mlflow.log_artifact("<namn på filen som du kör>")
```
