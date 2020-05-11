from app import db


# the stored procedures in the database use the same name as the key from the forms.py selection
def get_stat_total(stat, account_id, begin_time, queue):
    query = """
        CALL {} ('{}', {}, {})
    """.format(stat, account_id, queue, begin_time)
    return db.engine.execute(query)


def get_stat_by_champ(stat, account_id, begin_time, queue):
    query = """
        CALL {}_by_champ ('{}', {}, {})
    """.format(stat, account_id, queue, begin_time)
    return db.engine.execute(query)
