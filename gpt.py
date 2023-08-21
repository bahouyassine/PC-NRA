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
                            of the PC titled {title} the out put must be a dictionarie having as keys
                            CPU_Model,GPU_Model,RAM_Capacity,Storage_Type,Storage_Cpacity and their values
                            from the title
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

    def get_spec(self, title):
        return eval(self.chain.run(title))

class SpecExtractor:
    def __init__(self):
        self.config = Configuration()
        self.agent = OpenAIAgent(self.config)

    def extract_from_title(self, title: str):
        return self.agent.get_spec(title)


