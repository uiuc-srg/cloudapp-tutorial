import happybase as hb

conn = hb.Connection()

table = conn.table('emp')
columns = (b'personal:name', b'personal:city')

for key, data in table.scan(columns=columns, include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

conn.close()

