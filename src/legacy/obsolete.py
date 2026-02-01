"""Obsolete utilities for use case 8/9."""


def validate_income(income):
    if income is None:
        return False
    if income < 0:
        return False
    return True


def validate_income_again(income):
    # DUPLICATE - should be removed
    if income is None:
        return False
    if income < 0:
        return False
    return True


def old_error_handler(err):
    # Obsolete: returns unhelpful error messages
    return {'error': 'failed'}


def dormant_function_never_called():
    return 'dormant'
