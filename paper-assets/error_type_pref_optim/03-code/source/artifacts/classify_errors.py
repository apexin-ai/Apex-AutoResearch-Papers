#!/usr/bin/env python3
"""
Phase A Step 2: Classify failure steps in ALFWorld trajectories.

Input:  data/trajectories.jsonl  (from generate_trajectories.py)
Output: data/classified_trajectories.jsonl

For each step, determines:
  1. Whether it is a failure (heuristic + LLM)
  2. Error type: action / verification / planning (LLM zero-shot)

Dependencies: vllm (or transformers), json
Usage:
    python classify_errors.py
    python classify_errors.py --input data/trajectories.jsonl --backend vllm
"""

import os
import sys
import json
import re
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

PROJECT_ROOT = Path("/root/error_type_pref_optim")
ETO_ROOT = PROJECT_ROOT / "ETO"
MODEL_PATH = str(PROJECT_ROOT / "models" / "Qwen3-8B")
DATA_DIR = PROJECT_ROOT / "data"

logger = logging.getLogger("classify_errors")

# ---------------------------------------------------------------------------
# Heuristic failure indicators
# ---------------------------------------------------------------------------
FAILURE_INDICATORS = [
    "Nothing happened",
    "Error Input",
    "You can't see such",
    "There's nothing",
]

NOTHING_HAPPENED_PATTERN = re.compile(r"Nothing happened", re.IGNORECASE)


def is_likely_failure_heuristic(step: dict, prev_steps: list, task_desc: str) -> bool:
    obs = step.get("observation", "")
    action = step.get("agent_action", "")
    for indicator in FAILURE_INDICATORS:
        if indicator.lower() in obs.lower():
            return True
    if action and not action.strip():
        return True
    return False


# ---------------------------------------------------------------------------
# Classification prompt
# ---------------------------------------------------------------------------
CLASSIFICATION_PROMPT = """You are an expert at analyzing agent behavior in household task environments.

Given a task description, the trajectory history, and a specific step, determine:
1. Whether this step is a FAILURE (the agent made an error that hinders task completion)
2. If it is a failure, classify the PRIMARY error type:

**Error Types:**
- **action**: The agent tried an invalid or incorrect action (wrong syntax, interacting with non-existent object, wrong action verb). The error is in the immediate physical execution.
- **verification**: The agent failed to verify the outcome of a previous action or misinterpreted an observation. It proceeded based on incorrect beliefs about the current state.
- **planning**: The agent chose a wrong subgoal or strategy. The action itself may be valid, but it moves toward the wrong objective or follows an incorrect plan.

**Classification Rule:** If an incorrect action was caused by a wrong subgoal decomposition, classify as **planning** (root cause). If the action is syntactically wrong or targets a non-existent object but the plan was correct, classify as **action**.

Task: {task_description}

Trajectory so far:
{trajectory_context}

Current step (step {step_idx}):
  Action: {action}
  Observation: {observation}

Respond in this exact JSON format (no other text):
{{"is_failure": true/false, "primary_error_type": "action"/"verification"/"planning"/null, "reasoning": "...", "secondary_error_type": "action"/"verification"/"planning"/null}}"""


def format_trajectory_context(steps: list, up_to: int) -> str:
    lines = []
    for s in steps[:up_to]:
        lines.append(f"  Step {s['step_idx']}: Action: {s.get('agent_action', 'N/A')}")
        lines.append(f"    Observation: {s.get('observation', 'N/A')}")
    return "\n".join(lines) if lines else "(start of trajectory)"


# ---------------------------------------------------------------------------
# LLM wrapper (reuse from generate_trajectories)
# ---------------------------------------------------------------------------
class VLLMClassifier:
    def __init__(self, model_path: str, tensor_parallel_size: int = 1):
        from vllm import LLM, SamplingParams
        self.llm = LLM(
            model=model_path,
            tensor_parallel_size=tensor_parallel_size,
            trust_remote_code=True,
            max_model_len=8192,
        )
        self.tokenizer = self.llm.get_tokenizer()
        self.sampling_params = SamplingParams(
            temperature=0.0,
            max_tokens=512,
        )

    def classify(self, prompt: str) -> str:
        messages = [
            {"role": "system", "content": "You are an expert error classifier. Always respond with valid JSON only."},
            {"role": "user", "content": prompt},
        ]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = self.llm.generate([text], self.sampling_params)
        return outputs[0].outputs[0].text.strip()

    def classify_batch(self, prompts: List[str]) -> List[str]:
        all_texts = []
        for prompt in prompts:
            messages = [
                {"role": "system", "content": "You are an expert error classifier. Always respond with valid JSON only."},
                {"role": "user", "content": prompt},
            ]
            all_texts.append(self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))
        outputs = self.llm.generate(all_texts, self.sampling_params)
        return [o.outputs[0].text.strip() for o in outputs]


class TransformersClassifier:
    def __init__(self, model_path: str):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, torch_dtype=torch.bfloat16, device_map="auto",
            trust_remote_code=True,
        )
        self.model.eval()

    def classify(self, prompt: str) -> str:
        import torch
        messages = [
            {"role": "system", "content": "You are an expert error classifier. Always respond with valid JSON only."},
            {"role": "user", "content": prompt},
        ]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            out = self.model.generate(**inputs, max_new_tokens=512, temperature=0.0, do_sample=False)
        return self.tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()

    def classify_batch(self, prompts: List[str]) -> List[str]:
        return [self.classify(p) for p in prompts]


# ---------------------------------------------------------------------------
# Parse LLM response
# ---------------------------------------------------------------------------
def parse_classification(response: str) -> Dict[str, Any]:
    try:
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if match:
            data = json.loads(match.group())
            valid_types = {"action", "verification", "planning", None}
            return {
                "is_failure": bool(data.get("is_failure", False)),
                "primary_error_type": data.get("primary_error_type") if data.get("primary_error_type") in valid_types else None,
                "reasoning": str(data.get("reasoning", "")),
                "secondary_error_type": data.get("secondary_error_type") if data.get("secondary_error_type") in valid_types else None,
            }
    except (json.JSONDecodeError, AttributeError):
        pass
    return {
        "is_failure": False,
        "primary_error_type": None,
        "reasoning": f"PARSE_ERROR: {response[:200]}",
        "secondary_error_type": None,
    }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def classify_trajectory(trajectory: dict, classifier, batch_size: int = 32) -> dict:
    steps = trajectory["steps"]
    task_desc = trajectory["task_description"]

    candidates = []
    for i, step in enumerate(steps):
        if is_likely_failure_heuristic(step, steps[:i], task_desc):
            candidates.append(i)

    non_candidates = [i for i in range(len(steps)) if i not in candidates]
    all_indices = candidates + non_candidates

    prompts = []
    prompt_indices = []
    for i in all_indices:
        step = steps[i]
        prompt = CLASSIFICATION_PROMPT.format(
            task_description=task_desc,
            trajectory_context=format_trajectory_context(steps, up_to=i),
            step_idx=step["step_idx"],
            action=step.get("agent_action", "N/A"),
            observation=step.get("observation", "N/A"),
        )
        prompts.append(prompt)
        prompt_indices.append(i)

    results_raw = []
    for batch_start in range(0, len(prompts), batch_size):
        batch = prompts[batch_start:batch_start + batch_size]
        results_raw.extend(classifier.classify_batch(batch))

    for idx, raw in zip(prompt_indices, results_raw):
        classification = parse_classification(raw)
        steps[idx]["is_failure"] = classification["is_failure"]
        if classification["is_failure"]:
            steps[idx]["error_classification"] = {
                "primary_error_type": classification["primary_error_type"],
                "reasoning": classification["reasoning"],
                "secondary_error_type": classification["secondary_error_type"],
                "classifier_model": "Qwen3-8B",
                "classifier_prompt_version": "v1",
            }
        else:
            steps[idx]["error_classification"] = None

    trajectory["steps"] = steps
    n_failures = sum(1 for s in steps if s.get("is_failure"))
    type_counts = {}
    for s in steps:
        if s.get("is_failure") and s.get("error_classification"):
            t = s["error_classification"]["primary_error_type"]
            type_counts[t] = type_counts.get(t, 0) + 1
    trajectory["failure_summary"] = {
        "total_failures": n_failures,
        "type_counts": type_counts,
    }
    return trajectory


def main():
    parser = argparse.ArgumentParser(description="Classify failure steps in ALFWorld trajectories")
    parser.add_argument("--input", type=str, default=str(DATA_DIR / "trajectories.jsonl"))
    parser.add_argument("--output", type=str, default=str(DATA_DIR / "classified_trajectories.jsonl"))
    parser.add_argument("--model_path", type=str, default=MODEL_PATH)
    parser.add_argument("--backend", type=str, default="vllm", choices=["vllm", "transformers"])
    parser.add_argument("--tensor_parallel_size", type=int, default=1)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    trajectories = []
    with open(args.input) as f:
        for line in f:
            if line.strip():
                trajectories.append(json.loads(line))
    logger.info(f"Loaded {len(trajectories)} trajectories from {args.input}")

    logger.info(f"Loading classifier model from {args.model_path} (backend={args.backend})")
    if args.backend == "vllm":
        classifier = VLLMClassifier(args.model_path, tensor_parallel_size=args.tensor_parallel_size)
    else:
        classifier = TransformersClassifier(args.model_path)

    out_f = open(args.output, "w")
    total_failures = 0
    total_steps = 0

    for i, traj in enumerate(trajectories):
        logger.info(f"[{i+1}/{len(trajectories)}] Classifying trajectory {traj['trajectory_id']}")
        classified = classify_trajectory(traj, classifier, batch_size=args.batch_size)
        out_f.write(json.dumps(classified, ensure_ascii=False) + "\n")
        out_f.flush()

        n_f = classified["failure_summary"]["total_failures"]
        n_s = len(classified["steps"])
        total_failures += n_f
        total_steps += n_s
        logger.info(f"  failures={n_f}/{n_s}  types={classified['failure_summary']['type_counts']}")

        if args.debug and i >= 4:
            break

    out_f.close()
    logger.info(f"Done. Total failures: {total_failures}/{total_steps} "
                f"({total_failures/max(total_steps,1)*100:.1f}%). Output: {args.output}")


if __name__ == "__main__":
    main()
