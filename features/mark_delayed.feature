Feature: Mark a task as delayed.
 Scenario: Mark a task as delayed
 Given the to-do list contains tasks:
 | Task | Status |
 | Buy groceries | Pending |
 When the user marks task "Buy groceries" as delayed
 Then the to-do list should show task "Buy groceries" as delayed
