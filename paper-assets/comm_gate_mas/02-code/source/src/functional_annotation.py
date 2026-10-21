"""LLM-based functional annotation of inter-agent messages.

Input: traces JSONL
Output: JSONL with per-message function type annotation.
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

_DOMAIN_CONFIGS = {
    "math": {
        "task_description": "multi-agent math problem-solving conversation",
        "examples": {
            "information_provision": [
                '"The cost per item is $24 / 6 = $4, and the total for 3 items is $12."',
                '"From the problem, we know the rate is 15 miles per hour and the time is 4 hours."',
            ],
            "reasoning_guidance": [
                '"Let\'s approach this by first finding the rate per hour, then multiplying by total hours."',
                '"We need to solve this in three parts: (1) find the cost per item, (2) calculate the total, (3) apply the discount."',
            ],
            "verification": [
                '"The multiplication in step 2 is wrong: 15 × 4 = 60, not 45."',
                '"I verified step 3: 60 × 0.9 = 54, which is correct because the 10% discount applies after tax."',
            ],
            "coordination": [
                '"Please verify my calculation for step 3 while I work on step 4."',
                '"Could you clarify whether the discount applies before or after tax?"',
            ],
            "acknowledgment": [
                '"Yes, I agree that 2 + 2 = 4."',
                '"That\'s correct, the answer is 42."',
            ],
        },
    },
    "science": {
        "task_description": "multi-agent science question-answering conversation",
        "examples": {
            "information_provision": [
                '"The boiling point of water at sea level is 100°C, and at higher altitudes it decreases due to lower atmospheric pressure."',
                '"Looking at the options, photosynthesis converts CO2 and water into glucose and oxygen using sunlight."',
            ],
            "reasoning_guidance": [
                '"Let\'s analyze each option: (A) relates to thermal expansion, (B) to phase changes, (C) to chemical bonding. We need to identify which principle applies here."',
                '"We should first identify the scientific domain — this is about Newton\'s third law — then evaluate each option against that principle."',
            ],
            "verification": [
                '"Option B is incorrect because convection requires a fluid medium, and this scenario is in a vacuum."',
                '"Your reasoning about momentum conservation is correct. Let me verify: initial momentum = final momentum, so the answer checks out."',
            ],
            "coordination": [
                '"Please check whether option C could also apply if we consider edge cases."',
                '"Could you clarify which physical law you\'re applying in step 2?"',
            ],
            "acknowledgment": [
                '"Yes, I agree that the answer is (B)."',
                '"That\'s correct, option A is the right choice."',
            ],
        },
    },
    "strategyqa": {
        "task_description": "multi-agent commonsense yes/no reasoning conversation",
        "examples": {
            "information_provision": [
                '"The population of Tokyo is approximately 14 million, making it one of the most populous cities in the world."',
                '"The speed of light is about 300,000 km/s, and the distance from Earth to the Sun is about 150 million km."',
            ],
            "reasoning_guidance": [
                '"Let\'s break this into sub-questions: (1) What is X? (2) Does X have property Y? (3) Does that imply the answer is yes or no?"',
                '"We need to reason by analogy: first establish the general principle, then apply it to this specific case."',
            ],
            "verification": [
                '"Your claim that penguins can fly is incorrect — they are flightless birds. This changes the answer to no."',
                '"I verified your reasoning: dolphins are indeed mammals, not fish, so your conclusion is correct."',
            ],
            "coordination": [
                '"Could you check whether the premise about average lifespan is accurate?"',
                '"Please verify the geographical claim before we finalize the answer."',
            ],
            "acknowledgment": [
                '"Yes, I agree the answer is no."',
                '"That\'s correct, the answer is yes."',
            ],
        },
    },
    "code": {
        "task_description": "multi-agent code generation conversation",
        "examples": {
            "information_provision": [
                '"The function signature requires two parameters: a list of integers and a target sum. The return type should be a list of index pairs."',
                '"Looking at the test cases, the input list can contain negative numbers and duplicates."',
            ],
            "reasoning_guidance": [
                '"Let\'s use a hash map approach: (1) iterate through the list, (2) for each element check if target-element exists in the map, (3) return indices if found."',
                '"We should handle edge cases first — empty list, single element, no valid pair — then implement the main logic."',
            ],
            "verification": [
                '"Your solution fails on the test case [3, 3] with target 6 — it returns the same index twice. You need to check i != j."',
                '"I ran the code against all test cases and it passes. The time complexity is O(n) which meets the constraint."',
            ],
            "coordination": [
                '"Please review my implementation while I write the edge case tests."',
                '"Could you clarify whether the function should return all pairs or just the first one found?"',
            ],
            "acknowledgment": [
                '"Yes, the hash map approach looks correct."',
                '"That\'s right, we should return a list of tuples."',
            ],
        },
    },
}


def build_annotation_system_prompt(task_domain: str = "math") -> str:
    cfg = _DOMAIN_CONFIGS.get(task_domain, _DOMAIN_CONFIGS["math"])
    examples = cfg["examples"]

    return f"""You are a communication analyst for multi-agent systems. Your task is to classify the function of a message in a {cfg["task_description"]}.

## Function Types

1. **information_provision**: Provides facts, data, intermediate calculations, or partial results that advance the solution. Includes reporting computed values, stating known quantities, or presenting new numerical results.
   Example: {examples["information_provision"][0]}
   Example: {examples["information_provision"][1]}

2. **reasoning_guidance**: Provides reasoning direction, problem decomposition, step-by-step plans, or conceptual frameworks. Includes breaking the problem into sub-problems, suggesting solution strategies, or outlining multi-step approaches.
   Example: {examples["reasoning_guidance"][0]}
   Example: {examples["reasoning_guidance"][1]}

3. **verification**: Checks, corrects, or confirms the correctness of previous work. Includes identifying errors, validating results, pointing out mistakes, or confirming a step is correct with a specific reason.
   Example: {examples["verification"][0]}
   Example: {examples["verification"][1]}

4. **coordination**: Manages the flow of the conversation, assigns tasks, requests clarification, or controls turn-taking. Includes delegating sub-tasks, asking for more information, or directing the problem-solving process.
   Example: {examples["coordination"][0]}
   Example: {examples["coordination"][1]}

5. **acknowledgment**: Simple confirmation, repetition, or agreement that adds no new information or reasoning. Includes restating what was already said without extending it.
   Example: {examples["acknowledgment"][0]}
   Example: {examples["acknowledgment"][1]}

## Decision Rules

- If a message both provides new results AND checks previous work, classify as **verification** (checking takes priority).
- If a message provides a reasoning plan AND new results, classify as **reasoning_guidance** (the plan is the primary function).
- If a message confirms correctness WITH a substantive explanation of why, classify as **verification** (not acknowledgment).
- If a message simply agrees or restates without adding new information, classify as **acknowledgment**.

## Output Format

Respond with ONLY a JSON object (no markdown, no extra text):
{{"type": "<function_type>", "confidence": <0.0-1.0>, "reasoning": "<brief explanation>"}}
"""


ANNOTATION_SYSTEM_PROMPT = build_annotation_system_prompt("math")


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def build_annotation_prompt(messages: list[dict], target_idx: int) -> str:
    lines = ["## Conversation Context\n"]
    for i, msg in enumerate(messages):
        marker = " <<< TARGET MESSAGE >>>" if i == target_idx else ""
        lines.append(f"[Message {i}] {msg['sender']} -> {msg['receiver']}:{marker}")
        lines.append(msg["content"])
        lines.append("")
    lines.append(f"Classify the function of Message {target_idx}.")
    return "\n".join(lines)


def annotate_message(client: OpenAI, model: str, messages: list[dict], target_idx: int, max_tokens: int,
                     system_prompt: str | None = None) -> dict:
    user_prompt = build_annotation_prompt(messages, target_idx)
    api_messages = [
        {"role": "system", "content": system_prompt or ANNOTATION_SYSTEM_PROMPT},
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
        logger.warning("Failed to parse annotation: %s", raw[:200])
        return {"type": "unknown", "confidence": 0.0, "reasoning": f"Parse error: {raw[:100]}"}


def compute_cohens_kappa(labels1: list[str], labels2: list[str]) -> float:
    from collections import Counter
    assert len(labels1) == len(labels2)
    n = len(labels1)
    if n == 0:
        return 0.0
    agree = sum(1 for a, b in zip(labels1, labels2) if a == b)
    p_o = agree / n
    counts1 = Counter(labels1)
    counts2 = Counter(labels2)
    all_labels = set(labels1) | set(labels2)
    p_e = sum((counts1[l] / n) * (counts2[l] / n) for l in all_labels)
    if p_e >= 1.0:
        return 1.0
    return (p_o - p_e) / (1 - p_e)


def main():
    parser = argparse.ArgumentParser(description="Functional annotation of inter-agent messages")
    parser.add_argument("--config", type=str, default="configs/mvp.yaml")
    parser.add_argument("--traces", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--test-retest", action="store_true", help="Run twice and compute Cohen's kappa")
    parser.add_argument("--cross-model", action="store_true", help="Cross-model annotation with model B")
    parser.add_argument("--model-b-base", type=str, default=None, help="Model B API base URL")
    parser.add_argument("--model-b-name", type=str, default=None, help="Model B model name")
    parser.add_argument("--task-domain", type=str, default="math", choices=list(_DOMAIN_CONFIGS.keys()),
                        help="Task domain for annotation examples (math or code)")
    args = parser.parse_args()

    if args.test_retest and args.cross_model:
        parser.error("--test-retest and --cross-model are mutually exclusive")

    cfg = load_config(args.config)
    traces_path = args.traces or os.path.join(cfg["output"]["trace_dir"], "traces.jsonl")
    output_path = args.output or os.path.join(cfg["output"]["annotation_dir"], "annotations.jsonl")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    client_a = OpenAI(base_url=cfg["model"]["api_base"], api_key=[REDACTED]"model"]["api_key"])
    model_a = cfg["model"]["name"]
    max_tokens = cfg.get("annotation", {}).get("max_tokens", 512)
    system_prompt = build_annotation_system_prompt(args.task_domain)

    with open(traces_path) as fin:
        tasks = []
        for line_num, line in enumerate(fin, 1):
            line = line.strip()
            if not line:
                continue
            try:
                tasks.append(json.loads(line))
            except json.JSONDecodeError:
                logger.warning("Skipping malformed JSON at line %d", line_num)

    if args.cross_model:
        model_b_cfg = cfg.get("annotation", {}).get("model_b", cfg.get("model_b", {}))
        # Fallback to port 8001 when no config/CLI override — assumes second vLLM instance for cross-model.
        model_b_base = args.model_b_base or model_b_cfg.get("api_base", "http://localhost:8001/v1")
        model_b_name = args.model_b_name or model_b_cfg.get("name", "")
        model_b_key = model_b_cfg.get("api_key", "EMPTY")

        model_a_base = cfg["model"]["api_base"]
        if model_a_base.rstrip("/") == model_b_base.rstrip("/"):
            raise ValueError(
                f"model and model_b point to the same API base ({model_a_base}). "
                "Cross-model annotation requires different models to produce independent annotations."
            )

        client_b = OpenAI(base_url=model_b_base, api_key=[REDACTED]

        results = []
        labels_a = []
        labels_b = []

        for task in tasks:
            task_id = task["task_id"]
            messages = [m for m in task["messages"] if m.get("round", 0) > 0]
            for msg_idx in range(len(messages)):
                logger.info("Task %s msg %d: annotating (model A)", task_id, msg_idx)
                ann_a = annotate_message(client_a, model_a, messages, msg_idx, max_tokens, system_prompt)

                logger.info("Task %s msg %d: annotating (model B)", task_id, msg_idx)
                ann_b = annotate_message(client_b, model_b_name, messages, msg_idx, max_tokens, system_prompt)

                type_a = ann_a.get("type", "unknown")
                type_b = ann_b.get("type", "unknown")
                labels_a.append(type_a)
                labels_b.append(type_b)

                record = {
                    "task_id": task_id,
                    "message_index": msg_idx,
                    "sender": messages[msg_idx]["sender"],
                    "receiver": messages[msg_idx]["receiver"],
                    "annotation_a": ann_a,
                    "annotation_b": ann_b,
                    "agreement": type_a == type_b,
                    "content_preview": messages[msg_idx]["content"][:100],
                }
                results.append(record)

        with open(output_path, "w") as fout:
            for r in results:
                fout.write(json.dumps(r, ensure_ascii=False) + "\n")

        kappa = compute_cohens_kappa(labels_a, labels_b)
        n = len(labels_a)
        agree_count = sum(1 for a, b in zip(labels_a, labels_b) if a == b)
        percent_agreement = agree_count / n if n > 0 else 0.0

        disagreements = []
        for r in results:
            type_a = r["annotation_a"].get("type", "unknown")
            type_b = r["annotation_b"].get("type", "unknown")
            if type_a != type_b:
                disagreements.append({
                    "task_id": r["task_id"],
                    "message_index": r["message_index"],
                    "model_a": type_a,
                    "model_b": type_b,
                })

        cross_stats = {
            "cohens_kappa": round(kappa, 4),
            "percent_agreement": round(percent_agreement, 4),
            "n": n,
            "disagreements": disagreements,
        }
        cross_path = output_path.replace(".jsonl", "_cross_model.json")
        with open(cross_path, "w") as f:
            json.dump(cross_stats, f, indent=2)
        logger.info("Cross-model kappa: %.4f, agreement: %.2f%%, saved to %s",
                     kappa, percent_agreement * 100, cross_path)

    else:
        results_pass1 = []
        results_pass2 = []

        for task in tasks:
            task_id = task["task_id"]
            messages = [m for m in task["messages"] if m.get("round", 0) > 0]

            for msg_idx in range(len(messages)):
                logger.info("Task %s msg %d: annotating (pass 1)", task_id, msg_idx)
                annotation = annotate_message(client_a, model_a, messages, msg_idx, max_tokens, system_prompt)
                record = {
                    "task_id": task_id,
                    "message_index": msg_idx,
                    "sender": messages[msg_idx]["sender"],
                    "receiver": messages[msg_idx]["receiver"],
                    "annotation": annotation,
                    "content_preview": messages[msg_idx]["content"][:100],
                }
                results_pass1.append(record)

        with open(output_path, "w") as fout:
            for r in results_pass1:
                fout.write(json.dumps(r, ensure_ascii=False) + "\n")

        if args.test_retest:
            logger.info("Running test-retest pass 2")
            for task in tasks:
                task_id = task["task_id"]
                messages = [m for m in task["messages"] if m.get("round", 0) > 0]
                for msg_idx in range(len(messages)):
                    logger.info("Task %s msg %d: annotating (pass 2)", task_id, msg_idx)
                    annotation = annotate_message(client_a, model_a, messages, msg_idx, max_tokens, system_prompt)
                    results_pass2.append(annotation)

            labels1 = [r["annotation"].get("type", "unknown") for r in results_pass1]
            labels2 = [r.get("type", "unknown") for r in results_pass2]
            kappa = compute_cohens_kappa(labels1, labels2)
            logger.info("Test-retest Cohen's kappa: %.4f", kappa)

            retest_path = output_path.replace(".jsonl", "_retest.json")
            with open(retest_path, "w") as f:
                json.dump({"cohens_kappa": round(kappa, 4), "n": len(labels1)}, f, indent=2)
            logger.info("Retest results saved to %s", retest_path)

    logger.info("Annotations saved to %s", output_path)


if __name__ == "__main__":
    main()
