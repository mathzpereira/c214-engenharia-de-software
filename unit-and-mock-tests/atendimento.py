from pydantic import BaseModel, field_validator, model_validator
from typing import Literal


class Atendimento(BaseModel):
    """Horário de atendimento."""

    nome_professor: str
    horario: str
    periodo: Literal["integral", "noturno"]
    sala: int
    predio: str = None

    @field_validator("predio")
    def validar_predio(cls, value):
        if value not in ["1", "2", "3", "4", "6"]:
            raise ValueError("O prédio deve ser '1', '2', '3', '4' ou '6'")
        return value

    def get_predio(self) -> str:
        """Retorna o prédio baseado na sala."""
        if 1 <= self.sala <= 5:
            return "1"
        elif 6 <= self.sala <= 10:
            return "2"
        elif 11 <= self.sala <= 15:
            return "3"
        elif 16 <= self.sala <= 20:
            return "4"
        elif 21 <= self.sala <= 25:
            return "6"
        else:
            raise ValueError("Prédio não encontrado")

    @model_validator(mode="after")
    def preencher_predio(self) -> "Atendimento":
        if self.predio is None:
            self.predio = self.get_predio()
        return self
