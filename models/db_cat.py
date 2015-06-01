db.define_table(
    'cat',
    Field('name',requires=IS_NOT_EMPTY()),
    Field('image',requires=IS_URL()),
    Field('rating','float',writable=False,readable=False),
    auth.signature)

db.define_table(
    'vote',
    Field('cat','reference cat'),
    Field('rating','float'),
    auth.signature)
