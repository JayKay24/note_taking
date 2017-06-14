from .note import Note

class NoteTake:
    def __init__(self):
        self.__notes = []
        
    def create_note(self, content):
        """
        Create a note.
        """
        note = Note(content)
        self.__notes.append(note)
        for i in range(len(self.__notes)):
            self.__notes[i].note_id = i
        print("Note created successfully.")
            
    def view_note(self, note_id):
        """
        View a note.
        """
        a_note = None
        for note in self.__notes:
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
        for note in self.__notes:
            if note.note_id == note_id:
                self.__notes.pop(note_id)
                print("Note was successfully deleted.")
                break
    
    def list_notes(self):
        for note in self.__notes:
            print(note.note_id, note.content)
            
    def search_notes(self, query_string):
        """
        Search all notes for the query_string.
        """
        found_notes = []
        for note in self.__notes:
            found = note.search(query_string)
            # The note was found.
            if found is not None:
                found_notes.append(found)
        for note in found_notes:
            print(note.note_id, note.content)
        