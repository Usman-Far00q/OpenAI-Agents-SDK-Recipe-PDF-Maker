from agents import Agent, Runner, set_tracing_disabled, ModelSettings, OpenAIChatCompletionsModel, AsyncOpenAI
import os

from dotenv import load_dotenv

from markdown_to_html_render import render_markdown_to_html_file

load_dotenv(override=True)
api_key = os.getenv("GROQ_API_KEY")

# --------------------
# Setting the Tracing for the Agent to be disabled since it requires a valid OpenAi key
set_tracing_disabled(True)
# -------------


model = OpenAIChatCompletionsModel(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    openai_client=AsyncOpenAI(base_url="https://api.groq.com/openai/v1/", api_key=api_key)
)

instructions_for_recipe_agent = """You are a talented chef that knows how to make any dish 
no matter how exotic or simple it might be, given a demand from someone that is hungry, you 
will come up with interesting recipes that they can follow and make a meal that meets their demands and
is delicious as well. Have you response be in pure markdown (your output should be nothing but pure markdown).
The repose should essentially be a recipe that a novice cook could even understand and follow to created their desired meal."""


recipe_into_markdown_agent = Agent(name="Professional Recipe teller",
                     instructions=instructions_for_recipe_agent,
                     model=model,
                     model_settings=ModelSettings(temperature=0.1))

# TODO: Usman Explain this
recipe_agent_as_a_tool = recipe_into_markdown_agent.as_tool(tool_name="recipe into Markdown agent", tool_description="given a users demand generate a recipe for it in pure Markdown")


recipe_sprucer_instructions ="""Your are a person that has a good sense of style. You use the tools given to:
1- get the cooking Recipe that is in Markdown.
 to HTML that get shown on the browser.
 
2- once the you get the recipe Markdown you have to go through the Markdown and make sure to inject 
 valid emojis inside the Markdown. Make sure the emojis are valid and incase you can't figure out a 
 valid emoji do not insert anything that is NOT an emoji. You edit the Markdown ONLY once.
 
3- ONLY When you are happy with the looks of the final Markdown,you use another tool to show the Markdown in HTML form in the browser

Lastly make SURE to ALWAYS ALWAYS FOLLOW THE FOLLOWING:
Do not call the tool=render_markdown_to_html_file MORE than once not matter what.
Do not call the tool=recipe into Markdown agent.
Assume that each tool works as expected on the first attempt."""

tools = [recipe_agent_as_a_tool, render_markdown_to_html_file]

recipe_sprucer_agent = Agent(name="Recipe sprucer", instructions=recipe_sprucer_instructions, tools=tools, model=model)


hungry_user_demand = "I really like chocolate but I need to have a dish that has got rice in it as well"

Runner.run_sync(recipe_sprucer_agent, hungry_user_demand)
