# Simulateur de Marge pour Broker Repo

# Paramètres de l'opération
notional = 10_000_000         # Montant prêté par le broker
collateral_value = 10_200_000 # Valeur du collatéral
repo_rate = 0.028             # Taux de repo (2.8%)
haircut = 0.02                # Haircut (2%)
funding_cost = 0.023          # Coût de financement (2.3%)
duration_days = 5             # Durée en jours

# Calculs
effective_collateral = collateral_value * (1 - haircut)
cash_lent = min(notional, effective_collateral)

interest_received = cash_lent * repo_rate * duration_days / 360
interest_paid = cash_lent * funding_cost * duration_days / 360

pnl = interest_received - interest_paid

# Résultat
print(f"Cash prêté         : {cash_lent:,.2f} €")
print(f"Intérêts reçus     : {interest_received:,.2f} €")
print(f"Coût de funding    : {interest_paid:,.2f} €")
print(f"➡️  Marge nette broker : {pnl:,.2f} €")
