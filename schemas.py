from typing import List

from pydantic import BaseModel, Field

"""
Este código define dos esquemas de datos usando Pydantic, una biblioteca de validación y manejo de datos en Python. 
Los esquemas se usan para estructurar y validar la información que maneja un agente (por ejemplo, un chatbot o sistema 
de preguntas y respuestas).

Source: Es una clase que representa una fuente de información. Solo tiene un campo:

url: una cadena que indica la URL de la fuente.
AgentResponse: Es una clase que representa la respuesta del agente. Tiene dos campos:

answer: una cadena con la respuesta generada por el agente.
sources: una lista de objetos Source, que indica las fuentes utilizadas para generar la respuesta. 
Por defecto, la lista está vacía.
Ambas clases heredan de BaseModel de Pydantic, lo que permite validar los datos y generar documentación automáticamente. 
Además, se usan descripciones para cada campo, lo que ayuda a entender su propósito.
"""


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="The answer provided by the agent")
    sources: List[Source] = Field(
        default_factory=list, description="List of sources used to generate the answer"
    )
