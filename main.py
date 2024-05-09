import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': '************'
})

ref = db.reference('/')

data = ref.get()


df = pd.DataFrame.from_dict(data)

df.to_excel("firebase_data.xlsx", index=False)

print("Dados do Firebase foram escritos no arquivo 'firebase_data.xlsx'.")
