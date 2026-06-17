# projet-finance

Pipeline de données financières end-to-end, de la collecte brute jusqu'à un système de questions-réponses en langage naturel.

## Objectif

Construire un pipeline complet autour de données boursières (Apple / Yahoo Finance) :
collecte automatisée → stockage PostgreSQL → transformation dbt → visualisation Power BI → RAG (questions en langage naturel sur les données).

## Stack technique

| Couche | Outil |
|---|---|
| Collecte | Python, yfinance, pandas |
| Stockage | PostgreSQL, psycopg2 |
| Transformation | dbt |
| Visualisation | Power BI |
| LLM / RAG | Ollama (llama3.2) ou LangChain, pgvector |
| Conteneurisation | Docker |

## Architecture des données

```
cours_apple (bronze)
    └── silver_cours_apple    variation absolue, variation %
            └── gold_cours_apple    MA 7j, MA 30j, volume moyen, volatilité
```

## Installation

### Prérequis

- Python 3.13.14
- PostgreSQL 18
- dbt-postgres
- Docker (requis pour pgvector et la brique RAG)
- Ollama ou LangChain

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd projet-finance
```

### 2. Créer et activer l'environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

### 4. Configurer la connexion PostgreSQL

Créer le fichier `~/.dbt/profiles.yml` et renseigner :

```
host: 127.0.0.1
port: 5432
database: <nom_de_la_base>
user: <user>
password: <mot_de_passe>
```

### 5. Collecter les données

```bash
python recuperer_donnees.py
```

### 6. Lancer les transformations dbt

```bash
dbt run
dbt test
```

## Structure du projet

```
projet-finance/
├── README.md
├── recuperer_donnees.py
└── financial_dashboard/
    ├── models/
    │   ├── silver/
    │   │   └── silver_cours_apple.sql
    │   └── gold/
    │       └── gold_cours_apple.sql
    ├── requirements.txt
    └── dbt_project.yml
```

## Statut

Terminé : Collecte et nettoyage des données, Stockage PostgreSQL, Modèle Silver, Modèle Gold

À faire : Docker + pgvector, Brique RAG, Power BI, Automatisation (Task Scheduler)
