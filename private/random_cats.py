import urllib
for k in range(30):
    catapi = urllib.urlopen('http://thecatapi.com/api/images/get?format=src&type=gif')
    url = catapi.geturl()
    db.cat.insert(name="cat #%s" % k, image=url)
db.commit()
