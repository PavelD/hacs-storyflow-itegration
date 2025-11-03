pytest_plugins = ["pytest_homeassistant_custom_component"]

import pytest


@pytest.fixture(autouse=True)
def enable_storyflow_integration(enable_custom_integrations):
    """Ensure storyflow integration is enabled for all tests."""
    yield
