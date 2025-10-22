class StoryManager:
    """Handles stories and their tasks."""

    def __init__(self, storage_handler):
        self.storage = storage_handler

    def create_story(self, title, description):
        """Create a new story."""
        pass

    def clone_story(self, story_id, new_title):
        """Clone a story: tasks reset to todo + assigned_to=None."""
        pass
