import pandas as pd

# Charger les fichiers CSV
vict_df = pd.read_csv('vict.csv', sep='\t')
carac_df = pd.read_csv('carac.csv', sep='\t')
lieux_df = pd.read_csv('lieux.csv', sep='\t')
veh_df = pd.read_csv('veh.csv', sep='\t')

# Fusionner les DataFrames
merged_df = pd.merge(vict_df, carac_df, on='Num_Acc', how='inner')
merged_df = pd.merge(merged_df, lieux_df, on='Num_Acc', how='inner')
merged_df = pd.merge(merged_df, veh_df, on='Num_Acc', how='inner')

# Afficher le DataFrame fusionné
print(merged_df)

# Enregistrer le DataFrame fusionné dans un nouveau fichier CSV
merged_df.to_csv('merged_data.csv', index=False)
