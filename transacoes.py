from dataclasses import dataclass
from categorias import Categoria
@dataclass

class Transacao:
    desc: str
    valor: float
    categoria: Categoria
    
    def exibir(self):
        print(f"Esta transacao eh uma {self.categoria.nome}, com valor: {self.valor:.2f}. Descricao: {self.desc}.")