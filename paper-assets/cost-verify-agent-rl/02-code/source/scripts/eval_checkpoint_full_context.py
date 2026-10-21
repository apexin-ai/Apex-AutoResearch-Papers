#!/usr/bin/env python3
"""Post-hoc evaluation of h-sweep checkpoints with full context window.

Evaluates trained checkpoints using multi-turn messages matching RAGEN's
context_window_mode=full, to isolate credit assignment effects from
inference-time context truncation.

Usage:
    # Single checkpoint
    python eval_checkpoint_full_context.py --ckpt_path /path/to/global_step_N/

    # Batch mode: all checkpoints in a run directory
    python eval_checkpoint_full_context.py --run_dir /root/autodl-tmp/checkpoints/hsweep-h2/

    # Output: JSON per checkpoint with success_rate, action_is_valid_rate, etc.
"""

import multiprocessing
multiprocessing.set_start_method('spawn', force=True)

import argparse
import json
import os
import random
import re
import shutil
import sys
import time
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "RAGEN"))
from ragen.env.alfworld.env import AlfredTXTEnv
from ragen.env.alfworld.config import AlfredEnvConfig

from vllm import LLM, SamplingParams

# --- AlfworldSG env_instruction (from config/envs.yaml) ---
ENV_INSTRUCTION = (
    "You are an expert agent in the ALFRED Embodied Environment.\n"
    "Complete household tasks by navigating and interacting with objects.\n\n"
    "Before each action, you MUST first produce a self-guidance assessment in your reasoning:\n"
    "[Assessment: positive/neutral/negative] - evaluate your current progress toward the task goal.\n"
    "[Reasoning: one sentence analyzing what has been accomplished and what remains.]\n"
    "[Suggestion: the best next action from admissible actions.]\n\n"
    "Your reasoning MUST be enclosed within <think> </think> tags.\n"
    "After the closing </think> tag, wrap your chosen action in <answer> </answer> tags.\n"
    "The action must be a precise ALFWorld command from the admissible actions list "
    "(e.g. go to desk 1, pick up pen 2, open drawer 1).\n"
    "Do NOT output natural language descriptions or anything after the </answer> tag.\n\n"
    "Example: <think>[Assessment: neutral] I need to find a pen. The desk is a likely location. "
    "[Suggestion: go to desk 1]</think><answer>go to desk 1</answer>\n"
)

SYSTEM_PROMPT = "You're a helpful assistant. " + ENV_INSTRUCTION
FORMAT_PROMPT = "<think> [Your thoughts] </think> <answer> [your answer] </answer>"
LENGTH_PROMPT = "Max response length: 512 words (tokens)."
MAX_ACTIONS_PER_TRAJ = 50
MAX_PROMPT_TOKENS = 30000

TASK_TYPE_MAP = {
    "pick_and_place_simple": "put",
    "pick_two_obj_and_place": "put",
    "pick_heat_then_place_in_recep": "heat",
    "pick_cool_then_place_in_recep": "cool",
    "pick_clean_then_place_in_recep": "clean",
    "look_at_obj_in_light": "examine",
}


def build_turn_state_content(state: str, turn_number: int, actions_left: int,
                             invalid_action: bool = False) -> str:
    """Build state content for a single turn, matching RAGEN ctx_manager._build_turn_state_content."""
    warning = ""
    if invalid_action:
        warning = "No valid action provided previously. Environment state remains the same. Please try again.\n"
    content = f"\nTurn {turn_number}:\n"
    content += (
        f"State:\n{state}\n{warning}"
        f"You have {actions_left} actions left. Always output: {FORMAT_PROMPT} "
        f"with no extra text. Strictly follow this format. {LENGTH_PROMPT}\n"
    )
    return content


def parse_action(response: str) -> Tuple[str, bool, bool]:
    has_think = bool(re.search(r"<think>.*?</think>", response, re.DOTALL))
    m = re.search(r"<think>.*?</think>\s*<answer>(.*?)</answer>", response, re.DOTALL)
    if m:
        return m.group(1).strip(), has_think, True
    m = re.search(r"</think>\s*(.*)", response, re.DOTALL)
    if m:
        action = m.group(1).strip().split("\n")[0].strip()
        for tok in ["<|im_end|>", "<|endoftext|>"]:
            action = action.replace(tok, "").strip()
        if action:
            return action, has_think, False
    return "", has_think, False


def get_task_type(game_file: str) -> str:
    if not game_file:
        return "unknown"
    for prefix, ttype in TASK_TYPE_MAP.items():
        if prefix in game_file:
            return ttype
    return "unknown"


def truncate_messages(messages: List[Dict], tokenizer, max_tokens: int) -> List[Dict]:
    """Truncate multi-turn messages by removing oldest turns (keeping system + latest)."""
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    token_count = len(tokenizer.encode(text))
    if token_count <= max_tokens:
        return messages

    # Remove oldest user/assistant pairs (keep system at [0] and latest user at [-1])
    while token_count > max_tokens and len(messages) > 3:
        # Remove messages[1] and messages[2] (oldest user + assistant pair)
        messages = [messages[0]] + messages[3:]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        token_count = len(tokenizer.encode(text))

    return messages


def run_episode(llm, sampling_params, tokenizer, env, episode_idx: int,
                max_steps: int = 50) -> Tuple[List[Dict], str]:
    """Run one episode with full-context multi-turn messages (RAGEN context_window_mode=full)."""
    random.seed(episode_idx)
    np.random.seed(episode_idx)

    obs = env.reset(seed=episode_idx, mode="val")
    game_file = getattr(env, "current_game_file", "")
    task_type = get_task_type(game_file)

    # Multi-turn message history (grows each step)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": ""},
    ]

    steps = []
    prev_invalid = False

    for step_i in range(max_steps):
        actions_left = max_steps - step_i
        turn_number = step_i + 1

        # Append current turn's state to the last user message
        state_content = build_turn_state_content(obs, turn_number, actions_left, prev_invalid)
        messages[-1]["content"] += state_content

        # Truncate if too long (remove oldest turns)
        msgs = truncate_messages(list(messages), tokenizer, MAX_PROMPT_TOKENS)
        text = tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
        text += "<think>"

        outputs = llm.generate([text], sampling_params, use_tqdm=False)
        response = "<think>" + outputs[0].outputs[0].text
        clean_response = response.replace("<|im_end|>", "").replace("<|endoftext|>", "").strip()
        action, has_think, has_answer = parse_action(clean_response)
        format_ok = has_think and (has_answer or bool(action))
        action_is_valid = action in env.available_actions if action else False

        step_info = {
            "step": step_i,
            "action": action,
            "has_think": has_think,
            "has_answer": has_answer,
            "format_ok": format_ok,
            "action_is_valid": action_is_valid,
            "action_is_effective": False,
        }

        if not action:
            step_info["success"] = False
            step_info["done"] = True
            step_info["reward"] = 0.0
            steps.append(step_info)
            break

        obs_before = obs
        obs, reward, done, info = env.step(action)
        step_info["reward"] = reward
        step_info["success"] = info.get("success", False)
        step_info["done"] = done
        step_info["action_is_effective"] = info.get("action_is_effective", False)
        steps.append(step_info)

        prev_invalid = not action_is_valid

        if done:
            break

        # Build multi-turn continuation:
        # 1. Add assistant response
        messages.append({"role": "assistant", "content": clean_response})
        # 2. Add new user message with reward + (next state will be appended at top of loop)
        messages.append({"role": "user", "content": f"Reward:\n{reward}\n"})

    return steps, task_type


# --- Checkpoint handling (reused from eval_checkpoint.py) ---

def detect_checkpoint_format(path: str) -> str:
    if os.path.isfile(os.path.join(path, "config.json")):
        if (os.path.isfile(os.path.join(path, "model.safetensors"))
                or any(f.startswith("model-") and f.endswith(".safetensors") for f in os.listdir(path))
                or os.path.isfile(os.path.join(path, "pytorch_model.bin"))):
            return "hf"
    actor_dir = os.path.join(path, "actor")
    if os.path.isdir(actor_dir) and os.path.isfile(os.path.join(actor_dir, "fsdp_config.json")):
        return "fsdp"
    if os.path.isfile(os.path.join(path, "fsdp_config.json")):
        return "fsdp"
    raise ValueError(
        f"Cannot detect checkpoint format at {path}. "
        f"Expected HF (config.json + model.safetensors) or FSDP (actor/fsdp_config.json)."
    )


def convert_fsdp_to_hf(fsdp_dir: str, output_dir: str, dtype_str: str = "bf16") -> str:
    import torch
    from accelerate import init_empty_weights
    from transformers import AutoConfig, AutoModelForCausalLM

    dtype_map = {"bf16": torch.bfloat16, "fp16": torch.float16, "fp32": torch.float32}
    target_dtype = dtype_map[dtype_str]

    actor_dir = fsdp_dir
    if os.path.isdir(os.path.join(fsdp_dir, "actor")):
        actor_dir = os.path.join(fsdp_dir, "actor")

    fsdp_config_path = os.path.join(actor_dir, "fsdp_config.json")
    with open(fsdp_config_path) as f:
        fsdp_config = json.load(f)
    world_size = fsdp_config["world_size"]

    hf_dir = os.path.join(actor_dir, "huggingface")
    if not os.path.isdir(hf_dir):
        raise FileNotFoundError(f"huggingface/ subdirectory not found in {actor_dir}")

    print(f"  Converting FSDP checkpoint (world_size={world_size}) -> HF ...", flush=True)
    shards = []
    for rank in range(world_size):
        p = os.path.join(actor_dir, f"model_world_size_{world_size}_rank_{rank}.pt")
        shards.append(torch.load(p, map_location="cpu", weights_only=False))

    full_state_dict = {}
    for key in list(shards[0].keys()):
        local_tensors = []
        shard_dim = 0
        for rank in range(world_size):
            dt = shards[rank][key]
            if hasattr(dt, "placements") and len(dt.placements) > 0:
                shard_dim = dt.placements[0].dim
            lt = dt._local_tensor if hasattr(dt, "_local_tensor") else dt.to_local()
            local_tensors.append(lt)
        full_state_dict[key] = torch.cat(local_tensors, dim=shard_dim).to(target_dtype)
    del shards

    config = AutoConfig.from_pretrained(hf_dir)
    with init_empty_weights():
        model = AutoModelForCausalLM.from_config(config, dtype=target_dtype)
    model.to_empty(device="cpu")

    os.makedirs(output_dir, exist_ok=True)
    model.save_pretrained(output_dir, state_dict=full_state_dict, max_shard_size="5GB")
    del full_state_dict, model

    for fname in os.listdir(hf_dir):
        src = os.path.join(hf_dir, fname)
        dst = os.path.join(output_dir, fname)
        if not os.path.exists(dst):
            shutil.copy2(src, dst)

    print(f"  Converted to {output_dir}", flush=True)
    return output_dir


def discover_checkpoints(run_dir: str) -> List[Tuple[int, str]]:
    """Discover all global_step_N checkpoints in a run directory. Returns sorted (step, path) list."""
    checkpoints = []
    for entry in os.listdir(run_dir):
        m = re.match(r"global_step_(\d+)$", entry)
        if m:
            step = int(m.group(1))
            path = os.path.join(run_dir, entry)
            if os.path.isdir(path):
                checkpoints.append((step, path))
    checkpoints.sort()
    return checkpoints


def resolve_model_path(ckpt_path: str, fsdp_convert_dir: Optional[str] = None) -> Tuple[str, str]:
    """Detect format and convert if needed. Returns (model_path, format)."""
    fmt = detect_checkpoint_format(ckpt_path)
    if fmt == "fsdp":
        convert_dir = fsdp_convert_dir or (ckpt_path.rstrip("/") + "_hf")
        if os.path.isfile(os.path.join(convert_dir, "config.json")):
            print(f"  Using existing HF conversion at {convert_dir}", flush=True)
            return convert_dir, fmt
        return convert_fsdp_to_hf(ckpt_path, convert_dir), fmt
    return ckpt_path, fmt


def evaluate_checkpoint(ckpt_path: str, args, env=None, llm_cache=None):
    """Evaluate a single checkpoint. Returns summary dict."""
    print(f"\n{'='*60}", flush=True)
    print(f"Evaluating: {ckpt_path}", flush=True)
    print(f"{'='*60}", flush=True)

    start_time = time.time()
    model_path, fmt = resolve_model_path(ckpt_path, args.fsdp_convert_dir)

    # Reuse LLM if model_path matches cached one
    if llm_cache and llm_cache.get("model_path") == model_path:
        llm = llm_cache["llm"]
        tokenizer = llm_cache["tokenizer"]
        print(f"  Reusing loaded model from {model_path}", flush=True)
    else:
        print(f"  Loading model from {model_path} ...", flush=True)
        llm = LLM(
            model=model_path,
            tensor_parallel_size=1,
            gpu_memory_utilization=args.gpu_memory_utilization,
            max_model_len=20480,
            enforce_eager=True,
            trust_remote_code=True,
            enable_prefix_caching=True,
        )
        tokenizer = llm.get_tokenizer()
        if llm_cache is not None:
            llm_cache["llm"] = llm
            llm_cache["tokenizer"] = tokenizer
            llm_cache["model_path"] = model_path

    sampling_params = SamplingParams(
        temperature=args.temperature,
        top_p=0.95,
        max_tokens=1024,
        stop=["<|im_end|>", "<|endoftext|>"],
    )
    load_time = time.time() - start_time
    print(f"  Model ready in {load_time:.1f}s", flush=True)

    if env is None:
        os.environ.setdefault("ALFWORLD_DATA", "/root/autodl-tmp/alfworld")
        ragen_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "RAGEN")
        alfworld_cfg = os.path.join(ragen_root, "ragen", "env", "alfworld", "alfworld_config.yaml")
        env_config = AlfredEnvConfig(config_file=alfworld_cfg, eval_dataset="eval_in_distribution")
        env = AlfredTXTEnv(config=env_config, mode="val")

    ep_results = []
    eval_start = time.time()

    for ep_i in range(1, args.num_episodes + 1):
        ep_start = time.time()
        steps, task_type = run_episode(
            llm, sampling_params, tokenizer, env,
            episode_idx=ep_i - 1,
            max_steps=args.max_steps,
        )
        ep_time = time.time() - ep_start

        total_steps = len(steps)
        valid_actions = sum(1 for s in steps if s["action_is_valid"])
        effective_actions = sum(1 for s in steps if s["action_is_effective"])
        format_ok_count = sum(1 for s in steps if s["format_ok"])
        success = any(s.get("success", False) for s in steps)

        result = {
            "episode": ep_i,
            "task_type": task_type,
            "total_steps": total_steps,
            "success": success,
            "action_is_valid_rate": valid_actions / total_steps if total_steps > 0 else 0,
            "action_is_effective_rate": effective_actions / total_steps if total_steps > 0 else 0,
            "format_ok_rate": format_ok_count / total_steps if total_steps > 0 else 0,
            "time_seconds": round(ep_time, 1),
            "steps": steps,
        }
        ep_results.append(result)

        status = "SUCCESS" if success else "FAIL"
        print(
            f"  EP {ep_i:>2}/{args.num_episodes}: {status} | "
            f"steps={total_steps:2d} "
            f"valid={valid_actions}/{total_steps} "
            f"effective={effective_actions}/{total_steps} "
            f"fmt={format_ok_count}/{total_steps} "
            f"type={task_type} "
            f"({ep_time:.1f}s)",
            flush=True,
        )

    eval_time = time.time() - eval_start
    total_time = time.time() - start_time

    n = len(ep_results)
    success_rate = sum(1 for r in ep_results if r["success"]) / n
    avg_valid = np.mean([r["action_is_valid_rate"] for r in ep_results])
    avg_effective = np.mean([r["action_is_effective_rate"] for r in ep_results])
    avg_format = np.mean([r["format_ok_rate"] for r in ep_results])
    avg_steps = np.mean([r["total_steps"] for r in ep_results])

    print("\n" + "=" * 60, flush=True)
    print(f"RESULTS ({n} episodes, context_window_mode=full)", flush=True)
    print("=" * 60, flush=True)
    print(f"  success_rate           : {success_rate:.1%} ({sum(1 for r in ep_results if r['success'])}/{n})", flush=True)
    print(f"  action_is_valid rate   : {avg_valid:.1%}", flush=True)
    print(f"  action_is_effective rate: {avg_effective:.1%}", flush=True)
    print(f"  format_ok rate         : {avg_format:.1%}", flush=True)
    print(f"  avg_steps/episode      : {avg_steps:.1f}", flush=True)
    print(f"  eval time              : {eval_time:.1f}s ({eval_time/n:.1f}s/episode)", flush=True)
    print("=" * 60, flush=True)

    type_stats = defaultdict(lambda: {"count": 0, "success": 0})
    for r in ep_results:
        tt = r.get("task_type", "unknown")
        type_stats[tt]["count"] += 1
        if r["success"]:
            type_stats[tt]["success"] += 1

    # Extract step number from path
    step_match = re.search(r"global_step_(\d+)", ckpt_path)
    checkpoint_step = int(step_match.group(1)) if step_match else -1

    summary = {
        "checkpoint_path": ckpt_path,
        "model_path": model_path,
        "checkpoint_format": fmt,
        "checkpoint_step": checkpoint_step,
        "context_window_mode": "full",
        "num_episodes": n,
        "temperature": args.temperature,
        "max_steps": args.max_steps,
        "c003_compliant": n >= 16,
        "success_rate": round(success_rate, 4),
        "action_is_valid_rate": round(float(avg_valid), 4),
        "action_is_effective_rate": round(float(avg_effective), 4),
        "format_ok_rate": round(float(avg_format), 4),
        "avg_steps": round(float(avg_steps), 1),
        "eval_time_seconds": round(eval_time, 1),
        "total_time_seconds": round(total_time, 1),
        "per_task_type": {tt: dict(s) for tt, s in type_stats.items()},
        "episodes": ep_results,
    }

    return summary, env


def main():
    parser = argparse.ArgumentParser(
        description="Post-hoc eval with full context window (multi-turn messages)."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--ckpt_path",
                       help="Path to a single checkpoint (HF dir or FSDP global_step dir)")
    group.add_argument("--run_dir",
                       help="Path to run directory containing global_step_N/ subdirs")

    parser.add_argument("--num_episodes", type=int, default=32,
                        help="Number of eval episodes (C003: >=16, default 32)")
    parser.add_argument("--max_steps", type=int, default=50,
                        help="Max steps per episode (default 50)")
    parser.add_argument("--temperature", type=float, default=0.4,
                        help="Sampling temperature (default 0.4)")
    parser.add_argument("--output_dir", default="/root/autodl-tmp/eval_results/full_context/",
                        help="Directory for JSON result files")
    parser.add_argument("--gpu", type=int, default=0,
                        help="GPU index (default 0)")
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.35,
                        help="vLLM GPU memory utilization (default 0.35)")
    parser.add_argument("--fsdp_convert_dir", default=None,
                        help="Where to save converted HF models (default: <ckpt>_hf)")
    parser.add_argument("--dry_run", action="store_true",
                        help="Only discover checkpoints, don't run eval")
    args = parser.parse_args()

    if args.num_episodes < 16:
        print(f"ERROR: C003 requires >=16 episodes, got {args.num_episodes}. Aborting.", flush=True)
        sys.exit(1)

    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    # Determine checkpoint list
    if args.run_dir:
        checkpoints = discover_checkpoints(args.run_dir)
        if not checkpoints:
            print(f"ERROR: No global_step_N directories found in {args.run_dir}", flush=True)
            sys.exit(1)
        print(f"Discovered {len(checkpoints)} checkpoints in {args.run_dir}:", flush=True)
        for step, path in checkpoints:
            print(f"  step {step}: {path}", flush=True)
        if args.dry_run:
            return
    else:
        ckpt = os.path.abspath(args.ckpt_path)
        step_match = re.search(r"global_step_(\d+)", ckpt)
        step = int(step_match.group(1)) if step_match else 0
        checkpoints = [(step, ckpt)]
        if args.dry_run:
            print(f"Checkpoint: {ckpt} (step {step})", flush=True)
            return

    os.makedirs(args.output_dir, exist_ok=True)
    all_summaries = []
    env = None
    llm_cache = {}

    for step, ckpt_path in checkpoints:
        summary, env = evaluate_checkpoint(ckpt_path, args, env=env, llm_cache=llm_cache)
        all_summaries.append(summary)

        # Save individual result
        run_name = os.path.basename(os.path.dirname(ckpt_path).rstrip("/"))
        if not run_name or run_name == "checkpoints":
            run_name = "single"
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        fname = f"fullctx_{run_name}_step{step}_{args.num_episodes}ep_{timestamp}.json"
        out_path = os.path.join(args.output_dir, fname)
        with open(out_path, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"Saved: {out_path}", flush=True)

        # Must reload model for different checkpoints
        if len(checkpoints) > 1:
            llm_cache.clear()

    # Batch summary
    if len(all_summaries) > 1:
        batch_summary = {
            "run_dir": args.run_dir,
            "context_window_mode": "full",
            "num_episodes_per_checkpoint": args.num_episodes,
            "temperature": args.temperature,
            "checkpoints": [
                {
                    "step": s["checkpoint_step"],
                    "success_rate": s["success_rate"],
                    "action_is_valid_rate": s["action_is_valid_rate"],
                    "action_is_effective_rate": s["action_is_effective_rate"],
                    "format_ok_rate": s["format_ok_rate"],
                    "avg_steps": s["avg_steps"],
                }
                for s in all_summaries
            ],
        }
        run_name = os.path.basename(args.run_dir.rstrip("/"))
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        batch_path = os.path.join(args.output_dir, f"fullctx_{run_name}_batch_{timestamp}.json")
        with open(batch_path, "w") as f:
            json.dump(batch_summary, f, indent=2)
        print(f"\nBatch summary saved: {batch_path}", flush=True)

        print("\n" + "=" * 70, flush=True)
        print("BATCH RESULTS (full context eval)", flush=True)
        print("=" * 70, flush=True)
        print(f"  {'Step':>6}  {'Success':>8}  {'Valid':>8}  {'Effective':>10}  {'Format':>8}  {'AvgSteps':>8}", flush=True)
        print(f"  {'------':>6}  {'-------':>8}  {'-----':>8}  {'---------':>10}  {'------':>8}  {'--------':>8}", flush=True)
        for s in batch_summary["checkpoints"]:
            print(
                f"  {s['step']:>6}  {s['success_rate']:>7.1%}  {s['action_is_valid_rate']:>7.1%}  "
                f"{s['action_is_effective_rate']:>9.1%}  {s['format_ok_rate']:>7.1%}  {s['avg_steps']:>8.1f}",
                flush=True,
            )
        print("=" * 70, flush=True)

    if env is not None:
        env.close()


if __name__ == "__main__":
    main()
