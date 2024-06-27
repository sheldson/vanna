import openai
from openai import OpenAI
class LingyiWanwu:
    def __init__(self, config=None):
        if config is None:
            raise ValueError("For LingyiWanwu, config must be provided with an api_key and model")

        if "api_key" not in config:
            raise ValueError("config must contain an api_key")

        if "model" not in config:
            raise ValueError("config must contain a model")

        self.api_key = config["api_key"]
        self.model = config["model"]
        self.client = OpenAI(api_key=self.api_key, base_url="https://api.lingyiwanwu.com/v1")

    def system_message(self, message: str) -> any:
        return {"role": "system", "content": message}

    def user_message(self, message: str) -> any:
        return {"role": "user", "content": message}

    def assistant_message(self, message: str) -> any:
        return {"role": "assistant", "content": message}

    def generate_sql(self, question: str, **kwargs) -> str:
        # Use the super generate_sql if needed
        sql = super().generate_sql(question, **kwargs) if hasattr(super(), 'generate_sql') else question
        # Replace "\_" with "_"
        sql = sql.replace("\\_", "_")
        return sql

    def submit_prompt(self, prompt, **kwargs) -> str:
        chat_response = self.client.chat.completions.create(
            model=self.model,
            messages=prompt,
    )
        return chat_response.choices[0].message.content