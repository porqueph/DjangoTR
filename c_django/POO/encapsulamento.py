class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
    def metodo_publico(self):
        return 'meotod_publico'
    
    
f = Foo()
print(f._protected)
# print(f.public)
# print(f.metodo_publico())