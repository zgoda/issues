from flask_restful import Resource

from .models import ToDo


class TodoCollectionResource(Resource):

    def get(self):
        items = [i.to_dict() for i in ToDo.select()]
        return {'todos': items}
