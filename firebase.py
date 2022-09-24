import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('sb-python-firebase-adminsdk-m3m50-6478db808b.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
users_ref = db.collection(u'users')


def getProfile(id):
    user_docs = users_ref.stream()
    for doc in user_docs:
        if doc.id ==id:
            return doc.to_dict()['name'] 
    

def getUsersCoffees(id):
    coffees = []
    coffees_ref = db.collection(u'coffees')
    coffee_docs = coffees_ref.stream()
    for doc in coffee_docs:
        if(users_ref.document(id).get().to_dict()['boughtBefore'].__contains__(doc.to_dict()['id'])):
            coffees.append(doc.to_dict())
    return coffees