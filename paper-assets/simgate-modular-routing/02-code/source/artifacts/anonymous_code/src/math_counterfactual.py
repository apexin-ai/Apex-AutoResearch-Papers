"""MATH counterfactual labeling pipeline.

For each MATH problem, runs two trajectories:
1. Pure Internal: LLM reasoning only, no code execution
2. Code Interpreter: LLM + Python code sandbox (ReAct-style)

Produces episode-level labels:
- det-preferred: code interpreter correct + internal wrong
- internal-preferred: internal correct + code interpreter wrong
- no-preference: both correct or both wrong

Input:  MATH dataset (Level 4-5), loaded via HuggingFace or local
Output: data/math-counterfactual/episodes.jsonl
"""

import argparse
import json
import os
import re
import sys
import time
from typing import List, Dict, Any, Optional, Tuple

from code_sandbox import execute_code
from math_answer_utils import extract_boxed_answer, answers_equal

INTERNAL_SYSTEM = (
    "Solve this math problem step by step. "
    "Show your reasoning clearly. "
    "Give your final answer as \\boxed{answer}."
)

CODE_INTERPRETER_SYSTEM = (
    "You MUST solve this problem by writing and executing Python code. "
    "Show your code in a ```python\n...\n``` block, execute it, and report the result. "
    "Do not use mental math or reasoning alone. "
    "Every answer must come from code execution output. "
    "Give your final answer as \\boxed{answer}."
)


def extract_code_blocks(text: str) -> List[str]:
    blocks = re.findall(r'```python\s*\n(.*?)```', text, re.DOTALL)
    if not blocks:
        blocks = re.findall(r'```\s*\n(.*?)```', text, re.DOTALL)
    return blocks


def run_internal(agent, problem: str) -> Dict[str, Any]:
    messages = [
        {"role": "system", "content": INTERNAL_SYSTEM},
        {"role": "user", "content": problem},
    ]
    response = agent._generate(messages)
    answer = extract_boxed_answer(response)
    return {"response": response, "answer": answer}


def run_code_interpreter(agent, problem: str, max_rounds: int = 3) -> Dict[str, Any]:
    messages = [
        {"role": "system", "content": CODE_INTERPRETER_SYSTEM},
        {"role": "user", "content": problem},
    ]

    all_code_outputs = []
    for round_idx in range(max_rounds):
        response = agent._generate(messages)
        code_blocks = extract_code_blocks(response)

        if not code_blocks:
            break

        for code in code_blocks:
            result = execute_code(code)
            all_code_outputs.append({"code": code, "output": result})
            messages.append({"role": "assistant", "content": response})
            messages.append({"role": "user", "content": f"Code output:\n{result['stdout']}"})
            break

    final_response = agent._generate(messages) if len(messages) > 2 else response
    answer = extract_boxed_answer(final_response)
    return {"response": final_response, "answer": answer, "code_outputs": all_code_outputs}


def main():
    parser = argparse.ArgumentParser(description="MATH counterfactual labeling")
    parser.add_argument("--n_problems", type=int, default=200)
    parser.add_argument("--levels", type=str, default="4,5")
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="results/math-counterfactual")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    print("MATH counterfactual labeling pipeline")
    print(f"Problems: {args.n_problems}, levels: {args.levels}")
    print(f"Output: {args.output_dir}")


if __name__ == "__main__":
    main()
