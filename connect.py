import pymongo
from mongoengine import connect

def connect_db(name_db='post'):
    uri =f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/post?retryWrites=true&w=majority"
    connect(host=uri)
    client = pymongo.MongoClient(uri)
        # f"mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/{name_db}?retryWrites=true&w=majority")
       
    database_name = name_db
    if database_name in client.list_database_names():
        print(f"База данных {database_name} существует.")
        
        try:
            client.admin.command('ping')
            
            # return "Pinged your deployment. You successfully connected to MongoDB!"
        except Exception as e:
            return e
    else:
        print(f"База данных {database_name} не существует.")
    client.close()
    return uri
    
    

if __name__ == '__main__':
    connect_db('post')
    