import openai
import ssl

# Disable SSL verification globally (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context



from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import os

from openai import api_key

information = """
Narendra Damodardas Modi[a] (born 17 September 1950)[b] is an Indian politician who has served as the prime minister of India since 2014. Modi was the chief minister of Gujarat from 2001 to 2014 and is the member of parliament (MP) for Varanasi. He is a member of the Bharatiya Janata Party (BJP) and of the Rashtriya Swayamsevak Sangh (RSS), a right-wing Hindu nationalist paramilitary volunteer organisation. He is the longest-serving prime minister outside the Indian National Congress.[4]
Modi was born and raised in Vadnagar in northeastern Gujarat, where he completed his secondary education. He was introduced to the RSS at the age of eight. At the age of 18, he was married to Jashodaben Modi, whom he abandoned soon after, only publicly acknowledging her four decades later when legally required to do so. Modi became a full-time worker for the RSS in Gujarat in 1971. The RSS assigned him to the BJP in 1985 and he rose through the party hierarchy, becoming general secretary in 1998.[c] In 2001, Modi was appointed chief minister of Gujarat and elected to the legislative assembly soon after. His administration is considered complicit in the 2002 Gujarat riots,[d] and has been criticised for its management of the crisis. According to official records, a little over 1,000 people were killed, three-quarters of whom were Muslim; independent sources estimated 2,000 deaths, mostly Muslim.[13] A Special Investigation Team appointed by the Supreme Court of India in 2012 found no evidence to initiate prosecution proceedings against him.[e] While his policies as chief minister were credited for encouraging economic growth, his administration was criticised for failing to significantly improve health, poverty and education indices in the state.[f]
In the 2014 Indian general election, Modi led the BJP to a parliamentary majority, the first for a party since 1984. His administration increased direct foreign investment, and reduced spending on healthcare, education, and social-welfare programmes. Modi began a high-profile sanitation campaign, and weakened or abolished environmental and labour laws. His demonetisation of banknotes in 2016 and introduction of the Goods and Services Tax in 2017 sparked controversy. Modi's administration launched the 2019 Balakot airstrike against an alleged terrorist training camp in Pakistan. The airstrike failed,[16][17] but the action had nationalist appeal.[18] Modi's party won the 2019 general election which followed.[19] In its second term, his administration revoked the special status of Jammu and Kashmir,[20][21] and introduced the Citizenship Amendment Act, prompting widespread protests, and spurring the 2020 Delhi riots in which Muslims were brutalised and killed by Hindu mobs.[22][23][24] Three controversial farm laws led to sit-ins by farmers across the country, eventually causing their formal repeal. Modi oversaw India's response to the COVID-19 pandemic, during which, according to the World Health Organization's estimates, 4.7 million Indians died.[25][26] In the 2024 general election, Modi's party lost its majority in the lower house of Parliament and formed a government leading the National Democratic Alliance coalition.[27][28]
Under Modi's tenure, India has experienced democratic backsliding, or the weakening of democratic institutions, individual rights, and freedom of expression.[29][30][g] As prime minister, he has received consistently high approval ratings.[36][37][38] Modi has been described as engineering a political realignment towards right-wing politics. He remains a controversial figure domestically and internationally, over his Hindu nationalist beliefs and handling of the Gujarat riots, which have been cited as evidence of a majoritarian and exclusionary social agenda.[h]
"""
if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")
    print(os.environ["OPEN_API_KEY"])
    api_key = os.getenv("OPEN_API_KEY")
    prompt_text  = f"""
    you are given information {information} to summaries. So summaries it and give
    1. two interesting facts about that person
    2. is this person goog for humanity?, give one line explanation
    """
    prompt = PromptTemplate(input_variables = ["information"], template = prompt_text)

    llm = ChatOpenAI(temperature= 0.6, model = "gpt-3.5-turbo", openai_api_key= api_key)
    llm = ChatOllama(model = 'llama3')
    llm = ChatOllama(model='mistral')
    chain = prompt | llm
    result  = chain.invoke({"information":information})
    print(result)
