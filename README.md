# Simulateur de Marge pour Broker Repo

📈 Ce script simule la **marge nette d’un broker** sur une opération de repo, en prenant en compte :

- Le cash réellement prêté (haircut sur le collatéral)
- Le taux repo reçu
- Le coût de financement interne
- La durée de l’opération

## 🧪 Exemple

- Notional : 10 000 000 €
- Collatéral : 10 200 000 €
- Haircut : 2%
- Taux repo : 2.8%
- Coût de funding : 2.3%
- Durée : 5 jours

## ▶️ Exécution

```bash
python3 repo_margin_simulator.py
```

## 📦 Dépendances

Aucune dépendance externe requise ✅

## 👨‍💻 Auteur

Gabriel Benguigui  
Master Financial Markets & Risk Evaluation – TSM

## 🚀 Tester en ligne

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Gabriel-Benguigui/repo-margin-simulator/blob/main/repo_margin_simulator.ipynb)
