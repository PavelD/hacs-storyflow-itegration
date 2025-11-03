# StoryFlow Integration (Home Assistant)

**Status:** MVP skeleton – initial version  

---

## 🎯 Goal

Provide a **custom Home Assistant integration** to manage stories and tasks:

- Define **stories** (like user stories in Scrum)  
- Track tasks with states: `todo`, `progress`, `review`, `done`, `rejected`  
- Assign tasks to **persons**  
- Persist stories and tasks in Home Assistant storage  
- Prepare for **visualization in Lovelace** and automation triggers  
- Ready for **HACS integration**  

Essentially, a **mini Scrum / checklist tracker** inside Home Assistant.

---

## ✅ Functional Progress / TODO

### Implemented / Available in MVP
- [x] Initial ConfigFlow to define a story  
- [x] Story descriptions support Markdown multi-line strings  
- [x] Basic storage of stories and tasks in Home Assistant  
- [x] Tasks support states (`todo`, `progress`, `review`, `done`, `rejected`)  
- [x] Tasks can optionally be assigned to a person (`person.<name>` or `None`)  
- [x] Add support of HACS installation as custom repository  

### In Progress / Next steps (MVP → v1)
- [ ] Create new stories via `StoryManager.create_story()`  
- [ ] Clone a story (tasks reset to `todo` and `assigned_to=None`)  
- [ ] Change task states via services (`set_state`)  
- [ ] Assign/unassign tasks via services (`assign_person`)  
- [ ] Simple Lovelace card / UI template to display stories and tasks  
- [ ] Ability to view task descriptions in UI  
- [ ] Optional: mark stories as complete with aggregated progress  

### Future Enhancements (v1+)
- [ ] Enforce flow rules (`todo → progress → review → done/rejected`)  
- [ ] Full interactive Lovelace card with drag-and-drop or buttons  
- [ ] Notifications on task updates  
<!-- - [ ] Security checks and CI quality gates (Bandit, coverage threshold)  -->

---

## 📝 Notes

- Task IDs are linked to parent story for automation purposes  
- Assigned person can be `person.<name>` or `None`  
