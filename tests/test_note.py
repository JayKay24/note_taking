import unittest

from ..classes import note

class NoteTest(unittest.TestCase):
    def setUp(self):
        self.note = note.Note("Lunch hour")
        
    def test_id_is_None(self):
        self.assertIsNone(self.note.id, 
        "id should be none")
        
    def test_search_returns_correct_output(self):
        self.obj = self.note.search('Bond')
        self.assertIsNone(self.obj)
        self.obj = self.note.search('Lunch hour')
        self.assertEqual(id(self.note), id(self.obj),
                         "should return only the note itself")
        