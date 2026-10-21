"""LLM-based correctness annotation of mathematical reasoning in inter-agent messages.

Input: traces JSONL (with ground_truth)
Output: JSONL with per-message correctness judgment.
"""

import argparse
import json
import logging
import os

import yaml
from openai import OpenAI

from utils import model_supports_system_role, convert_system_to_user

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

CORRECTNESS_SYSTEM_PROMPT = """You are a mathematical correctness judge. Given a message from a multi-agent math conversation and the ground truth answer, evaluate the mathematical correctness of the message.

## Categories

- **correct**: All mathematical reasoning and calculations in the message are correct.
- **partially_correct**: Some steps are correct but there are errors in other steps.
- **incorrect**: Key conclusions or calculations are wrong.
- **not_applicable**: The message does not contain mathematical reasoning (e.g., pure coordination).

## Output Format

Respond with ONLY a JSON object (no markdown, no extra text):
{"correctness": "<category>", "confidence": <0.0-1.0>, "reasoning": "<brief explanation>"}
"""


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def build_correctness_prompt(messages: list[dict], target_idx: int, ground_truth: str) -> str:
    lines = ["## Conversation Context\n"]
    for i, msg in enumerate(messages):
        marker = " <<< EVALUATE THIS MESSAGE >>>" if i == target_idx else ""
        lines.append(f"[Message {i}] {msg['sender']}:{marker}")
        lines.append(msg["content"])
        lines.append("")
    lines.append(f"Ground truth answer: {ground_truth}")
    lines.append(f"\nEvaluate the mathematical correctness of Message {target_idx}.")
    return "\n".join(lines)


def annotate_correctness(
    client: OpenAI, model: str, messages: list[dict], target_idx: int,
    ground_truth: str, max_tokens: int,
) -> dict:
    user_prompt = build_correctness_prompt(messages, target_idx, ground_truth)
    api_messages = [
        {"role": "system", "content": CORRECTNESS_SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]
    if not model_supports_system_role(model):
        api_messages = convert_system_to_user(api_messages)
    resp = client.chat.completions.create(
        model=model,
        messages=api_messages,
        temperature=0,
        top_p=1.0,
        max_tokens=max_tokens,
    )
    raw = resp.choices[0].message.content or "{}"
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        logger.warning("Failed to parse correctness annotation: %s", raw[:200])
        return {"correctness": "unknown", "confidence": 0.0, "reasoning": f"Parse error: {raw[:100]}"}


def main():
    parser = argparse.ArgumentParser(description="Correctness annotation of inter-agent messages")
    parser.add_argument("--config", type=str, default="configs/mvp.yaml")
    parser.add_argument("--traces", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    traces_path = args.traces or os.path.join(cfg["output"]["trace_dir"], "traces.jsonl")
    output_path = args.output or os.path.join(cfg["output"]["correctness_dir"], "correctness.jsonl")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    client = OpenAI(base_url=cfg["model"]["api_base"], api_key=[REDACTED]"model"]["api_key"])
    model = cfg["model"]["name"]
    max_tokens = cfg.get("correctness", {}).get("max_tokens", 512)

    done_keys: set[tuple[str, int]] = set()
    if os.path.exists(output_path):
        with open(output_path) as f:
            for existing_line in f:
                existing_line = existing_line.strip()
                if not existing_line:
                    continue
                try:
                    rec = json.loads(existing_line)
                    done_keys.add((rec["task_id"], rec["message_index"]))
                except (json.JSONDecodeError, KeyError):
                    continue
        logger.info("Resuming: %d records already done", len(done_keys))

    with open(traces_path) as fin, open(output_path, "a") as fout:
        for line_num, line in enumerate(fin, 1):
            line = line.strip()
            if not line:
                continue
            try:
                task = json.loads(line)
            except json.JSONDecodeError:
                logger.warning("Skipping malformed JSON at line %d", line_num)
                continue
            task_id = task["task_id"]
            messages = [m for m in task["messages"] if m.get("round", 0) > 0]
            ground_truth = task["ground_truth"]

            for msg_idx in range(len(messages)):
                if (task_id, msg_idx) in done_keys:
                    continue
                logger.info("Task %s msg %d: correctness annotation", task_id, msg_idx)
                result = annotate_correctness(client, model, messages, msg_idx, ground_truth, max_tokens)

                record = {
                    "task_id": task_id,
                    "message_index": msg_idx,
                    "sender": messages[msg_idx]["sender"],
                    "correctness": result.get("correctness", "unknown"),
                    "confidence": result.get("confidence", 0.0),
                    "reasoning": result.get("reasoning", ""),
                    "ground_truth": ground_truth,
                }
                fout.write(json.dumps(record, ensure_ascii=False) + "\n")
                fout.flush()

    logger.info("Correctness annotations saved to %s", output_path)


if __name__ == "__main__":
    main()
