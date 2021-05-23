import datetime

# store the next available id for all new notes
LAST_ID = 0

class Note:
    """
    Represent a note in the notebook. Match against a string and store tags for each note.
    """
    def __init__(self, memo, tags=""):
        """
        Initialize a note with memo and optional space separated tags.
        Automatically set the note's creation date and unique ID
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global LAST_ID
        LAST_ID += 1
        self.id = LAST_ID

    def match(self, filter):
        """
        Determine if this note matches the filter text.
        Return true if it matches, False otherwise.
        Search is case sensitive and matches both text and tags.
        """
        return filter in self.memo or filter in self.tags
