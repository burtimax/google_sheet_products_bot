from openai import OpenAI

class ChatGPTClient:

    def get_product_ai_description(self, api_key, model, role, product_info) -> str:

        client = OpenAI(api_key=api_key)
        messages = [
            {"role": "system", "content": role},
            {"role": "user", "content": product_info},
        ]

        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            raise e


gpt_client = ChatGPTClient()

if __name__ == "__main__":
    # Пример использования клиента
    API_KEY = "sk-TOKEN"  # Замените на ваш API-ключ OpenAI

    # Инициализация клиента
    client = ChatGPTClient()
    response = client.get_product_ai_description(API_KEY, "gpt-4o", "You are a helpful assistant.", "What is the capital of France?")
    print(f"Ответ ChatGPT: {response}")
