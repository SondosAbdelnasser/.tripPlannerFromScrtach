# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def travel_program(self, agent, city , travel_dates, interests ):
        return Task(
            description=dedent(
                f"""
            *Task*: Develop a 7-Day Travel Program
            *Description*: Expand the city guide into a full 7-day travel  program with detailed 
                per-day plans, including weather forecasts, places to eat, packing suggestions, 
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay, 
                and actual restaurants to go to. This itinerary should cover all aspects of the trip, 
                from arrival to departure, integrating the city guide information with practical travel logistics.


            
             *Parameters*: 
            - City: {city}
            - Trip Date: {travel_dates}
            - Traveler Interests: {interests}

            *Note*: {self.__tip_section()}
        """

            ),
             
            agent=agent,
        )

    def identify_city(self, agent,origin,cities,interests,travel_dates ):
        return Task(
            description=dedent(
                f"""
            Task : Identify the best City for the trip 
            description: analyze and select the best city for the trip based on 
                  specific criteria like  weather patterns ,seasnol events and 
                  festivals , travel costs .
                 this task involves comparing multiple cities ,considering factors like current 
                 weather conditions, upcoming cultural or seasonal events , and 
                 overall travel expenses.
                  YOUR FINAL answer MUST be a detailed report on the chosen city ,
                 including actual flight costs and weather forcasting and attractions.
            
            Parameters 
            -Origin:{origin}
            -Cities:{cities}
            -Interests:{interests}
            -Travel_Dates:{travel_dates}

            **Note**{self.__tip_section()}

           
        """
            ),
            
            agent=agent,
        )
    def gather_city_info (self, agent,city,interests,travel_dates ):
        return Task(
            description=dedent(
                f"""
            **Task**: Gather In-depth City Guide Information
            **Description **: Complie In-depth the selected City , gathering information about 
                key attractions , local customs ,special events , and  daily activity recommendations. 
                This guide should provide a through overview of what the city has to offer , including 
                hidden gems , cultural hotspots , multi-visit landmarks , weather forcasting , and high-level cost .
            Parameters 
            -City:{city}
            -Interests:{interests}
            -Travel_Dates:{travel_dates}

            **Note**{self.__tip_section()}

           
        """
            ),
            
            agent=agent,
        )