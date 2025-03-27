from .autor import Autor
from .date import Date
from .local import Local
from .modalidade import Modalidade
from .time import Time

# Define quais classes serão acessíveis ao fazer "from utils import *"
__all__ = ["Autor", "Date", "Local", "Modalidade", "Time"]
