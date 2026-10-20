#!/usr/bin/env python3
"""
Phase A Step 3: Measure correction horizon for failure steps.

Input:  data/classified_trajectories.jsonl  (from classify_errors.py)
Output: data/correction_measured_trajectories.jsonl

For each failure step:
  - Restores ALFWorld env to that state by replaying prior actions
  - Generates N=10 correction continuations from the failure point
  - Records min/mean correction horizon (steps to task completion)

Dependencies: vllm (or transformers), alfworld, pyyaml
Usage:
    python measure_correction_horizon.py
    python measure_correction_horizon.py --n_attempts 10 --max_correction_steps 30
"""

import os
import sys
import json
import re
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

PROJECT_ROOT = Path("/root/error_type_pref_optim")
ETO_ROOT = PROJECT_ROOT / "ETO"
MODEL_PATH = str(PROJECT_ROOT / "models" / "Qwen3-8B")
DATA_DIR = PROJECT_ROOT / "data"
ALFWORLD_DATA = str(ETO_ROOT / "eval_agent" / "data" / "alfworld")

os.environ["ALFWORLD_DATA"] = ALFWORLD_DATA
sys.path.insert(0, str(ETO_ROOT))

logger = logging.getLogger("measure_correction_horizon")


def process_ob(ob: str) -> str:
    if ob.startswith("You arrive at loc "):
        ob = ob[ob.find(". ") + 2:]
    return ob


def parse_action(llm_output: str) -> Optional[str]:
    pattern = re.compile(r"Action:\s?(.*)", re.DOTALL)
    m = pattern.search(llm_output)
    return m.group(1).strip() if m else None


# ---------------------------------------------------------------------------
# Prompt builder (same as generate_trajectories)
# ---------------------------------------------------------------------------
def build_initial_messages(instruction: str, icl_examples: list, task_obs: str) -> List[Dict[str, str]]:
    messages: List[Dict[str, str]] = [{"role": "user", "content": instruction}]
    messages.append({"role": "assistant", "content": "OK"})
    for ex in icl_examples:
        for turn in ex:
            role = turn.get("role", "assistant" if turn.get("from") == "gpt" else "user")
            content = turn.get("content", turn.get("value", ""))
            messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": task_obs})
    return messages


# ---------------------------------------------------------------------------
# Agent wrappers (same interface as generate_trajectories)
# ---------------------------------------------------------------------------
class VLLMAgent:
    def __init__(self, model_path: str, temperature: float = 0.7,
                 max_tokens: int = 512, tensor_parallel_size: int = 1):
        from vllm import LLM, SamplingParams
        self.llm = LLM(
            model=model_path,
            tensor_parallel_size=tensor_parallel_size,
            trust_remote_code=True,
            max_model_len=8192,
        )
        self.tokenizer = self.llm.get_tokenizer()
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, messages: List[Dict[str, str]], seed: int = 42) -> str:
        from vllm import SamplingParams
        sp = SamplingParams(
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stop=["\nObservation:", "\nTask:", "\n---"],
            seed=seed,
        )
        prompt = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = self.llm.generate([prompt], sp)
        return outputs[0].outputs[0].text.strip()


class TransformersAgent:
    def __init__(self, model_path: str, temperature: float = 0.7, max_tokens: int = 512):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True,
        )
        self.model.eval()
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, messages: List[Dict[str, str]], seed: int = 42) -> str:
        import torch
        torch.manual_seed(seed)
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer(text, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            out = self.model.generate(
                **inputs, max_new_tokens=self.max_tokens,
                temperature=self.temperature, do_sample=True,
            )
        generated = self.tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        for stop in ["\nObservation:", "\nTask:", "\n---"]:
            if stop in generated:
                generated = generated[:generated.index(stop)]
        return generated.strip()


# ---------------------------------------------------------------------------
# ALFWorld env management
# ---------------------------------------------------------------------------
class ALFWorldEnvManager:
    """Manages ALFWorld env initialization and game navigation."""

    def __init__(self, split: str = "train"):
        import yaml
        import alfworld
        import alfworld.agents.environment as alf_envs

        with open(os.path.join(ALFWORLD_DATA, "base_config.yaml")) as f:
            config = yaml.safe_load(f)

        split_map = {"train": "train", "dev": "eval_in_distribution", "test": "eval_out_of_distribution"}
        alf_split = split_map[split]

        self.config = config
        self.alf_split = alf_split
        self.alf_envs = alf_envs
        self._env = None

    def _create_env(self):
        env = getattr(self.alf_envs, self.config["env"]["type"])(
            self.config, train_eval=self.alf_split
        )
        return env.init_env(batch_size=1)

    def navigate_to_game(self, target_task_index: int) -> Tuple[Any, str, str]:
        """Create a fresh env and navigate to the specified game index.
        Returns (env, obs_text, game_file)."""
        env = self._create_env()
        for i in range(target_task_index):
            env.reset()
        obs, info = env.reset()
        obs_text = "\n".join(obs[0].split("\n\n")[1:])
        game_file = info["extra.gamefile"][0]
        return env, obs_text, game_file

    def replay_actions(self, env, actions: List[str]) -> bool:
        """Replay a sequence of actions. Returns True if all succeeded without ending the game."""
        for action in actions:
            obs_raw, reward, done, info = env.step([action])
            if done or info["won"][0]:
                return False
        return True


# ---------------------------------------------------------------------------
# Correction continuation
# ---------------------------------------------------------------------------
def run_correction(
    agent,
    env,
    messages_prefix: List[Dict[str, str]],
    max_steps: int = 30,
    seed: int = 42,
) -> Optional[int]:
    """Run one correction continuation from the current env state.
    Returns number of steps to task completion, or None if failed."""
    messages = list(messages_prefix)

    for step in range(max_steps):
        llm_output = agent.generate(messages, seed=seed + step)
        action = parse_action(llm_output)

        if action is None:
            messages.append({"role": "assistant", "content": llm_output})
            messages.append({"role": "user", "content": "Observation: Error Input. Your input must contains 'Action: '"})
            continue

        obs_raw, reward, done, info = env.step([action])
        observation = process_ob(obs_raw[0])
        won = info["won"][0]

        messages.append({"role": "assistant", "content": llm_output})
        messages.append({"role": "user", "content": f"Observation: {observation}"})

        if done or won:
            if won:
                return step + 1
            return None

    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Measure correction horizon for failure steps")
    parser.add_argument("--input", type=str, default=str(DATA_DIR / "classified_trajectories.jsonl"))
    parser.add_argument("--output", type=str, default=str(DATA_DIR / "correction_measured_trajectories.jsonl"))
    parser.add_argument("--model_path", type=str, default=MODEL_PATH)
    parser.add_argument("--backend", type=str, default="vllm", choices=["vllm", "transformers"])
    parser.add_argument("--tensor_parallel_size", type=int, default=1)
    parser.add_argument("--n_attempts", type=int, default=10)
    parser.add_argument("--max_correction_steps", type=int, default=30)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--split", type=str, default="train", choices=["train", "dev", "test"])
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
    logger.info(f"Loaded {len(trajectories)} trajectories")

    logger.info(f"Loading agent from {args.model_path} (backend={args.backend})")
    if args.backend == "vllm":
        agent = VLLMAgent(args.model_path, temperature=args.temperature,
                          tensor_parallel_size=args.tensor_parallel_size)
    else:
        agent = TransformersAgent(args.model_path, temperature=args.temperature)

    instruction_path = str(ETO_ROOT / "eval_agent" / "prompt" / "instructions" / "alfworld_inst.txt")
    icl_path = str(ETO_ROOT / "eval_agent" / "prompt" / "icl_examples" / "alfworld_icl.json")
    with open(instruction_path) as f:
        instruction = f.read()
    with open(icl_path) as f:
        icl_examples = json.load(f)

    env_manager = ALFWorldEnvManager(split=args.split)
    out_f = open(args.output, "w")

    for traj_i, traj in enumerate(trajectories):
        failure_steps = [s for s in traj["steps"] if s.get("is_failure")]
        if not failure_steps:
            out_f.write(json.dumps(traj, ensure_ascii=False) + "\n")
            out_f.flush()
            continue

        task_index = traj.get("task_index", traj_i)
        task_desc = traj["task_description"]
        logger.info(f"[{traj_i+1}/{len(trajectories)}] traj={traj['trajectory_id']} "
                     f"failures={len(failure_steps)}")

        for fi, fstep in enumerate(failure_steps):
            step_idx = fstep["step_idx"]
            logger.info(f"  Measuring correction for step {step_idx} "
                         f"(type={fstep.get('error_classification', {}).get('primary_error_type', '?')})")

            prior_actions = []
            for s in traj["steps"][:step_idx]:
                a = s.get("agent_action", "")
                if a and "Error Input" not in s.get("observation", ""):
                    prior_actions.append(a)

            correction_horizons = []
            successful_attempts = 0

            for attempt in range(args.n_attempts):
                try:
                    env, obs_text, game_file = env_manager.navigate_to_game(task_index)

                    if prior_actions:
                        replay_ok = env_manager.replay_actions(env, prior_actions)
                        if not replay_ok:
                            correction_horizons.append(None)
                            continue

                    messages = build_initial_messages(instruction, icl_examples, task_desc)
                    for s in traj["steps"][:step_idx + 1]:
                        thought = s.get("agent_thought", f"Thought: Let me try.\nAction: {s.get('agent_action', '')}")
                        messages.append({"role": "assistant", "content": thought})
                        messages.append({"role": "user", "content": f"Observation: {s.get('observation', '')}"})

                    seed = 1000 * (step_idx + 1) + attempt
                    horizon = run_correction(
                        agent, env, messages,
                        max_steps=args.max_correction_steps,
                        seed=seed,
                    )
                    correction_horizons.append(horizon)
                    if horizon is not None:
                        successful_attempts += 1

                except Exception as e:
                    logger.warning(f"    Attempt {attempt} failed: {e}")
                    correction_horizons.append(None)

            successful_values = [h for h in correction_horizons if h is not None]
            is_uncorrectable = len(successful_values) == 0

            measurement = {
                "n_attempts": args.n_attempts,
                "successful_attempts": successful_attempts,
                "correction_horizons": correction_horizons,
                "min_correction_horizon": min(successful_values) if successful_values else None,
                "mean_correction_horizon": round(sum(successful_values) / len(successful_values), 2) if successful_values else None,
                "is_uncorrectable": is_uncorrectable,
            }

            for s in traj["steps"]:
                if s["step_idx"] == step_idx:
                    s["correction_measurement"] = measurement
                    break

            logger.info(f"    horizons={correction_horizons} "
                         f"min={measurement['min_correction_horizon']} "
                         f"uncorrectable={is_uncorrectable}")

        out_f.write(json.dumps(traj, ensure_ascii=False) + "\n")
        out_f.flush()

        if args.debug and traj_i >= 2:
            break

    out_f.close()
    logger.info(f"Done. Output: {args.output}")


if __name__ == "__main__":
    main()
