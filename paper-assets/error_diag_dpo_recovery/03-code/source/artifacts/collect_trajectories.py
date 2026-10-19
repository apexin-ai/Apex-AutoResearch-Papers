"""ALFWorld trajectory collection with Qwen3-8B direct inference.

Usage:
  python src/collect_trajectories.py \
    --model_name /root/autodl-tmp/.hf_cache/Qwen3-8B \
    --output_dir data/trajectories \
    --split train \
    --temperature 0.7 \
    --max_steps 40 \
    --gpu 0 \
    --num_tasks 100
"""

import os
import re
import json
import time
import logging
import argparse
from pathlib import Path

import yaml
import torch
import alfworld
from alfworld.agents.environment import get_environment
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

logger = logging.getLogger("collect_traj")

PREFIXES = {
    "pick_and_place": "put",
    "pick_clean_then_place": "clean",
    "pick_heat_then_place": "heat",
    "pick_cool_then_place": "cool",
    "look_at_obj": "examine",
    "pick_two_obj": "puttwo",
}

ETO_ROOT = "/root/autodl-tmp/rl-active-probe-fl/eto_repo"


def get_task_type(game_file: str) -> str:
    for k in PREFIXES:
        if f"/{k}" in game_file:
            return k
    return "unknown"


def process_ob(ob: str) -> str:
    if ob.startswith("You arrive at loc "):
        ob = ob[ob.find(". ") + 2 :]
    return ob


def load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):
    """Load ALFWorld environment. Returns (generator, n_tasks)."""
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

    if part_num > 1:
        assert part_idx >= 0
        part_sizes = [n_tasks // part_num] * part_num
        part_sizes[-1] += n_tasks % part_num
        env.skip(sum(part_sizes[:part_idx]))
        n_tasks = part_sizes[part_idx]

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
    """Load model with 4-bit quantization."""
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map=f"cuda:{gpu}",
        trust_remote_code=True,
        dtype=torch.bfloat16,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model.eval()
    return model, tokenizer


def load_prompt_resources():
    """Load instruction and ICL examples from ETO repo."""
    with open(os.path.join(ETO_ROOT, "eval_agent/prompt/instructions/alfworld_inst.txt")) as f:
        instruction = f.read().strip()
    with open(os.path.join(ETO_ROOT, "eval_agent/prompt/icl_examples/alfworld_icl.json")) as f:
        icl_examples = json.load(f)
    return instruction, icl_examples


def build_initial_messages(instruction: str, icl_examples: list, task_obs: str) -> list:
    """Build initial conversation with ICL examples in 'conversation' format.

    Mirrors ETO's prompt_with_icl with icl_format='conversation'.
    """
    messages = [
        {"role": "user", "content": instruction},
        {"role": "assistant", "content": "OK"},
    ]

    for example in icl_examples:
        for j, turn in enumerate(example):
            content = turn["content"]
            if j % 2 == 0:
                messages.append({"role": "user", "content": content})
            else:
                messages.append({"role": "assistant", "content": content})

    messages.append({"role": "user", "content": task_obs})
    return messages


def generate_response(
    model, tokenizer, messages: list,
    temperature: float = 0.7, max_new_tokens: int = 256,
) -> str:
    """Generate response. Disables Qwen3 thinking mode for clean output."""
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

    # Strip any <think>...</think> blocks if present
    response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
    return response


def parse_action(response: str) -> str:
    """Extract action from 'Thought: ...\\nAction: ...' format."""
    match = re.search(r"Action:\s*(.*)", response, re.DOTALL)
    if match:
        action = match.group(1).strip().split("\n")[0].strip()
        if action:
            return action
    return "look"


def collect_single_trajectory(
    task_info: dict,
    model, tokenizer,
    instruction: str, icl_examples: list,
    temperature: float = 0.7,
    max_steps: int = 40,
    max_new_tokens: int = 256,
) -> dict:
    """Run one episode and return the trajectory."""
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
        "conversations": messages,
    }


def main():
    parser = argparse.ArgumentParser("Collect ALFWorld trajectories")
    parser.add_argument("--model_name", type=str, default="/root/autodl-tmp/.hf_cache/Qwen3-8B")
    parser.add_argument("--output_dir", type=str, default="data/trajectories")
    parser.add_argument("--split", type=str, default="train", choices=["train", "dev", "test"])
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--max_steps", type=int, default=40)
    parser.add_argument("--max_new_tokens", type=int, default=256)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--num_tasks", type=int, default=-1, help="-1 = all tasks")
    parser.add_argument("--part_num", type=int, default=1)
    parser.add_argument("--part_idx", type=int, default=-1)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    logger.info("Loading prompt resources...")
    instruction, icl_examples = load_prompt_resources()

    logger.info(f"Loading model: {args.model_name}")
    model, tokenizer = load_model(args.model_name, args.gpu)

    logger.info(f"Loading ALFWorld {args.split} environment...")
    task_gen, n_tasks = load_alfworld_env(args.split, args.part_num, args.part_idx)

    if args.num_tasks > 0:
        n_tasks = min(n_tasks, args.num_tasks)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = f"_part{args.part_idx}" if args.part_num > 1 else ""
    output_file = output_dir / f"{args.split}{suffix}.jsonl"

    logger.info(f"Collecting {n_tasks} trajectories -> {output_file}")

    success_count = 0
    total_count = 0

    with open(output_file, "w") as f:
        for i, task_info in enumerate(task_gen):
            if i >= n_tasks:
                break

            t0 = time.time()
            traj = collect_single_trajectory(
                task_info, model, tokenizer,
                instruction, icl_examples,
                temperature=args.temperature,
                max_steps=args.max_steps,
                max_new_tokens=args.max_new_tokens,
            )
            elapsed = time.time() - t0

            total_count += 1
            if traj["reward"]:
                success_count += 1

            f.write(json.dumps(traj, ensure_ascii=False) + "\n")
            f.flush()

            logger.info(
                f"[{total_count}/{n_tasks}] task={traj['task_id']} "
                f"type={traj['task_type']} reward={traj['reward']} "
                f"steps={traj['steps']} time={elapsed:.1f}s "
                f"sr={success_count}/{total_count}"
            )

    logger.info(
        f"Done. {success_count}/{total_count} succeeded "
        f"({success_count / max(total_count, 1) * 100:.1f}%)"
    )


if __name__ == "__main__":
    main()
