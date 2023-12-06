import pandas as pd

# Charger les fichiers CSV
carac = pd.read_csv("carac.csv",sep=';')
lieux = pd.read_csv("lieux.csv",sep=';')
veh = pd.read_csv("veh.csv",sep=';')
vict = pd.read_csv("vict.csv",sep=';')

# Fusionner les DataFrames
victime = vict.merge(veh,on=['Num_Acc','num_veh'])
accident = carac.merge(lieux,on = 'Num_Acc')
merged_df = victime.merge(accident,on='Num_Acc')

# Afficher le DataFrame fusionné
print(merged_df)

# Enregistrer le DataFrame fusionné dans un nouveau fichier CSV
merged_df.to_csv('merged_data.csv', index=False)
