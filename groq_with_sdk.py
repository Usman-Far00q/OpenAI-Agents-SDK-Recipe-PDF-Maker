from agents import Agent, Runner, set_tracing_disabled, ModelSettings, OpenAIChatCompletionsModel, AsyncOpenAI
import os

from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("GROQ_API_KEY")

# --------------------
# Setting the Tracing for the Agent to be disabled since it require a valid OpenAi key
set_tracing_disabled(True)
# -------------


model = OpenAIChatCompletionsModel(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    openai_client=AsyncOpenAI(base_url="https://api.groq.com/openai/v1/", api_key=api_key)
)


agent = Agent(name="Joke Teller",
              instructions="You are a comedic joke teller with excellent humour, your responses are always hillarous and not repetitive ",
              model=model,
              model_settings=ModelSettings(temperature=0.1))

result1 = Runner.run_sync(agent, "tell me a good american joke")
print(result1.final_output) 