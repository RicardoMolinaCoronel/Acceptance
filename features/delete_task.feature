Feature: Delete a task in the to-do list.
 Scenario: Delete a task in the to-do list
 Given the to-do list contains tasks:
| Task |
| Buy groceries |
| Pay bills |
 When the user marks task "Buy groceries" user marks task "Buy groceries" to be deleted
 Then the to-do list shouldn't show task "Buy groceries"
