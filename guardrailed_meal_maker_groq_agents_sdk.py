from agents import Agent, Runner, input_guardrail, GuardrailFunctionOutput
from pydantic import BaseModel

from meal_maker_groq_and_agents_sdk import model, tools, recipe_sprucer_instructions, hungry_user_demand


class IsHalalOutput(BaseModel):
    is_halal: bool
    haram_phrase: str


haram_meal_demand_detector_agent = Agent(name="Muslim ingredients checker",
                                         instructions="check if the user is demanding a meal that is considered haram by muslims",
                                         output_type=IsHalalOutput,
                                         model=model)


@input_guardrail
async def guardrail_against_haram_meals(context, agent, input):
    result = await Runner.run(haram_meal_demand_detector_agent, input, context=context)  # have to run it async
    # since Runner.run_sync can only be called once (and I want that in the end)
    is_haram_meal = not result.final_output.is_halal
    return GuardrailFunctionOutput(output_info={"meal_info": result.final_output}, tripwire_triggered=is_haram_meal)

muslim_recipe_sprucer_agent = Agent(name="Muslim Recipe Sprucer",
                                    instructions=recipe_sprucer_instructions,
                                    tools=tools,
                                    model=model,
                                    input_guardrails=[guardrail_against_haram_meals])
if __name__ == "__main__":
    Runner.run_sync(muslim_recipe_sprucer_agent, hungry_user_demand)
