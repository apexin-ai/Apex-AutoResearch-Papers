"""Quick test: Claude API for 5-class ack classification (drop-in GPT-4o replacement).

Usage:
  ANTHROPIC_API_KEY=[REDACTED] python scripts/test_claude_oracle.py
"""
import json
import os

from anthropic import Anthropic

SYSTEM_PROMPT = """You are a communication analyst for multi-agent systems. Your task is to classify the function of a message in a multi-agent math problem-solving conversation.

## Function Types

1. **information_provision**: Provides facts, data, intermediate calculations, or partial results that advance the solution. Includes reporting computed values, stating known quantities, or presenting new numerical results.

2. **reasoning_guidance**: Provides reasoning direction, problem decomposition, step-by-step plans, or conceptual frameworks. Includes breaking the problem into sub-problems, suggesting solution strategies, or outlining multi-step approaches.

3. **verification**: Checks, corrects, or confirms the correctness of previous work. Includes identifying errors, validating results, pointing out mistakes, or confirming a step is correct with a specific reason.

4. **coordination**: Manages the flow of the conversation, assigns tasks, requests clarification, or controls turn-taking. Includes delegating sub-tasks, asking for more information, or directing the problem-solving process.

5. **acknowledgment**: Simple confirmation, repetition, or agreement that adds no new information or reasoning. Includes restating what was already said without extending it.

## Priority Rules (when a message fits multiple categories)

Priority: coordination > verification > reasoning_guidance > information_provision > acknowledgment

- If a message both provides new results AND checks previous work, classify as **verification**.
- If a message provides a reasoning plan AND new results, classify as **reasoning_guidance**.
- If a message confirms correctness WITH a substantive explanation of why, classify as **verification** (not acknowledgment).
- If a message simply agrees or restates without adding new information, classify as **acknowledgment**.

## Output Format

Respond with ONLY a JSON object (no markdown, no extra text):
{"type": "<function_type>", "confidence": <0.0-1.0>, "reasoning": "<brief explanation>"}
"""

MODEL = "claude-sonnet-4-20250514"


def classify_message(client: Anthropic, prev_text: str, msg_text: str,
                     sender: str, task_id: str) -> dict:
    user_prompt = f"""## Context

Task: {task_id}

### Previous message (for context):
{prev_text[:2000] if prev_text else '[conversation start]'}

### Current message to classify (sent by {sender}):
{msg_text[:3000]}

Classify the function of the current message."""

    resp = client.messages.create(
        model=MODEL,
        max_tokens=256,
        temperature=0,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )
    raw = resp.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
    result = json.loads(raw)
    print(f"Input tokens: {resp.usage.input_tokens}, Output tokens: {resp.usage.output_tokens}")
    return result


def main():
    client = Anthropic(api_key=[REDACTED]"ANTHROPIC_API_KEY"])

    with open("outputs/oracle_labels/llama_n300_traces.jsonl") as f:
        task = json.loads(f.readline())

    msgs = task["messages"]
    prev_text = msgs[0]["content"]
    msg = msgs[1]

    print(f"Task: {task['task_id']}")
    print(f"Sender: {msg['sender']}")
    print(f"Content preview: {msg['content'][:200]}...")
    print(f"\nClassifying with {MODEL}...")

    result = classify_message(client, prev_text, msg["content"],
                              msg["sender"], task["task_id"])
    print(f"\nResult: {json.dumps(result, indent=2)}")


if __name__ == "__main__":
    main()
