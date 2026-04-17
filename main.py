from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create prompt template
prompt = PromptTemplate(
    input_variables=["animal"],
    template="Suggest 3 cool and unique names for a pet {animal}. Keep them short."
)

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

# Take user input
animal = input("Enter your pet type: ")

# Format prompt
final_prompt = prompt.format(animal=animal)

# Call LLM
response = llm.invoke(final_prompt)

# Output
print("\nSuggested Names:\n")
print(response.content)