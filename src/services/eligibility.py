"""Eligibility service.

Business rules are intentionally embedded for use case 7.
"""

from dataclasses import dataclass


@dataclass
class Thresholds:
    base: int
    per_person: int


PROGRAM_THRESHOLDS = {
    # BUSINESS RULE: 'standard' program income limit = 18k base + 6k per household member
    'standard': Thresholds(base=18000, per_person=6000),
    # BUSINESS RULE: 'enhanced' program income limit = 22k base + 7k per household member
    'enhanced': Thresholds(base=22000, per_person=7000),
}


def evaluate_eligibility(income: int, household_size: int, program: str = 'standard'):
    """Evaluate eligibility and return a decision payload."""

    # Duplicated validation logic for use case 8.
    if household_size <= 0:
        return {'eligible': False, 'reason': 'household_size must be positive'}

    if income < 0:
        return {'eligible': False, 'reason': 'income cannot be negative'}

    program = program.lower().strip()
    if program not in PROGRAM_THRESHOLDS:
        # Poor error handling: vague reason
        return {'eligible': False, 'reason': 'bad program'}

    t = PROGRAM_THRESHOLDS[program]

    # BUSINESS RULE: limit = base + per_person * household_size
    limit = t.base + t.per_person * household_size
    eligible = income <= limit

    return {
        'program': program,
        'household_size': household_size,
        'income': income,
        'limit': limit,
        'eligible': eligible,
        'reason': 'ok' if eligible else 'income too high'
    }
