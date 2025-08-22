from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def main():
    print("Hello from langchain-course-1!")
    information = """
    Alexis Alejandro Sánchez Sánchez (Tocopilla, 19 de diciembre de 1988) es un futbolista chileno que juega como delantero en el Udinese Calcio de la Serie A de Italia.

Es ampliamente citado como uno de los mejores jugadores de su generación y, en ocasiones, como el más grande jugador chileno de todos los tiempos. 
En la temporada 2010-11 llegó al punto más alto de su carrera en Italia, jugando para Udinese, conquistó 12 goles en 31 partidos y se convirtió así en el segundo goleador del equipo, detrás de la leyenda del club, Antonio Di Natale Luego de participar en la Copa América 2011, recibió distintas ofertas de clubes como el Manchester United, S.S.C Napoli, Inter de Milán, Manchester City, Juventus, F. C. Barcelona, Real Madrid, y Chelsea FC. Sin embargo, finalmente el club culé lo fichó por 26 millones de euros (aproximadamente US$43 millones) más 13 millones en variables. En su paso en F. C. Barcelona, conquistó 1 Liga, 1 Copa del Rey, 2 Supercopas de España, además sus 2 primeros títulos internacionales, la Supercopa de Europa 2011 y la Copa Mundial de Clubes de 2011. Una de sus mejores actuaciones se produjo en un partido contra el Real Madrid en 2013, Sánchez entró desde el banco y anotó un gol de vaselina en la victoria de su equipo en el Clásico. Esta fue quizás su postal más importante con el cuadro catalán y uno de los goles más importantes en su carrera. Desde ese momento el tocopillano cambió las críticas por elogios a punta de goles, los cuales lo situarían como el segundo máximo anotador del equipo después de Lionel Messi al final del torneo. 
"""
    summary_template = """
        Dada la siguiente informacion: {information} sobre una persona, quiero que crees:
        1. Un resumen corto
        2. Dos datos interesantes sobre la persona
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatGoogleGenerativeAI(temperature=0,model="gemini-2.5-flash")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
