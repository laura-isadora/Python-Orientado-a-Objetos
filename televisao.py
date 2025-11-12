class Televisao:
    def __init__(self, canal=1, canal_min=1, canal_max=5):
        self.canal = canal
        self.canal_min = canal_min
        self.canal_max = canal_max

    def aumentar(self):
        if self.canal < self.canal_max:
            self.canal += 1
        else:
            self.canal = self.canal_min

    def diminuir(self):
        if self.canal > self.canal_min:
            self.canal -= 1
        else:
            self.canal = self.canal_max

tv = Televisao()
tv.aumentar()
print(tv.canal) #canal 2
tv.aumentar()
tv.aumentar()
tv.aumentar()
tv.aumentar()
print(tv.canal) #canal 1, voltou pro inicio