from mongoengine import Document, StringField, BooleanField, connect

uri = "mongodb+srv://user_python:54321@cluster0.yypw24v.mongodb.net/post?retryWrites=true&w=majority"
connect(host=uri)

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(max_length=40)
    phone_number = StringField(max_lenght=20)
    send_preference = StringField(choices=["SMS", "Email"], default="Email")
    confirm = BooleanField(default=False)
