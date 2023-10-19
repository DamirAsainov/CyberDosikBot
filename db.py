import psycopg2

class BotDB:

    def __init__(self, dbb_file):
        self.conn = psycopg2.connect(dbb_file)
        self.cursor = self.conn.cursor()
