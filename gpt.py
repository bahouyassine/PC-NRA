import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from keys import key
#add a keys.py file with a variable key with open ai api key
os.environ['OPENAI_API_KEY'] = key

class Configuration:
    def __init__(self):
        self.temperature = 0.9
        self.max_tokens = 256
        self.model_name = 'text-davinci-002'
        self.template = """Act as a Computer Hardware Expert,
                            and provide me with the complete specifications
                            of the PC titled {title} the output is a string containing the value of 
                            CPU_Model,GPU_Model,RAM_Capacity,Storage_Type,Storage_Cpacity
                            separated by , and -1 if the value is not existing
                         """

class OpenAIAgent:
    def __init__(self, config: Configuration):
        self.llm = OpenAI(model_name=config.model_name, 
                          temperature=config.temperature, 
                          max_tokens=config.max_tokens)
        self.prompt_template = PromptTemplate(
            input_variables=["title"],
            template=config.template,
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
class SpecExtractor:
    def __init__(self):
        self.config = Configuration()
        self.agent = OpenAIAgent(self.config)

    def extract_from_title(self, title: str):
        return self.agent.chain.run(title)


# extractor = SpecExtractor()
# result = extractor.extract_from_title("PC with Ryzen 5 7600X and RTX 4060Ti. It has 16 GB RAM and a 1TB SSD")
# print(result.split(','))