from flask import Blueprint, request, jsonify
from ..services.eligibility import evaluate_eligibility
from ..services.audit import record_audit_event

api = Blueprint('api', __name__, url_prefix='/api')


@api.get('/eligibility')
def eligibility():
    """Return an eligibility decision."""
    income = int(request.args.get('income', '0'))
    household_size = int(request.args.get('household_size', '1'))
    program = request.args.get('program', 'standard')

    decision = evaluate_eligibility(income=income, household_size=household_size, program=program)
    record_audit_event('eligibility_checked', details=decision)
    return jsonify(decision)
