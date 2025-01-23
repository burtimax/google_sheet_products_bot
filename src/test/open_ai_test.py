import openai
from openai import OpenAI

# Замените 'YOUR_API_KEY' на ваш реальный API-ключ GPT-4
API_KEY = "sk-TOKEN"

def generate_product_description(product_name, features):
    """Генерирует описание продукта на основе его названия и характеристик.

    Args:
        product_name (str): Название продукта.
        features (list): Список характеристик продукта.

    Returns:
        str: Сгенерированное описание.
    """

    prompt = f"Напиши краткое и привлекательное описание для продукта {product_name}. Удели особое внимание следующим характеристикам: {', '.join(features)}."

    client = OpenAI(api_key=API_KEY)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

    return response.choices[0].text.strip()

# Пример использования
product_name = "Беспроводные наушники"
features = ["активное шумоподавление", "высокое качество звука", "долгое время автономной работы"]

description = generate_product_description(product_name, features)
print(description)