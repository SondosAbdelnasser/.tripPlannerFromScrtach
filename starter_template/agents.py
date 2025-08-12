from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI



class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role=" expert travel agent ",
            backstory=dedent(f"""Expert in travel professional with in-depth knowledge of global destinations, 
                             travel logistics, and customer service."""),
            goal=dedent(f"""create a 7 day travel  with detailed per day ,
                        contains budget, packing recommendation , tips """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def city_expert(self):
        return Agent(
            role="City selection Expert ",
            backstory=dedent(f"""expert at  decision-making function based on 
                             travel data to
                         choose a prefect  destination city for travel """),
            goal=dedent(f""" city selected based on weater ,budget , season ,Events and festivals ,
                        Accommodation availability, Safety  """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,   
        )
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide ",
            backstory=dedent(f"""knowledgeble local guide with
                              extensive inforamtion about the city , its attraction and customs """),
            goal=dedent(f"""provide the best insights about the selected city """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )