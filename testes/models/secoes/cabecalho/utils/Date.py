from dataclasses import dataclass
from typing import Dict, Tuple
  

@dataclass
class Ano:
    value: int
    description : str = "Ano da reunião"
    
    @classmethod
    def set_year(cls, ano: int) -> 'Ano':
        """Cria uma instância de Ano e define se é bissexto.

        Args:
            ano (int): ano por extenso

        Returns:
            Ano: Objeto representando o ano.
        """
        return cls(int(ano))
    
    def is_bissexto(self) -> bool:
        """Verifica se um ano é bissexto."""
        return (self.value % 4 == 0 and self.value % 100 != 0) or (self.value % 400 == 0)


@dataclass
class Mes:
    value: int
    description :str = "Mês da reunião"
    def __post_init__(self):
        if not (1 <= self.value <= 12):
            raise ValueError(f"Data inválida: o mês {self.value} não existe!")
                 
    @classmethod
    def set_month(cls, mes: int) -> 'Mes':
        """Cria uma instância de Mes.

        Args:
            mes (int): Número do mês (1 a 12).


        Returns:
            Mes: Objeto representando o mês.
        """
        return cls(int(mes))

    def get_days(self, ano: Ano) -> int:
        """Retorna a quantidade de dias do mês, alterando baseado no ano bissexto

        Args:
            ano (Ano): ano fornecido

        Returns:
            int: dias do mes
        """
        dias_por_mes: Dict[int, int] = {
            1: 31, 2: 29 if ano.is_bissexto() else 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        return dias_por_mes[self.value]

@dataclass
class Dia():
    value: int
    description:str = "Dia da reunião"
    
    def __post_init__(self):
        if self.value < 1:
            raise ValueError(f"Data invalida: Dia não pode ser menor que 1")
    
    @classmethod         
    def set_day(cls, dia: int):
        return cls(int(dia))
    
@dataclass
class Date:
    dia: Dia
    mes: Mes
    ano: Ano
    description : str = "Horário que a reunião ocorreu"


    def __post_init__(self):
        """Verifica se a data é válida ao inicializar a instância."""
        
        if self.dia.value > self.mes.get_days(self.ano):
            raise ValueError(f"Data inválida: o dia {self.dia} não existe em {self.mes.value}/{self.ano.value}!") 

    @classmethod
    def date(cls, dia: int, mes: int, ano: int) -> 'Date':
        """Retorna uma instância da classe Date, usando os parâmetros fornecidos.

        Args:
            dia (int): Dia da data representada.
            mes (int): Mês da data representada.
            ano (int): Ano da data representada.

        Returns:
            Date: Instância da classe Date, que representa uma data válida.
        """
        ano_instance = Ano.set_year(ano)
        mes_instance = Mes.set_month(mes)
        dia_instance = Dia.set_day(dia)
        return cls(dia_instance, mes_instance, ano_instance)
    
    @classmethod
    def from_string(cls, string: str) -> 'Date':
        """Retorna instância da classe Date a partir de uma string no formato 'dd/mm/aaaa'.

        Args:
            string (str): String no formato 'dd/mm/aaaa'.

        Returns:
            Date: Instância da classe Date.
        """
        dia, mes, ano = map(int, string.split('/'))
        return cls.from_values(dia, mes, ano)
    
    def get(self) -> Tuple[int, int, int]:
        """Retorna uma tupla contendo o dia, mês e ano da data.
        
        Returns:
            Tuple[int, int, int]: Tupla com (dia, mes, ano) da data.
        """
        return self.dia.value, self.mes.value, self.ano.value

    def __str__(self) -> str:
        """Retorna a data no formato 'dd/mm/aaaa'.
        
        Returns:
            str: Data formatada como string.
        """
        return f"{self.dia.value:02}/{self.mes.value:02}/{self.ano.value}"

if __name__ == "__main__":
    pass