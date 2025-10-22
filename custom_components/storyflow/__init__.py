from homeassistant.core import HomeAssistant

DOMAIN = "storyflow"

async def async_setup(hass: HomeAssistant, config: dict):
    """Setup StoryFlow component."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Setup from config entry."""
    return True
