# GHAS / Code Security demo notes (Use case 5 + reporting)

If GitHub Code Security (or GHAS) is enabled for the repo:

1. Enable CodeQL (Security → Code scanning → Set up).
2. Trigger a scan by opening a PR.
3. Use Copilot Autofix on a CodeQL alert to generate a fix suggestion.
4. Optional: use Copilot coding agent to remediate one or more alerts via a PR.
5. Show reporting by:
   - PR checks (Actions)
   - Code scanning alert status changes (open → fixed)
   - PR summary describing what changed
