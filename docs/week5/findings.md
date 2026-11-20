# Findings and Hidden-Bug Explanation


## Findings

| Location | Evidence | Finding | Impact | Action |
|---|---|---|---|---|
| `grades.py` | Manual review | Conditional grade thresholds | Boundary mistakes are possible if comparisons are wrong | Add tests at every specified boundary |
| Original Kata | Source required | Hidden bug not yet verified | An invented explanation may be incorrect | Reproduce it against the assignment specification |

## Extra code smells

For each verified smell, record the file/line, evidence, impact, and proposed
small refactoring. Do not list generic smells unless they exist in your code.

## Hidden bug

**Not yet established.** Document:
1. Triggering input.
2. Expected result from the assignment.
3. Actual result from original code.
4. Root cause.
5. Regression test proving the fix.
