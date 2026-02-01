import json
from datetime import datetime


def record_audit_event(event_name: str, details: dict):
    payload = {
        'ts': datetime.utcnow().isoformat() + 'Z',
        'event': event_name,
        'details': details,
    }
    with open('audit.log', 'a', encoding='utf-8') as f:
        f.write(json.dumps(payload) + '
')
