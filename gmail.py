# https://python.langchain.com/en/latest/modules/agents/toolkits/examples/gmail.html

# Step 1: Create a json file and download the same in the working folder: https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application

# Step 2: pip install google-api-python-client, google-auth-oauthlib, google-auth-httplib2, beautifulsoup4, langchain

# Step 3: Add Users for testing this app In Authconsent Screen
# Issues resolved: https://stackoverflow.com/questions/65184355/error-403-access-denied-from-google-authentication-web-api-despite-google-acc

# Step 4: Enable it by visiting https://console.developers.google.com/apis/api/gmail.googleapis.com/overview?project=26982114008



from langchain_community.agent_toolkits.gmail.toolkit import GmailToolkit


toolkit = GmailToolkit() 

# tools = toolkit.get_tools()
# print(tools)

import os
os.environ['GOOGLE_API_KEY'] = ''

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType

llm = ChatGoogleGenerativeAI(temperature=0, model="models/gemini-1.5-flash")


agent = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)


# agent.run("Create a gmail draft for me to editor of a letter from the perspective of a sentient parrot"
#           " who is looking to collaborate on some research with her"
#           " estranged friend, a cat. Under no circumstances may you send the message, however.")

agent.run("Check my inbox for the latest email from Ansh Singhal and summarize it for me format it to update in excel. and then reply to it with a thank you note.")

# print(agent.run("Could you search in my drafts for the latest email?"))
print(agent.run("Could you search in my mails for the latest email?"))





