from src.services.eligibility import evaluate_eligibility


def test_negative_income_is_rejected():
    r = evaluate_eligibility(income=-1, household_size=2)
    assert r['eligible'] is False

# TODO: add more tests (use case 3)
