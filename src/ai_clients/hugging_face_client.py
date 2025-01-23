from huggingface_hub import InferenceClient
from src.env import HF_TOKEN

class HuggingFaceClient:

    def get_product_ai_description(self, api_key, model, role, product_info) -> str:

        client = InferenceClient(api_key=HF_TOKEN)
        messages = [
            {"role": "system", "content": role},
            {"role": "user", "content": "Исходный текст: " + product_info},
        ]

        try:
            completion = client.chat.completions.create(
                model="Qwen/Qwen2.5-72B-Instruct",
                messages=messages,
                temperature=0.5,
                max_tokens=1024,
                top_p=0.3
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise e


gpt_client = HuggingFaceClient()

if __name__ == "__main__":
    # Пример использования клиента
    API_KEY = "sk-TOKEN"  # Замените на ваш API-ключ OpenAI

    # Инициализация клиента
    client = HuggingFaceClient()
    response = client.get_product_ai_description(API_KEY, "gpt-4o", "You are a helpful assistant.", "What is the capital of France?")
    print(f"Ответ HuggingFace: {response}")
