class StorageHandler:
    """Wrapper for HA storage .storage/storyflow"""

    def __init__(self, hass):
        self.hass = hass
        self.store = {}

    async def save_story(self, story_id, data):
        self.store[story_id] = data

    async def load_story(self, story_id):
        return self.store.get(story_id)
