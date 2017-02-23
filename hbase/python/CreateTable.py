import happybase as hb

conn = hb.Connection()

cf = {
    'personal': dict(),
    'professional': dict()
}

conn.create_table('emp', cf)
print('Created table emp')

conn.close()

