class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_list = []
        self.redo_list = []

    def make_changes(self, new_text):
        self.undo_list.append(self.document)
        self.document += new_text
        self.redo_list.clear()  # Corrected

    def undo(self):
        if self.undo_list:
            self.redo_list.append(self.document)
            self.document = self.undo_list.pop()  # Actually revert
            print(self.document)
        else:
            print("DO NOTHING")

    def redo(self):
        if self.redo_list:
            self.undo_list.append(self.document)
            self.document = self.redo_list.pop()
            print(self.document)
        else:
            print("DO NOTHING")
