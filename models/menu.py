response.logo = A('CATS',_class="navbar-brand",_href=URL('index'))

response.menu = []
if auth.has_membership('administrator'):
    response.menu.append(('Manage',False, URL('default','manage')))
