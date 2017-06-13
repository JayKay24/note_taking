from note import Note

class NoteTake:
    def __init__(self):
        self.notes = []
        
    def create_note(self, content):
        """
        Create a note.
        """
        note = Note(content)
        self.notes.append(note)
        for i in range(len(self.notes)):
            self.notes[i].note_id = i
            
    def view_note(self, note_id):
        """
        View a note.
        """
        a_note = None
        for note in self.notes:
            if note.note_id == note_id:
                a_note = note
        if a_note is None:
            print("No note was found")
        else:
            print(a_note.content)
            
    def delete_note(self, note_id):
        """
        Deletes a note.
        """
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.pop(note_id)
                print("Note was successfully deleted.")
                break
        
        