def index():
    login = A('login to post',_href=URL('user/login'),_class='btn btn-primary')
    form = SQLFORM(db.cat).process() if auth.user else login
    cats = db(db.cat).select(orderby=~db.cat.rating)
    return locals()

@auth.requires_login()
def vote():
    cat_id = request.vars.cat
    vote = db.vote(cat = cat_id, created_by = auth.user.id)
    if vote:  vote.update_record(rating = request.vars.rating)
    else:     db.vote.insert(cat = cat_id, rating = request.vars.rating)
    avg = db.vote.rating.avg()
    row = db(db.vote.cat == cat_id).select(avg).first()
    db(db.cat.id == cat_id).update(rating = row[avg])

def user():
    return dict(form=auth())

@auth.requires_membership('administrator')
def manage():
    db.cat.url.represent = lambda v,r: A('image',_href=v)
    grid = SQLFORM.grid(db.cat)
    return locals()

def cats():
    return dict(data=db(db.cat).select().as_list())
