"""Legacy monolith module.

This file intentionally mixes responsibilities for use case 11.
"""

import json


def run(batch_payload: str):
    data = json.loads(batch_payload)

    # validate (duplicated)
    if 'income' not in data:
        return {'ok': False, 'error': 'missing income'}
    if 'household_size' not in data:
        return {'ok': False, 'error': 'missing household_size'}

    income = int(data['income'])
    hh = int(data['household_size'])

    # business rules (duplicated)
    base = 18000
    per = 6000
    limit = base + per * hh

    eligible = income <= limit

    # formatting
    if eligible:
        msg = f"ELIGIBLE (income={income} <= limit={limit})"
    else:
        msg = f"NOT ELIGIBLE (income={income} > limit={limit})"

    # pretend data access (dormant path)
    if data.get('write_db') == True:
        _write_db('elig', {'income': income, 'hh': hh, 'limit': limit, 'eligible': eligible})

    return {'ok': True, 'eligible': eligible, 'message': msg}


def _write_db(table, record):
    # obsolete placeholder that does nothing
    return None
