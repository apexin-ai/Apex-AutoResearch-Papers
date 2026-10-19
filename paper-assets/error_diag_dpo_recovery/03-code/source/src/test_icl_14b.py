"""ICL Few-shot test with Qwen3-14B-AWQ + expert trajectories on ALFWorld.

Usage:
  CUDA_VISIBLE_DEVICES=1 python src/test_icl_14b.py \
    --split dev --num_tasks 25 --gpu 0 --temperature 0
"""

import os
import re
import json
import time
import logging
import argparse
from pathlib import Path
from collections import defaultdict

import yaml
import torch
import alfworld
from alfworld.agents.environment import get_environment
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger("test_icl_14b")

PREFIXES = {
    "pick_and_place": "put",
    "pick_clean_then_place": "clean",
    "pick_heat_then_place": "heat",
    "pick_cool_then_place": "cool",
    "look_at_obj": "examine",
    "pick_two_obj": "puttwo",
}

ETO_ROOT = "/root/autodl-tmp/rl-active-probe-fl/eto_repo"
SFT_DATA = os.path.join(ETO_ROOT, "data/alfworld_sft.json")


def get_task_type(game_file: str) -> str:
    for k in PREFIXES:
        if f"/{k}" in game_file:
            return k
    return "unknown"


def process_ob(ob: str) -> str:
    if ob.startswith("You arrive at loc "):
        ob = ob[ob.find(". ") + 2 :]
    return ob


def load_alfworld_env(split: str):
    alfworld_data = "/root/autodl-tmp/alfworld_data"
    os.environ["ALFWORLD_DATA"] = alfworld_data

    with open(os.path.join(alfworld_data, "base_config.yaml")) as f:
        config = yaml.safe_load(f)

    split_map = {
        "train": ("train", 3321),
        "dev": ("eval_in_distribution", 140),
        "test": ("eval_out_of_distribution", 134),
    }
    env_split, n_tasks = split_map[split]

    EnvClass = get_environment(config["env"]["type"])
    env = EnvClass(config, train_eval=env_split)
    env = env.init_env(batch_size=1)

    def generator():
        for idx in range(n_tasks):
            obs, info = env.reset()
            obs_text = "\n".join(obs[0].split("\n\n")[1:])
            game_file = info["extra.gamefile"][0]
            yield {
                "task_id": idx,
                "game_file": game_file,
                "obs": obs_text,
                "env": env,
            }

    return generator(), n_tasks


def load_model(model_name: str, gpu: int = 0):
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map=f"cuda:{gpu}",
        trust_remote_code=True,
        torch_dtype=torch.float16,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model.eval()
    return model, tokenizer


def load_expert_icl_examples(max_per_type: int = 1, max_turns: int = 20):
    """Select short expert trajectories from SFT data, one per task type."""
    with open(SFT_DATA) as f:
        sft_data = json.load(f)

    by_type = defaultdict(list)
    for item in sft_data:
        tt = get_task_type(item["game_file"])
        convs = item["conversations"]
        # Skip the first system instruction + OK pair (index 0,1)
        # Only keep the actual interaction turns
        if len(convs) > 2:
            interaction = convs[2:]  # skip instruction + OK
        else:
            continue
        n_turns = len(interaction)
        if n_turns <= max_turns:
            by_type[tt].append((n_turns, interaction, item["game_file"]))

    # Pick shortest trajectory per type
    icl_examples = []
    for tt in ["pick_and_place", "pick_clean_then_place", "pick_heat_then_place",
               "pick_cool_then_place", "look_at_obj", "pick_two_obj"]:
        candidates = by_type.get(tt, [])
        if not candidates:
            continue
        candidates.sort(key=lambda x: x[0])
        for i in range(min(max_per_type, len(candidates))):
            n, turns, gf = candidates[i]
            # Convert from sft format to messages format
            msgs = []
            for turn in turns:
                role = "user" if turn["from"] == "human" else "assistant"
                msgs.append({"role": role, "content": turn["value"]})
            icl_examples.append(msgs)
            logger.info(f"ICL example: type={tt} turns={n} game={gf}")

    return icl_examples


def build_initial_messages(instruction: str, icl_examples: list, task_obs: str) -> list:
    messages = [
        {"role": "user", "content": instruction},
        {"role": "assistant", "content": "OK"},
    ]

    for example in icl_examples:
        for turn in example:
            messages.append({"role": turn["role"], "content": turn["content"]})

    messages.append({"role": "user", "content": task_obs})
    return messages


def generate_response(
    model, tokenizer, messages: list,
    temperature: float = 0.0, max_new_tokens: int = 256,
) -> str:
    try:
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,
        )
    except TypeError:
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )

    inputs = tokenizer(text, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=temperature > 0,
            temperature=temperature if temperature > 0 else None,
            top_p=0.9 if temperature > 0 else None,
            pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
        )

    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    response = tokenizer.decode(new_tokens, skip_special_tokens=True)
    response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
    return response


def parse_action(response: str) -> str:
    match = re.search(r"Action:\s*(.*)", response, re.DOTALL)
    if match:
        action = match.group(1).strip().split("\n")[0].strip()
        if action:
            return action
    return "look"


def run_single_task(
    task_info: dict,
    model, tokenizer,
    instruction: str, icl_examples: list,
    temperature: float = 0.0,
    max_steps: int = 40,
    max_new_tokens: int = 256,
) -> dict:
    env = task_info["env"]
    task_obs = task_info["obs"]
    game_file = task_info["game_file"]
    task_id = task_info["task_id"]
    task_type = get_task_type(game_file)

    messages = build_initial_messages(instruction, icl_examples, task_obs)

    reward = False
    steps = 0

    for _ in range(max_steps):
        response = generate_response(
            model, tokenizer, messages, temperature, max_new_tokens,
        )
        action = parse_action(response)
        messages.append({"role": "assistant", "content": response})

        try:
            observation, env_reward, env_done, info = env.step([action])
            observation = process_ob(observation[0])
            reward = info["won"][0]
            done = env_done[0]
        except Exception as e:
            logger.warning(f"Task {task_id} env.step error: {e}")
            observation = "Invalid action."
            reward = False
            done = False

        steps += 1
        messages.append({"role": "user", "content": f"Observation: {observation}"})

        if done or reward:
            break

    return {
        "task_id": task_id,
        "task_type": task_type,
        "game_file": game_file,
        "reward": bool(reward),
        "steps": steps,
        "last_action": action,
    }


def main():
    parser = argparse.ArgumentParser("ICL test with Qwen3-14B-AWQ")
    parser.add_argument("--model_name", type=str,
                        default="/root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ")
    parser.add_argument("--split", type=str, default="dev",
                        choices=["train", "dev", "test"])
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max_steps", type=int, default=40)
    parser.add_argument("--max_new_tokens", type=int, default=256)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--num_tasks", type=int, default=25)
    parser.add_argument("--icl_per_type", type=int, default=1)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    logger.info("Loading instruction...")
    with open(os.path.join(ETO_ROOT, "eval_agent/prompt/instructions/alfworld_inst.txt")) as f:
        instruction = f.read().strip()

    logger.info("Loading expert ICL examples from SFT data...")
    icl_examples = load_expert_icl_examples(
        max_per_type=args.icl_per_type, max_turns=20,
    )
    logger.info(f"Loaded {len(icl_examples)} ICL examples")

    logger.info(f"Loading model: {args.model_name}")
    model, tokenizer = load_model(args.model_name, args.gpu)

    logger.info(f"Loading ALFWorld {args.split} environment...")
    task_gen, n_tasks = load_alfworld_env(args.split)

    if args.num_tasks > 0:
        n_tasks = min(n_tasks, args.num_tasks)

    logger.info(f"Running {n_tasks} tasks...")

    results = []
    success_count = 0
    type_stats = defaultdict(lambda: {"total": 0, "success": 0})

    for i, task_info in enumerate(task_gen):
        if i >= n_tasks:
            break

        t0 = time.time()
        result = run_single_task(
            task_info, model, tokenizer,
            instruction, icl_examples,
            temperature=args.temperature,
            max_steps=args.max_steps,
            max_new_tokens=args.max_new_tokens,
        )
        elapsed = time.time() - t0

        results.append(result)
        if result["reward"]:
            success_count += 1

        ts = type_stats[result["task_type"]]
        ts["total"] += 1
        if result["reward"]:
            ts["success"] += 1

        logger.info(
            f"[{i+1}/{n_tasks}] type={result['task_type']} "
            f"reward={result['reward']} steps={result['steps']} "
            f"time={elapsed:.1f}s sr={success_count}/{i+1}"
        )

    # Summary
    total = len(results)
    sr = success_count / max(total, 1) * 100
    logger.info(f"\n{'='*60}")
    logger.info(f"OVERALL: {success_count}/{total} = {sr:.1f}%")
    logger.info(f"{'='*60}")
    for tt, stats in sorted(type_stats.items()):
        tt_sr = stats['success'] / max(stats['total'], 1) * 100
        logger.info(f"  {tt}: {stats['success']}/{stats['total']} = {tt_sr:.1f}%")
    logger.info(f"{'='*60}")
    logger.info(f"P1 GATE (>10%): {'PASS' if sr > 10 else 'FAIL'}")

    # Save results
    output_dir = Path("data/icl_test_results")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"14b_awq_{args.split}_{args.num_tasks}.json"
    with open(output_file, "w") as f:
        json.dump({
            "model": args.model_name,
            "split": args.split,
            "num_tasks": total,
            "success_rate": sr,
            "success_count": success_count,
            "type_stats": dict(type_stats),
            "results": results,
        }, f, indent=2, ensure_ascii=False)
    logger.info(f"Results saved to {output_file}")


if __name__ == "__main__":
    main()
