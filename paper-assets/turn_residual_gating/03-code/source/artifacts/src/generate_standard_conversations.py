import argparse
import json
import os
import sys

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import MODEL_NAME

SYSTEM_PROMPTS = [
    "You are a knowledgeable science tutor. Always explain concepts step by step. Use analogies when possible. Never give direct answers without explanation. If the student makes an error, gently correct them and guide them to the right answer.",
    "You are a professional code reviewer. Focus on code quality, security, and performance. Point out potential bugs and suggest improvements. Always explain why a change is needed, not just what to change. Be constructive and specific.",
    "You are a creative writing coach. Help users improve their storytelling skills. Focus on character development, plot structure, and vivid descriptions. Give specific feedback with examples. Encourage experimentation with different styles.",
    "You are a math problem solver. Show all steps clearly. Explain the reasoning behind each step. If there are multiple approaches, mention them. Check your work by verifying the answer. Use LaTeX notation for formulas.",
    "You are a debate coach who helps users argue both sides of issues. Present balanced perspectives. Challenge weak arguments constructively. Teach logical reasoning and evidence evaluation. Avoid personal opinions.",
]

CONVERSATIONS_DATA = [
    ["Why is the sky blue?", "What about sunsets being red?", "How does a rainbow form?",
     "Why do stars twinkle?", "What causes thunder?", "How do magnets work?",
     "Why is water wet?", "What is gravity?", "How do airplanes fly?", "Why is space dark?"],
    ["Review this: def add(a,b): return a+b", "What about error handling?", "How should I write tests for it?",
     "Is recursion better than iteration?", "When should I use async/await?", "How to handle memory leaks?",
     "Best practices for API design?", "How to optimize database queries?", "When to use microservices?", "How to handle rate limiting?"],
    ["Help me start a mystery story", "How do I create a compelling villain?", "What makes good dialogue?",
     "How to build suspense?", "Should I use first or third person?", "How to write a plot twist?",
     "Tips for describing settings?", "How to end a chapter with a cliffhanger?", "How to avoid cliches?", "How to write an epilogue?"],
    ["Solve: 3x + 7 = 22", "What is the derivative of x^3?", "Explain the Pythagorean theorem",
     "What is a prime number?", "How to calculate compound interest?", "What is the area of a circle?",
     "Explain matrix multiplication", "What is a logarithm?", "How to solve quadratic equations?", "What is calculus used for?"],
    ["Should AI be regulated?", "Is remote work better than office work?", "Should college be free?",
     "Is social media harmful?", "Should voting be mandatory?", "Is nuclear energy safe?",
     "Should animals have legal rights?", "Is space exploration worth the cost?", "Should there be a universal basic income?", "Is genetic engineering ethical?"],
]


def build_conversation(tokenizer, model, system_prompt, user_questions, device, max_new_tokens=100):
    messages = [{"role": "system", "content": system_prompt}]
    for q in user_questions:
        messages.append({"role": "user", "content": q})
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        input_ids = tokenizer(text, return_tensors="pt").input_ids.to(device)

        if input_ids.shape[1] > 1800:
            messages.pop()
            break

        with torch.no_grad():
            output = model.generate(input_ids, max_new_tokens=max_new_tokens, do_sample=False)

        new_tokens = output[0][input_ids.shape[1]:]
        response = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
        messages.append({"role": "assistant", "content": response})

    return messages


def main():
    parser = argparse.ArgumentParser(description="Generate standard conversations for fair GAR comparison")
    parser.add_argument("--model-name", default=MODEL_NAME)
    parser.add_argument("--output-path", default="/root/turn_residual_gating/data/standard_conversations.json")
    parser.add_argument("--max-new-tokens", type=int, default=100)
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    print(f"Model: {args.model_name}")

    print("Loading vanilla model (no LoRA, no gate)...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    model.eval()

    print(f"\nGenerating {len(SYSTEM_PROMPTS)} conversations...")
    conversations = []
    for i, (sys_prompt, user_qs) in enumerate(zip(SYSTEM_PROMPTS, CONVERSATIONS_DATA)):
        print(f"  Conversation {i+1}/{len(SYSTEM_PROMPTS)}: {sys_prompt[:50]}...")
        messages = build_conversation(tokenizer, model, sys_prompt, user_qs, device, args.max_new_tokens)
        num_turns = sum(1 for m in messages if m["role"] == "assistant")
        print(f"    {num_turns} assistant turns")
        conversations.append({
            "system_prompt": sys_prompt,
            "messages": messages,
            "num_turns": num_turns,
        })

    with open(args.output_path, "w") as f:
        json.dump(conversations, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(conversations)} conversations to {args.output_path}")
    for i, conv in enumerate(conversations):
        print(f"  Conv {i+1}: {conv['num_turns']} turns")


if __name__ == "__main__":
    main()
