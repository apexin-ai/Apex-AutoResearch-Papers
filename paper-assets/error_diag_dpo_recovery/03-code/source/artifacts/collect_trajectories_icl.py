"""ALFWorld trajectory collection with ICL few-shot from expert data.

Uses Qwen3-14B-AWQ with task-type-aware ICL demonstrations sampled from
expert (SFT) trajectories. Supports dual-GPU collection via --part_num/--part_idx.

Usage:
  CUDA_VISIBLE_DEVICES=0 python src/collect_trajectories_icl.py \
    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ \
    --gpu 0 --num_tasks 300 --seed 42 \
    --part_num 2 --part_idx 0 \
    --output_dir data/trajectories_v7_icl_cuda0
"""

import os
import re
import json
import time
import random
import logging
import argparse
from pathlib import Path
from collections import defaultdict

import yaml
import torch
import alfworld
from alfworld.agents.environment import get_environment
from transformers import AutoModelForCausalLM, AutoTokenizer

logger = logging.getLogger("collect_traj_icl")

PREFIXES = {
    "pick_and_place": "put",
    "pick_clean_then_place": "clean",
    "pick_heat_then_place": "heat",
    "pick_cool_then_place": "cool",
    "look_at_obj": "examine",
    "pick_two_obj": "puttwo",
}

ALFWORLD_INSTRUCTION = (
    "Interact with a household to solve a task. Imagine you are an intelligent "
    "agent in a household environment and your target is to perform actions to "
    "complete the task goal. At the beginning of your interactions, you will be "
    "given the detailed description of the current environment and your goal to "
    "accomplish. \nFor each of your turn, you will be given the observation of "
    'the last turn. You should first think about the current condition and plan '
    'for your future actions, and then output your action in this turn. Your '
    'output must strictly follow this format:"Thought: your thoughts.\n'
    'Action: your next action".\n\n'
    "The available actions are:\n"
    "1. go to {recep}\n"
    "2. take {obj} from {recep}\n"
    "3. put {obj} in/on {recep}\n"
    "4. open {recep}\n"
    "5. close {recep}\n"
    "6. toggle {obj} {recep}\n"
    "7. clean {obj} with {recep}\n"
    "8. heat {obj} with {recep}\n"
    "9. cool {obj} with {recep}\n"
    "where {obj} and {recep} correspond to objects and receptacles.\n"
    "After your each turn, the environment will give you immediate feedback "
    'based on which you plan your next few steps. if the envrionment output '
    '"Nothing happened", that means the previous action is invalid and you '
    "should try more options.\n\n"
    "Your response should use the following format:\n\n"
    "Thought: <your thoughts>\nAction: <your next action>"
)


def get_task_type(game_file: str) -> str:
    for k in PREFIXES:
        if f"/{k}" in game_file:
            return k
    return "unknown"


def normalize_game_file(game_file: str) -> str:
    gf = game_file.rstrip("/")
    if gf.endswith("/game.tw-pddl"):
        gf = gf[: -len("/game.tw-pddl")]
    parts = gf.split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else gf


def process_ob(ob: str) -> str:
    if ob.startswith("You arrive at loc "):
        ob = ob[ob.find(". ") + 2 :]
    return ob


def load_expert_data(expert_file: str, max_turns: int = 30) -> dict[str, list]:
    with open(expert_file) as f:
        sft_data = json.load(f)

    by_type = defaultdict(list)
    for item in sft_data:
        tt = get_task_type(item["game_file"])
        convs = item["conversations"]
        if len(convs) > 2:
            interaction = convs[2:]
        else:
            continue
        n_turns = len(interaction)
        if n_turns <= max_turns:
            by_type[tt].append({
                "game_file": item["game_file"],
                "normalized_gf": normalize_game_file(item["game_file"]),
                "task_type": tt,
                "n_turns": n_turns,
                "interaction": interaction,
            })

    for tt in by_type:
        by_type[tt].sort(key=lambda x: x["n_turns"])

    total = sum(len(v) for v in by_type.values())
    logger.info("Loaded %d expert examples across %d task types", total, len(by_type))
    for tt, examples in sorted(by_type.items()):
        logger.info("  %s: %d examples", tt, len(examples))

    return dict(by_type)


def sample_icl_examples(
    expert_by_type: dict[str, list],
    task_type: str,
    exclude_game_file: str,
    num_examples: int = 2,
    rng: random.Random = None,
) -> list[list[dict]]:
    if rng is None:
        rng = random.Random(42)

    exclude_key = normalize_game_file(exclude_game_file)

    same_type = [
        ex for ex in expert_by_type.get(task_type, [])
        if ex["normalized_gf"] != exclude_key
    ]

    other_type = []
    for tt, examples in expert_by_type.items():
        if tt == task_type:
            continue
        for ex in examples:
            if ex["normalized_gf"] != exclude_key:
                other_type.append(ex)
    other_type.sort(key=lambda x: x["n_turns"])

    selected = []
    if len(same_type) >= num_examples:
        selected = rng.sample(same_type, num_examples)
    else:
        selected = list(same_type)
        remaining = num_examples - len(selected)
        if remaining > 0 and other_type:
            supplement = other_type[:remaining]
            selected.extend(supplement)

    icl_messages = []
    for ex in selected:
        msgs = []
        for turn in ex["interaction"]:
            role = "user" if turn["from"] == "human" else "assistant"
            msgs.append({"role": role, "content": turn["value"]})
        icl_messages.append(msgs)

    return icl_messages


def load_alfworld_env(split: str, part_num: int = 1, part_idx: int = -1):
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
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map=f"cuda:{gpu}",
        trust_remote_code=True,
        torch_dtype=torch.float16,
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model.eval()
    return model, tokenizer


def build_icl_messages(
    instruction: str, icl_examples: list[list[dict]], task_obs: str,
) -> list:
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
    temperature: float = 0.7, max_new_tokens: int = 2048,
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
    response = re.sub(r"<think>.*?(?:</think>|$)", "", response, flags=re.DOTALL).strip()
    return response


def translate_action(action: str) -> str:
    """Translate put variants to 'move X to Y' for TextWorld 1.7.0."""
    m = re.match(r"put (.+?) (?:in/on|on|in) (?:the )?(.+)", action, re.IGNORECASE)
    if m:
        return f"move {m.group(1)} to {m.group(2)}"
    return action


def parse_action(response: str) -> str:
    match = re.search(r"Action:\s*(.*)", response, re.DOTALL)
    if match:
        action = match.group(1).strip().split("\n")[0].strip()
        if action:
            return translate_action(action)
    return "look"


def collect_single_trajectory(
    task_info: dict,
    model, tokenizer,
    expert_by_type: dict,
    num_icl_examples: int = 2,
    temperature: float = 0.7,
    max_steps: int = 40,
    max_new_tokens: int = 256,
    rng: random.Random = None,
) -> dict:
    env = task_info["env"]
    task_obs = task_info["obs"]
    game_file = task_info["game_file"]
    task_id = task_info["task_id"]
    task_type = get_task_type(game_file)

    icl_examples = sample_icl_examples(
        expert_by_type, task_type, game_file,
        num_examples=num_icl_examples, rng=rng,
    )

    messages = build_icl_messages(ALFWORLD_INSTRUCTION, icl_examples, task_obs)

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
            logger.warning("Task %d env.step error: %s", task_id, e)
            observation = "Invalid action."
            reward = False
            done = False

        # Episode boundary detection: ALFWorld auto-resets on task completion,
        # returning the NEW episode's done/won=False instead of the completed one's True.
        if not reward and not done and steps > 0:
            if observation.startswith("You are in the middle of a room") or \
               "Your task is to:" in observation:
                logger.info("Task %d: episode boundary detected at step %d (auto-reset)", task_id, steps)
                reward = True
                done = True

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
    parser = argparse.ArgumentParser("Collect ALFWorld trajectories with ICL few-shot")
    parser.add_argument("--model_name", type=str,
                        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-14B-AWQ")
    parser.add_argument("--expert_file", type=str,
                        default="data/alfworld_sft.json")
    parser.add_argument("--output_dir", type=str, default="data/trajectories")
    parser.add_argument("--split", type=str, default="train",
                        choices=["train", "dev", "test"])
    parser.add_argument("--temperature", type=float, default=0.5)
    parser.add_argument("--max_steps", type=int, default=40)
    parser.add_argument("--max_new_tokens", type=int, default=256)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--num_tasks", type=int, default=-1, help="-1 = all tasks")
    parser.add_argument("--num_icl_examples", type=int, default=2)
    parser.add_argument("--part_num", type=int, default=1)
    parser.add_argument("--part_idx", type=int, default=-1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--dry_run", action="store_true",
                        help="Validate pipeline with 2 tasks then exit")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    rng = random.Random(args.seed)
    torch.manual_seed(args.seed)

    logger.info("Loading expert data from %s...", args.expert_file)
    expert_by_type = load_expert_data(args.expert_file)

    logger.info("Loading model: %s", args.model_name)
    model, tokenizer = load_model(args.model_name, args.gpu)

    logger.info("Loading ALFWorld %s environment...", args.split)
    task_gen, n_tasks = load_alfworld_env(args.split, args.part_num, args.part_idx)

    if args.dry_run:
        n_tasks = min(2, n_tasks)
        logger.info("DRY RUN: collecting %d tasks only", n_tasks)
    elif args.num_tasks > 0:
        n_tasks = min(n_tasks, args.num_tasks)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = f"_part{args.part_idx}" if args.part_num > 1 else ""
    output_file = output_dir / f"{args.split}{suffix}.jsonl"

    logger.info("Collecting %d trajectories -> %s", n_tasks, output_file)
    logger.info("ICL examples per task: %d", args.num_icl_examples)

    success_count = 0
    total_count = 0

    with open(output_file, "w") as f:
        for i, task_info in enumerate(task_gen):
            if i >= n_tasks:
                break

            t0 = time.time()
            traj = collect_single_trajectory(
                task_info, model, tokenizer,
                expert_by_type,
                num_icl_examples=args.num_icl_examples,
                temperature=args.temperature,
                max_steps=args.max_steps,
                max_new_tokens=args.max_new_tokens,
                rng=rng,
            )
            elapsed = time.time() - t0

            total_count += 1
            if traj["reward"]:
                success_count += 1

            f.write(json.dumps(traj, ensure_ascii=False) + "\n")
            f.flush()

            logger.info(
                "[%d/%d] task=%d type=%s reward=%s steps=%d time=%.1fs sr=%d/%d",
                total_count, n_tasks, traj["task_id"],
                traj["task_type"], traj["reward"],
                traj["steps"], elapsed,
                success_count, total_count,
            )

    logger.info(
        "Done. %d/%d succeeded (%.1f%%)",
        success_count, total_count,
        success_count / max(total_count, 1) * 100,
    )


if __name__ == "__main__":
    main()
