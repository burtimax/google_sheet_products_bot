from openai import OpenAI
from src.env import OPEN_AI_TOKEN, OPEN_AI_MODEL

class ChatGPTClient:

    def get_product_ai_description(self, role, product_info) -> (bool, str):

        client = OpenAI(api_key=OPEN_AI_TOKEN)
        messages = [
            {"role": "system", "content": role},
            {"role": "user", "content": product_info},
        ]

        try:
            response = client.chat.completions.create(
                model=OPEN_AI_MODEL,
                messages=messages,
            )

            first_choice = response.choices[0]
            message_content = first_choice.message.content

            return (True, message_content)
        except Exception as e:
            return (False, str(e))


gpt_client = ChatGPTClient()

if __name__ == "__main__":
    # Пример использования клиента
    API_KEY = "sk-TOKEN"  # Замените на ваш API-ключ OpenAI

    # Инициализация клиента
    client = ChatGPTClient()
    response = client.get_product_ai_description(API_KEY, "gpt-4o", "You are a helpful assistant.", "What is the capital of France?")
    print(f"Ответ ChatGPT: {response}")
