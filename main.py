from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

load_dotenv()

# Inicializa las herramientas que el agente puede usar
tools = [TavilySearch()]

# Crea el modelo de lenguaje de Google Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Obtiene el prompt reactivo desde el hub de LangChain
react_prompt = hub.pull("hwchase17/react")

# Crea el analizador de salida
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)

# Crea el prompt reactivo con instrucciones de formato
react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS, 
    input_variables=[
        "input",
        "agent_scratchpad",
        "tool_names"
    ],
).partial(
    format_instructions=output_parser.get_format_instructions(),
)

# Crea el agente React con el modelo, tools y prompt
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt_with_format_instructions    
)

# Ejecuta el agente con las tools y activa el modo detallado
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

# Extrae la salida del agente
extract_output = RunnableLambda(lambda x: x["output"])

# Parsea la salida del agente 
parse_output = RunnableLambda(lambda x: output_parser.parse(x))

# Crea la cadena a partir del agente, extrayendo y parseando la salida
chain = agent_executor | extract_output | parse_output


def main():
    # Ejecuta la cadena, con el input especificado
    result = chain.invoke(
        input={
            "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
        }
    )

    # Imprime el resultado
    print(result)


if __name__ == "__main__":
    main()
