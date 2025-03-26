from dataclasses import dataclass
from typing import Tuple

@dataclass
class Hora:
    value: int
    description : str = "Horas"

    def __post_init__(self):
        if not (0 <= self.value < 24):
            raise ValueError("Horas devem estar entre 0 e 23.")

    def __str__(self):
        return f"{self.value:02}h"

@dataclass
class Minuto:
    value: int
    description : str = "Minutos"

    def __post_init__(self):
        if not (0 <= self.value < 60):
            raise ValueError("Minutos devem estar entre 0 e 59.")

    def __str__(self):
        return f"{self.value:02}m"

@dataclass
class Time:
    horas: Hora
    minutos: Minuto
    description : str = "Horário que a reunião ocorreu"

    def __str__(self):
        return f"{self.horas.value:02}h{self.minutos.value:02}m"

    @classmethod
    def time(cls, horas: int, minutos: int) ->'Time':
        return cls(Hora(int(horas)), Minuto(int(minutos)))
    
    @classmethod
    def from_string(cls, time_str: str) ->'Time':
        """Cria um objeto Tempo a partir de uma string no formato '00h00m'."""
        try:
            horas, minutos = map(int, time_str.lower().replace("h", " ").replace("m", "").split())
            return cls(Hora(int(horas)), Minuto(int(minutos)))
        except ValueError:
            raise ValueError("Formato inválido. Use '00h00m'.")
        
    def get(self) -> Tuple[int, int]:
        """
Retorna o valor de horas e minutos no formato de uma tupla
com os valores na respectiva ordem

    Returns:
            Tuple[int, int]: Tupla com os valores de hora e minuto
        """
        return self.horas.value, self.minutos.value

    def add_minutes(self, minutes: int) -> "Time":
        """Adiciona minutos ao tempo e retorna um novo objeto Tempo."""
        total_minutes = self.horas.value * 60 + self.minutos.value + minutes
        total_minutes %= 24 * 60  # Garante que fique no intervalo de 0 a 23h59m
        return Time(Hora(total_minutes // 60), Minuto(total_minutes % 60))
