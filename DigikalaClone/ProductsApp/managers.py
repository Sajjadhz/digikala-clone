from django.db.models import Manager
from django.db.models import manager


class DigiKalaManager(manager.Manager):
    def create_or_update(self, name, price):
        if self.filter(name=name).count() == 1:
            instance = self.get(name=name)
            instance.update(price=price)
        else:
            self.create(name=name, price=price)


    def refine_by_queryparams(self, request):
        query = self.all()
        params = request.GET.get('order_by', None)
        print(params)
        if params:
            try:
                query = query.order_by(params)
            except Exception as e:
                print(e)
                pass
        
        return query
        
        