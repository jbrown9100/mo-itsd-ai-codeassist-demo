from ..data.db import init_db, insecure_search_people

_db_ready = False


def search_people(q: str):
    global _db_ready
    if not _db_ready:
        init_db()
        _db_ready = True
    return insecure_search_people(q)
