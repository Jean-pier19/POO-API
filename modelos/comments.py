from modelos.post import Posts

class Comments(Posts):
    def __init__(self,postId=0, id=0, name='', email='',body=''):
        super().__init__(id=postId)
        self.postId = postId
        self.id = id
        self.name = name
        self.email = email
        self.body = body