#!/usr/bin/env python3
"""
Phase A Step 1: Generate ALFWorld trajectories using Qwen3-8B.

Input:  ALFWorld environment (via ETO codebase)
Output: data/trajectories.jsonl — one JSON object per trajectory

Dependencies: vllm, alfworld, transformers, pyyaml
Usage:
    python generate_trajectories.py --num_trajectories 200 --split train
    python generate_trajectories.py --num_trajectories 10 --split test --debug
"""

import os
import sys
import json
import re
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# ---------------------------------------------------------------------------
# Paths  (adjust if repo layout changes)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path("/root/error_type_pref_optim")
ETO_ROOT = PROJECT_ROOT / "ETO"
MODEL_PATH = str(PROJECT_ROOT / "models" / "Qwen3-8B")
DATA_DIR = PROJECT_ROOT / "data"
ALFWORLD_DATA = str(ETO_ROOT / "eval_agent" / "data" / "alfworld")

os.environ["ALFWORLD_DATA"] = ALFWORLD_DATA

sys.path.insert(0, str(ETO_ROOT))

logger = logging.getLogger("generate_trajectories")

# ---------------------------------------------------------------------------
# ALFWorld task‑type mapping (from ETO)
# ---------------------------------------------------------------------------
TASK_TYPE_PREFIXES = {
    "put": "pick_and_place",
    "clean": "pick_clean_then_place",
    "heat": "pick_heat_then_place",
    "cool": "pick_cool_then_place",
    "examine": "look_at_obj",
    "puttwo": "pick_two_obj",
}


def detect_task_type(game_file: str) -> str:
    for prefix, task_type in TASK_TYPE_PREFIXES.items():
        if f"/{prefix}" in game_file or game_file.startswith(prefix):
            return task_type
    return "unknown"


# ---------------------------------------------------------------------------
# Prompt builder  (mirrors ETO's conversation‑format ICL)
# ---------------------------------------------------------------------------
def build_initial_messages(instruction: str, icl_examples: list, task_obs: str) -> List[Dict[str, str]]:
    messages: List[Dict[str, str]] = [{"role": "user", "content": instruction}]
    messages.append({"role": "assistant", "content": "OK"})

    for ex in icl_examples:
        for j, turn in enumerate(ex):
            role = turn.get("role", "assistant" if turn.get("from") == "gpt" else "user")
            content = turn["content"] if "content" in turn else turn["value"]
            if role == "user":
                messages.append({"role": "user", "content": content})
            else:
                messages.append({"role": "assistant", "content": content})

    messages.append({"role": "user", "content": task_obs})
    return messages


# ---------------------------------------------------------------------------
# vLLM inference wrapper
# ---------------------------------------------------------------------------
class VLLMAgent:
    def __init__(self, model_path: str, temperature: float = 0.7,
                 max_tokens: int = 512, tensor_parallel_size: int = 1,
                 seed: int = 42):
        from vllm import LLM, SamplingParams
        self.llm = LLM(
            model=model_path,
            tensor_parallel_size=tensor_parallel_size,
            trust_remote_code=True,
            max_model_len=8192,
            seed=seed,
        )
        self.tokenizer = self.llm.get_tokenizer()
        self.sampling_params = SamplingParams(
            temperature=temperature,
            max_tokens=max_tokens,
            stop=["\nObservation:", "\nTask:", "\n---"],
            seed=seed,
        )

    def generate(self, messages: List[Dict[str, str]]) -> str:
        prompt = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )
        outputs = self.llm.generate([prompt], self.sampling_params)
        return outputs[0].outputs[0].text.strip()


# ---------------------------------------------------------------------------
# Transformers fallback
# ---------------------------------------------------------------------------
class TransformersAgent:
    def __init__(self, model_path: str, temperature: float = 0.7,
                 max_tokens: int = 512, seed: int = 42):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, torch_dtype=torch.bfloat16, device_map="auto",
            trust_remote_code=True,
        )
        self.model.eval()
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.seed = seed

    def generate(self, messages: List[Dict[str, str]]) -> str:
        import torch
        torch.manual_seed(self.seed)
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            out = self.model.generate(
                **inputs,
                max_new_tokens=self.max_tokens,
                temperature=self.temperature,
                do_sample=True,
            )
        generated = self.tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        for stop in ["\nObservation:", "\nTask:", "\n---"]:
            if stop in generated:
                generated = generated[:generated.index(stop)]
        return generated.strip()


# ---------------------------------------------------------------------------
# ALFWorld environment helpers
# ---------------------------------------------------------------------------
def process_ob(ob: str) -> str:
    if ob.startswith("You arrive at loc "):
        ob = ob[ob.find(". ") + 2:]
    return ob


def parse_action(llm_output: str) -> Optional[str]:
    pattern = re.compile(r"Action:\s?(.*)", re.DOTALL)
    m = pattern.search(llm_output)
    if m:
        return m.group(1).strip()
    return None


def run_trajectory(
    agent,
    env,
    task_obs: str,
    instruction: str,
    icl_examples: list,
    max_steps: int = 40,
) -> Dict[str, Any]:
    messages = build_initial_messages(instruction, icl_examples, task_obs)
    steps = []
    success = False
    total_steps = 0

    for step_idx in range(max_steps):
        llm_output = agent.generate(messages)
        action = parse_action(llm_output)

        if action is None:
            observation = "Error Input. Your input must contains 'Action: '"
            obs_text = f"Observation: {observation}"
            steps.append({
                "step_idx": step_idx,
                "agent_action": llm_output,
                "observation": observation,
                "is_failure": None,
            })
            messages.append({"role": "assistant", "content": llm_output})
            messages.append({"role": "user", "content": obs_text})
            total_steps += 1
            continue

        observation_raw, reward, done, info = env.step([action])
        observation = process_ob(observation_raw[0])
        won = info["won"][0]

        obs_text = f"Observation: {observation}"
        steps.append({
            "step_idx": step_idx,
            "agent_action": action,
            "agent_thought": llm_output,
            "observation": observation,
            "is_failure": None,
        })
        messages.append({"role": "assistant", "content": llm_output})
        messages.append({"role": "user", "content": obs_text})
        total_steps += 1

        if done or won:
            success = won
            break

    return {
        "steps": steps,
        "success": success,
        "total_steps": total_steps,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Generate ALFWorld trajectories with Qwen3-8B")
    parser.add_argument("--num_trajectories", type=int, default=200)
    parser.add_argument("--split", type=str, default="train", choices=["train", "dev", "test"])
    parser.add_argument("--max_steps", type=int, default=40)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--model_path", type=str, default=MODEL_PATH)
    parser.add_argument("--output", type=str, default=str(DATA_DIR / "trajectories.jsonl"))
    parser.add_argument("--backend", type=str, default="vllm", choices=["vllm", "transformers"])
    parser.add_argument("--tensor_parallel_size", type=int, default=1)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    # ---- Load ALFWorld env ------------------------------------------------
    import yaml
    import alfworld
    import alfworld.agents.environment as alf_envs

    with open(os.path.join(ALFWORLD_DATA, "base_config.yaml")) as f:
        config = yaml.safe_load(f)

    split_map = {"train": ("train", 3321), "dev": ("eval_in_distribution", 140),
                 "test": ("eval_out_of_distribution", 134)}
    alf_split, n_total = split_map[args.split]
    n_tasks = min(args.num_trajectories, n_total)

    env = getattr(alf_envs, config["env"]["type"])(config, train_eval=alf_split)
    env = env.init_env(batch_size=1)

    # ---- Load prompts -----------------------------------------------------
    instruction_path = str(ETO_ROOT / "eval_agent" / "prompt" / "instructions" / "alfworld_inst.txt")
    icl_path = str(ETO_ROOT / "eval_agent" / "prompt" / "icl_examples" / "alfworld_icl.json")

    with open(instruction_path) as f:
        instruction = f.read()
    with open(icl_path) as f:
        icl_examples = json.load(f)

    # ---- Load agent -------------------------------------------------------
    logger.info(f"Loading model from {args.model_path} with backend={args.backend}")
    if args.backend == "vllm":
        agent = VLLMAgent(args.model_path, temperature=args.temperature,
                          tensor_parallel_size=args.tensor_parallel_size, seed=args.seed)
    else:
        agent = TransformersAgent(args.model_path, temperature=args.temperature, seed=args.seed)

    # ---- Generate trajectories --------------------------------------------
    logger.info(f"Generating {n_tasks} trajectories on split={args.split}")
    out_f = open(args.output, "w")
    success_count = 0

    for idx in range(n_tasks):
        obs, info = env.reset()
        obs_text = "\n".join(obs[0].split("\n\n")[1:])
        game_file = info["extra.gamefile"][0]
        task_type = detect_task_type(game_file)

        logger.info(f"[{idx+1}/{n_tasks}] game_file={game_file}  task_type={task_type}")

        result = run_trajectory(
            agent, env, obs_text, instruction, icl_examples,
            max_steps=args.max_steps,
        )

        record = {
            "trajectory_id": f"traj_{idx:04d}",
            "task_type": task_type,
            "task_description": obs_text,
            "success": result["success"],
            "steps": result["steps"],
            "total_steps": result["total_steps"],
            "game_file": game_file,
            "task_index": idx,
            "metadata": {
                "model": "Qwen3-8B",
                "temperature": args.temperature,
                "seed": args.seed,
                "split": args.split,
                "backend": args.backend,
                "max_steps": args.max_steps,
            },
        }
        out_f.write(json.dumps(record, ensure_ascii=False) + "\n")
        out_f.flush()

        if result["success"]:
            success_count += 1
        logger.info(f"  success={result['success']}  steps={result['total_steps']}  "
                     f"running_sr={success_count}/{idx+1}")

        if args.debug and idx >= 4:
            break

    out_f.close()
    logger.info(f"Done. {success_count}/{n_tasks} succeeded. Output: {args.output}")


if __name__ == "__main__":
    main()
