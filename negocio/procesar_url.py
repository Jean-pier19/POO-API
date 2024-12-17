import auxiliares.URL as urls

def url_tipo(tipo):
    url = f"{urls.url_jsonplaceholder}{tipo}"
    return url

def id_url(url_id):
    url = f"{url_tipo('posts')}/{url_id}"
    return url