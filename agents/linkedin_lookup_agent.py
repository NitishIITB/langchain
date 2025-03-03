import os

from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tools.tools import get_profile_url_tavily


from tools.tools import get_profile_url_tavily



import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.6)
api_key = os.getenv("OPEN_API_KEY")
def lookup(name : str) ->str:
    llm = ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo", openai_api_key=api_key)
    #llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.6)
    template = """
    given the full name{name_of_person} I want you to get it me a link to their Linkedin profile
    page. your ans should only a url
    """

    prompt = PromptTemplate(template = template, input_variables= ["name_of_person"])

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt.format_prompt(name_of_person=name)}
    )

    linked_profile_url = result["output"]
    return linked_profile_url

if __name__ == "__main__":
    url = lookup(name = "NITISH Kumar IIT Bombay Thapar")
    print(url)