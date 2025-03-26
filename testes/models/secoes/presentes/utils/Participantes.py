from Componentes import Individuo
# Um participante possui dois valores, nome e cargo

class Participante(Individuo):
    description: str = "Participante presente na reunião"

class Convidados(Individuo):
    description: str = "Convidado para a reunião"

class Ausentes(Individuo):
    description: str = "Participante ausente na reunião"