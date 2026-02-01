# Use Case Cards (Ready-to-run Copilot prompts)

Copy/paste these prompts into Copilot Chat in VS Code or GitHub.com.

Tip: Start with: **Use only this repository as context.**

---

## Use case 1 — Documenting code (create a technical design doc)

```text
Create a technical design document (TDD) for this repository.
- Use docs/technical-design-template.md as the structure.
- Describe architecture, data flow, main modules, and endpoints.
- Extract and list business rules, including eligibility thresholds.
- Include an ASCII or Mermaid diagram.
- Add a testing strategy and a rollback/undo strategy.
Output: docs/technical-design.md
```

## Use case 2 — Interrogating existing code (impact of changing an input)

Scenario: Change standard program per_person threshold from 6000 to 6500.

```text
Analyze the downstream programmatic impact of changing the standard program per_person threshold from 6000 to 6500.
- Identify all places the value appears or is implied.
- Identify impacted tests and documents.
- Propose code changes with a minimal diff.
- Provide a risk list (behavior changes, edge cases).
- Update or add tests to cover the change.
```

## Use case 3 — Improving testing (generate tests)

```text
Generate a comprehensive pytest test suite for src/services/eligibility.py.
Include boundary tests, program variants, invalid inputs, and coverage gap notes.
Update tests/test_eligibility.py accordingly.
```

## Use case 4 — Converting code (legacy to modern)

Option A (COBOL → Java)

```text
Convert legacy/cobol/ELIGCALC.cbl to modern Java.
- Preserve business logic.
- Provide a Java class with evaluateEligibility(income, householdSize) -> boolean.
- Include a small main() to print the result.
- Add minimal JUnit tests.
```

Option B (refactor monolith)

```text
Refactor src/legacy/monolith.py to reuse src/services/eligibility.py.
- Remove duplicated business rules/validation.
- Keep behavior the same.
- Add tests to ensure parity.
```

## Use case 5 — Remediating vulnerabilities

```text
Find and remediate security vulnerabilities in this repository.
Focus on SQL injection in src/data/db.py and template safety in src/templates/search.html.
Provide: explanation of each issue, code changes to fix, and regression tests.
```

## Use case 6 — Generate new function to add new functionality

Scenario: Add /api/eligibility/explain.

```text
Add a new API endpoint /api/eligibility/explain.
- Same query params as /api/eligibility.
- Response includes threshold base/per_person, computed limit, eligible, and a human-readable explanation.
- Update routing, docs, and add tests.
```

## Use case 7 — Extract business rules out of code

```text
Extract all business rules from the repository.
Create docs/business-rules.md with: rule description, parameters, code location (file + function), and examples.
```

## Use case 8 — Identify obsolete/redundant/duplicate code

```text
Identify obsolete/redundant/duplicate code.
Focus on src/legacy/obsolete.py and duplicated validation/threshold logic.
Propose and implement a cleanup plan with minimal risk.
Replace unhelpful error handling with user-friendly messages.
```

## Use case 9 — Comment out/delete non-functional code

```text
Delete or comment out the non-functional code identified in use case 8.
Ensure behavior remains correct and add/adjust tests to prevent regressions.
Summarize what was removed and why.
```

## Use case 10 — Reporting mechanism for success/failure of 8 and 9

```text
Create a reporting mechanism to show success/failure of the cleanup.
Add docs/cleanup-report.md capturing: files changed, functions removed, tests added, and CI status.
Describe how this ties to PR checks and GitHub Actions.
```

## Use case 11 — Decompose (break monolith into modules)

```text
Decompose src/legacy/monolith.py into smaller modules.
Group by responsibility (parsing, validation, business logic, formatting, persistence).
Avoid circular dependencies. Keep public interfaces small and documented.
Return: folder structure, new module files, updated imports, and tests.
```
