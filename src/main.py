from transformers import AutoTokenizer, pipeline
import torch

model = "PY007/TinyLlama-1.1B-Chat-v0.2"
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline_ = pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

def ask(prompt: str):
    formatted_prompt = (
        f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
    )

    sequences = pipeline_(
        formatted_prompt,
        do_sample=True,
        top_k=50,
        top_p = 0.9,
        num_return_sequences=1,
        repetition_penalty=1.1,
        max_new_tokens=100,
        max_length=100
    )

    for seq in sequences:
        print(f"Result: {seq['generated_text']}")

while (True):
    ask(input("Prompt: "))
