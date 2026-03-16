import os
from anthropic import Anthropic
from utils.tools_structures_util import tools_structures


class IaService:

    def __init__(self):
        self.client = Anthropic()
        self.model = os.getenv("IAMODEL")

    def data_memo_generator(self, memo_data: str) -> dict:

        prompt_system = "You are a Senior Financial Analyst and a structured data extraction engine for institutional investment committees. Your objective is to analyze the raw information provided by the user (which may be in English or Spanish), precisely identify the nature of the business, and structure the data by invoking the most appropriate tool/function. ALL content you insert into the tool's JSON payload must be written in technical, professional, and precise SPANISH. "

        response = self.client.messages.create(
            model=self.model,
            max_tokens=16392,
            tools=tools_structures,
            tool_choice={"type": "any"},
            temperature=0.2,
            system=prompt_system,
            messages=[
                {
                    "role": "user",
                    "content": f"This is all the data obtained please note that it may be poorly structured or contain corrupted characters due to a faulty scan. DATA:\n\n{memo_data}",
                }
            ],
        )

        price_input = float(os.getenv("PRICE_PER_TOKEN_INPUT", "0"))
        price_output = float(os.getenv("PRICE_PER_TOKEN_OUTPUT", "0"))
        in_tokens = response.usage.input_tokens
        out_tokens = response.usage.output_tokens
        estimated_cost = (in_tokens * price_input) + (out_tokens * price_output)

        for block in response.content:
            if block.type == "tool_use":
                used_structure = block.name
                payload = block.input

                return {
                    "state": True,
                    "used_structure": used_structure,
                    "payload": payload,
                    "input_tokens": in_tokens,
                    "output_tokens": out_tokens,
                    "estimated_cost": estimated_cost,
                }


ia_service = IaService()
