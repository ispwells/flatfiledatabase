import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
class Record:
    def __init__(self,id,forename,surname,age,email):
        self.id = id
        self.forename = forename
        self.surname = surname
        self.age = age
        self.email = email
    def to_csv(self):
        return f"{self.id},{self.forename},{self.surname},{self.age},{self.email}"

class FlatFileDataBase:
    def __init__(self,filename):
        self.filename = filename
    def save_record(self,record):
        with open(self.filename,"a") as file:
            file.write(record.to_csv() + "\n")
    def read_record(self):
        with open(self.filename,"r") as file:
            return [line.strip().split(",") for line in file]
    def delete_record(self,record_id):
        record = self.read_record()
        records = [record for record in record if record[0] != str(record_id)]
        with open(self.filename,"w") as file:
            for record in records:
                file.write (",".join(record)+"\n")


db = FlatFileDataBase("database.txt")
#record1 = Record(1,"Alice","Smith",30,"alice@example.com")
#record2 = Record(2,"Bob","Brown",25,"bob@example.com")
#record3 = Record(3,"Andrew","Kelly",16,"Akelly@example.com")
#db.save_record(record1)
#db.save_record(record2)
#db.save_record(record3)
def adding():


    userid = st.number_input("please enter the user id")
    firstname = st.text_input("please enter the first name")
    lastname = st.text_input("please enter the last name")
    year = st.number_input("please enter the age of user")
    emailcontact = st.text_input("please enter the email")
    record4 = Record(userid,firstname,lastname,year,emailcontact)
    db.save_record(record4)

# Read records
records = db.read_record()
st.write("Records in the database:")
for rec in records:
    st.write(rec)

# Delete a record
selection = st.radio("Please choose add or delete User",[":rainbow[add]", ":rainbow[delete]"])
if selection == ":rainbow[delete]":
    selcter = st.number_input("please enter a number to delete a user please use the ID")
    db.delete_record(selcter)
    st.write("Updated records:")
    records = db.read_record()
    for rec in records:
        st.write(rec)
elif selection== ":rainbown[add]":
    adding()
