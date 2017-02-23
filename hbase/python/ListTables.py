import happybase as hb

conn = hb.Connection()

print('Found tables:')
print(conn.tables())

conn.close()

