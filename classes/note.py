"""
This module defines a class Note which will be used to
create Note objects.
"""
class Note:
    """
    Class to create Note objects.
    """
    def __init__(self, content):
        self.id = None
        self.content = content
        
    def search(self, query_string):
        """
        If a match is found, return this object.
        """
        if query_string in self.content:
            return self