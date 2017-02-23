import happybase as hb

conn = hb.Connection()

table = conn.table('emp')

row = table.row(b'row1')
name = row[b'personal:name']
city = row[b'personal:city']

print('name {} city: {}'.format(name, city))

conn.close()

