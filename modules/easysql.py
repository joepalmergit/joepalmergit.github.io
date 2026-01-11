import sqlite3

class EasySQL:
    def __init__(self, path):
        self.path = path
    
    def run(self, query, params=None):
        with sqlite3.connect(self.path) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            
            if query.strip().upper().startswith('SELECT'):
                results = [dict(row) for row in cur.fetchall()]
                
                if len(results) == 1:
                    return results[0]
                else:
                    return results
            else:
                con.commit()
                return cur.rowcount
