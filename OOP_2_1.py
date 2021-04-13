class Editor:

    def __init__(self, key):
        self.key = key

    def view_document(self):
        print("Only read in your version(Non license)")

    def edit_document(self):
        print("License version")

class ProEditor(Editor):

    def __init__(self, key):
        self.key = key

password = input("Enter your key: ")
if password == "123":
    obj = ProEditor("key")
    obj.edit_document()
else:
    obj = Editor("key")
    obj.view_document()
