python manage.py shell
from task1.models import Buyer
Buyer.objects.all()
Buyer.objects.create(name='Sergey', balance=1500, age=34)
Buyer.objects.create(name='Terminator2000', balance=2500, age=54)
Buyer.objects.create(name='Maxim', balance='0.5', age='16')
from task1.models import Game
Game.objects.all()
Game.objects.create(title='Cyberpunk2077', cost=31, size=46.2, description='Game of the year', age_limited='True')
Game.objects.create(title= 'Mario', cost =0.8, size =1, description = 'Maybe interesting', age_limited = False)
Game.objects.create(title='Hitman', cost=24, size=36.2, description='Who kills Mark?', age_limited='True')
buyer_1=Buyer.objects.get(id=1)
buyer_2=Buyer.objects.get(id=2)
buyer_3=Buyer.objects.get(id=3)
Game.objects.get(id=1).buyer.set((buyer_1, buyer_2))
Game.objects.get(id=2).buyer.set((buyer_1, buyer_3))
Game.objects.get(id=3).buyer.set((buyer_1, buyer_2))