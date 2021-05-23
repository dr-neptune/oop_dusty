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

class Notebook:
    """Represent a collection of notes that can be tagged, modified, and searched"""
    def __init__(self):
        """Initialize a notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=""):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """Locate the note with the given id"""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        print(f"Note id: {note_id} not found!")
        return None

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its
        memo to the given value.
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its tags to the given value"""
        self._find_note(note_id).tags = tags

    def search(self, filter):
        """
        Find all notes that match the given filter string.
        """
        return [note for note in self.notes if note.match(filter)]
