import psycopg2
import psycopg2.extras
import json

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):
    """

    postgresql module used to query tables in postgresql database.

    Example: lookup('postgres_query','database=database user=user password=password sql=SQL query')

    """
    def run(self, terms, variables, **kwargs):

        ret = []
        if not isinstance(terms, list):
            terms = [terms]

        for term in terms:
            params = term.split(' ', 3)

        paramvals = {
            'database': 'database',
            'user': 'user',
            'password': 'password',
            'sql': 'query',
        }
        try:
            for param in params:
                name, value = param.split('=')
                assert(name in paramvals)
                paramvals[name] = value
        except (ValueError, AssertionError) as e:
            raise AnsibleError(e)

        # assigning args for postgresql connect
        database = paramvals['database']
        user = paramvals['user']
        password = paramvals['password']
        sql = paramvals['sql'].replace("~~eq", "=")

        # Connection to postgresql
        con = None
        try:
            con = psycopg2.connect(database=database, user=user, password=password)
            cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cur.execute(sql)
            rows = cur.fetchall()
            for row in rows:
                ret.append(dict(row))
        except Exception as e:
            raise AnsibleError("Postgres query error:" % e.message)

        finally:
            if con:
                con.close()
        jsonret = json.dumps(ret, ensure_ascii=False)
        return [jsonret]
