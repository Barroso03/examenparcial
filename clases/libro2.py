class libro():
   def __init__(self,autor,ISBN,titulo):
    self.autor = autor
    self.ISBN = ISBN
    self.titulo = titulo
   

   def set_autor(self,autor):
        self.autor=autor
        autor = ("Jorge Barroso")
   def get_autor(self):
        return self.autor
   
   def set_ISBN(self,ISBN):
        self.ISBN=ISBN
        ISBN=123456789
   def get_ISBN(self):    
        return self.ISBN

   def set_titulo(self,titulo):
        self.titulo=titulo
        titulo = ("Los bro los mejores")
    
   def get_titulo(self):
        return self.titulo


print("Ejercicio 1:")
print(libro.get_autor(1))
print(libro.get_ISBN(2))
print(libro.get_titulo(3))
# no va
