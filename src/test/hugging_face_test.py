from huggingface_hub import InferenceClient
from src.env import HF_TOKEN

def main():
    client = InferenceClient(api_key=HF_TOKEN)

    messages = [
        { "role": "system", "content": "Привет, как дела\n" },
        { "role": "user", "content": "Расскажи о себе" },
    ]

    completion = client.chat.completions.create(
        model="Qwen/QwQ-32B-Preview",
        messages=messages,
        temperature=0.5,
        max_tokens=2048,
        top_p=0.7
    )

    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()