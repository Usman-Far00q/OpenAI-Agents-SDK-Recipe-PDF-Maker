from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, trace

from dotenv import load_dotenv

load_dotenv(override=True)

# Read doc --> https://medium.com/@danushidk507/openai-agents-sdk-with-ollama-fc85da11755d

# --------------------
# Setting the Tracing for the Agent to be disabled since it require a valid OpenAi key
run_config = RunConfig
run_config.tracing_disabled = True
# -------------


model = OpenAIChatCompletionsModel(
    model="llama3:8b",
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
)


agent = Agent(name="Joke Teller",
              instructions="You are a comedic joke teller with excellent humour, your responses are always hillarous and not repetitive ",
              model=model)


result1 = Runner.run_sync(agent, "Tell me a Knock Knock Joke", run_config=run_config)
result2 = Runner.run_sync(agent, "Tell me a political Joke", run_config=run_config)
print(result1.final_output,"\n\n\n\n\n" ,result2.final_output)