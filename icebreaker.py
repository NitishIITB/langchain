from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# from openai import api_key
from third_parties.linkedin import scrape_linkedin_profile
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_API_KEY"] = ""  # Ensure LangSmith is disabled

linkedin_data = scrape_linkedin_profile(
    url = "https://www.linkedin.com/in/eden-marco/" ,mode = True
) # make it mode = True to save api_key credit
print(linkedin_data)
if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")
    #os.environ["OPEN_API_KEY"]
    #api_key = os.getenv("OPEN_API_KEY")
    prompt_text = """
    you are given linkedin information : {information} to summaries. So summaries it and give
    1. two interesting facts about that person
    2. is this person goog for humanity? give ans in yes or no and , give one line explanation
    """
    prompt = PromptTemplate(input_variables=["information"], template=prompt_text)

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.6)
    #llm = ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo", openai_api_key=api_key)
    #llm = ChatOllama(model="llama3")
    #llm = ChatOllama(model="mistral")
    chain = prompt | llm | StrOutputParser()

    result = chain.invoke({"information": linkedin_data})
    print(result)
