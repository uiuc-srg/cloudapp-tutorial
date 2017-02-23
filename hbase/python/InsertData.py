import happybase as hb

conn = hb.Connection()

table = conn.table('emp')

data = {
    b'personal:name': b'Raju',
    b'personal:city': b'Hyderabad',
    b'professional:designation': b'Manager',
    b'professional:salary': b'50000'
}

table.put(b'row1', data)

print('Inserted data')

conn.close()

