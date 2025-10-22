async def async_setup_services(hass):
    """Register services."""

    async def set_state_service(call):
        task_id = call.data["task_id"]
        new_state = call.data["new_state"]
        # TODO: find task entity and set state

    async def assign_service(call):
        task_id = call.data["task_id"]
        person_id = call.data.get("person_id")
        # TODO: find task entity and set assigned_to

    async def clone_story_service(call):
        story_id = call.data["story_id"]
        new_title = call.data.get("new_story_name")
        # TODO: call story_manager.clone_story
