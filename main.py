from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()

# Inicializa las herramientas que el agente puede usar
tools = [TavilySearch()]

# Crea el modelo de lenguaje de Google Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Obtiene el prompt reactivo desde el hub de LangChain
react_prompt = hub.pull("hwchase17/react")

# Crea el agente React con el modelo, tools y prompt
agent = create_react_agent(
            llm=llm,
            tools=tools,
            prompt=react_prompt
        )

# Ejecuta el agente con las tools y activa el modo detallado
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# Crea la cadena a partir del agente
chain = agent_executor

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
