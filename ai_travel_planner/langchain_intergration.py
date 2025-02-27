from google_genai_integration import fetch_travel_data
from langchain.llms import OpenAI  
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain 

# Initialize the model and prompt template
llm = OpenAI(temperature=0.7)
prompt = PromptTemplate(input_variables=["source", "destination"], template="Find travel options from {source} to {destination}. Please include estimated costs and times for cab, train, bus, and flights.")

# Function to get recommendations
def get_travel_recommendations(source, destination):
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run({"source": source, "destination": destination})
    travel_data = fetch_travel_data(source, destination)
    
    # Combine LangChain result with fetched travel data
    result += "\n\nAdditional Travel Information:\n"
    result += travel_data
    return result
