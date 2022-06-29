from serie import Serie
from user import User

# Crear objetos
user1 = User('Santiago')
user2 = User('Jorge')
serie = Serie('Stranger Things')

# Suscribir objetos
serie.publisher.subscribe(user1)

# Comprobar notificaciones
serie.add_episode('T4:01 - Cosas raras')
