"""
A1 VLA baseline evaluation on LIBERO.
Standalone script — no tensorflow dependency.

Usage:
  CUDA_VISIBLE_DEVICES=0 python eval_a1_baseline.py \
      --benchmark object --n_rollouts 20 --seed 42 \
      --checkpoint /root/autodl-tmp/models/a1-libero/
"""
import argparse
import functools
builtins_print = print
print = functools.partial(builtins_print, flush=True)
import os
os.environ.setdefault("DATA_DIR", "/tmp")
os.environ.setdefault("VLA_CONFIG_YAML", "libero_simulation.yaml")
import sys
import json
import time
import traceback
from collections import deque
from pathlib import Path

import torch
import numpy as np
from PIL import Image
from robosuite.utils.transform_utils import quat2axisangle

from a1.vla.affordvla import AffordVLA
from a1.config import ModelConfig
from a1.util import resource_path
from a1.data import build_mm_preprocessor
from a1.data.collator import MMCollatorForAction
from a1.vla.constants import NormalizationType

from libero.libero import benchmark

from transformers.cache_utils import DynamicCache
if not hasattr(DynamicCache, "from_legacy_cache"):
    @classmethod
    def _from_legacy_cache(cls, past_key_values):
        cache = cls()
        if past_key_values is not None:
            for layer_idx, (key, value) in enumerate(past_key_values):
                cache.update(key, value, layer_idx)
        return cache
    DynamicCache.from_legacy_cache = _from_legacy_cache

SUITE_MAX_STEPS = {"object": 280, "spatial": 280, "goal": 300, "long": 520, "90": 400}
SUITE_TO_LIBERO = {
    "object": "libero_object",
    "spatial": "libero_spatial",
    "goal": "libero_goal",
    "long": "libero_10",
    "90": "libero_90",
}
UNNORM_KEY_MAP = {
    "object": "libero_object_no_noops",
    "spatial": "libero_spatial_no_noops",
    "goal": "libero_goal_no_noops",
    "long": "libero_10_no_noops",
    "90": "libero_90_no_noops",
}
NUM_OPEN_LOOP_STEPS = 8
NUM_STEPS_WAIT = 10
NORMALIZATION_TYPE = NormalizationType.BOUNDS_Q99


def set_seed(seed):
    import random
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    os.environ["PYTHONHASHSEED"] = str(seed)


def load_a1_model(checkpoint_path, device, tokenizer_path=None):
    cfg_path = resource_path(Path(checkpoint_path), "config.yaml")
    model_cfg = ModelConfig.load(cfg_path, key="model", validate_paths=False)
    model_cfg.num_diffusion_inference_steps = 10
    model_cfg.llm_causal_attention = False

    if tokenizer_path:
        model_cfg.tokenizer.identifier = tokenizer_path

    model = AffordVLA(model_cfg)
    state_dict_path = resource_path(Path(checkpoint_path), "model.pt")
    state_dict = torch.load(str(state_dict_path), map_location="cpu")
    model.load_state_dict(state_dict, strict=True)
    del state_dict
    torch.cuda.empty_cache()

    model = model.to(torch.bfloat16)
    model.to(device)
    model.eval()
    print(f"[a1] Model loaded, params={model.num_params():,d}, device={device}")
    return model


def load_norm_stats(checkpoint_path):
    stats_path = os.path.join(checkpoint_path, "dataset_statistics.json")
    with open(stats_path) as f:
        return json.load(f)


def normalize_proprio_bounds_q99(proprio, stats):
    q99 = np.array(stats["q99"])
    q01 = np.array(stats["q01"])
    mask = np.array(stats.get("mask", np.ones_like(q01, dtype=bool)))
    return np.where(mask, 2.0 * (proprio - q01) / (q99 - q01 + 1e-8) - 1.0, proprio)


def unnormalize_actions_bounds_q99(normalized, stats):
    q99 = np.array(stats["q99"])
    q01 = np.array(stats["q01"])
    mask = np.array(stats["mask"])
    return np.where(mask, 0.5 * (normalized + 1) * (q99 - q01) + q01, normalized)


def get_libero_image(obs):
    return obs["agentview_image"][::-1, ::-1]


def get_libero_wrist_image(obs):
    return obs["robot0_eye_in_hand_image"][::-1, ::-1]


def prepare_obs(obs, resize_size):
    img = get_libero_image(obs)
    wrist = get_libero_wrist_image(obs)
    img_pil = Image.fromarray(img).resize(resize_size, Image.BILINEAR)
    wrist_pil = Image.fromarray(wrist).resize(resize_size, Image.BILINEAR)
    state = np.concatenate([
        obs["robot0_eef_pos"],
        quat2axisangle(obs["robot0_eef_quat"]),
        obs["robot0_gripper_qpos"],
    ])
    return np.array(img_pil), np.array(wrist_pil), state


@torch.no_grad()
def predict_actions(model, device, img_np, wrist_np, state, task_desc,
                    norm_stats, unnorm_key, preprocessor, sequence_length):
    proprio_np = np.array(state, dtype=np.float32).reshape(1, -1)
    proprio_stats = norm_stats[unnorm_key]["proprio"]
    proprio_np = normalize_proprio_bounds_q99(proprio_np, proprio_stats)
    proprio = torch.from_numpy(proprio_np).float().unsqueeze(1).numpy()
    pad_width = [(0, 0)] * (proprio.ndim - 1) + [(0, model.config.proprio_dim - proprio.shape[-1])]
    proprio = np.pad(proprio, pad_width, constant_values=0)

    dummy_action = np.zeros((model.config.num_actions_chunk, model.config.action_dim), dtype=np.float32)
    input_data = {
        "question": task_desc,
        "proprio": proprio,
        "action": dummy_action,
        "action_pad_mask": np.zeros_like(dummy_action, dtype=bool),
        "answer": "Action",
        "style": "action",
        "metadata": {},
        "images": [Image.fromarray(img_np), Image.fromarray(wrist_np)],
    }

    processed = preprocessor(input_data)

    collator = MMCollatorForAction(
        model_config=model.config,
        use_proprio=True,
        max_sequence_length=sequence_length,
        include_metadata=False,
        pad="to_max",
        max_crops=model.config.get_max_crops(),
    )
    batch = collator([processed])
    for k in batch:
        if isinstance(batch[k], torch.Tensor):
            batch[k] = batch[k].to(device)

    model_inputs = {
        "input_ids": batch["input_ids"],
        "images": batch.get("images"),
        "image_masks": batch.get("image_masks"),
        "attention_mask": batch.get("attention_mask"),
        "attention_bias": batch.get("attention_bias"),
        "response_mask": (batch["loss_masks"] > 0) if "loss_masks" in batch else None,
        "image_input_idx": batch.get("image_input_idx"),
        "subsegment_ids": batch.get("subsegment_ids"),
        "position_ids": batch.get("position_ids"),
        "action_proprio": batch.get("proprio"),
        "proprio_token_idx": batch.get("proprio_token_idx"),
        "output_hidden_states": False,
        "use_cache": True,
    }

    with torch.autocast("cuda", dtype=torch.bfloat16):
        norm_actions = model.predict_actions(**model_inputs)
    norm_actions = norm_actions.to(torch.float32).cpu().numpy()
    norm_actions = norm_actions[..., :7]

    action_stats = norm_stats[unnorm_key]["action"]
    actions = unnormalize_actions_bounds_q99(norm_actions, action_stats)

    if actions.ndim == 3:
        actions = actions[0]
    return actions


def process_action(action):
    a = action.copy()
    a[-1] = 1.0 if a[-1] > 0.5 else -1.0
    a[-1] = -a[-1]
    return a


def run_rollout(env, init_state, model, device, task_desc, max_steps,
                norm_stats, unnorm_key, preprocessor, sequence_length):
    env.reset()
    obs = env.set_init_state(init_state)

    for _ in range(NUM_STEPS_WAIT):
        obs, _, _, _ = env.step(np.array([0, 0, 0, 0, 0, 0, -1], dtype=np.float64))

    resize_size = tuple(model.config.vision_backbone.image_default_input_size)
    action_queue = deque()

    for step in range(max_steps):
        try:
            if len(action_queue) == 0:
                img_np, wrist_np, state = prepare_obs(obs, resize_size)
                chunk = predict_actions(
                    model, device, img_np, wrist_np, state, task_desc,
                    norm_stats, unnorm_key, preprocessor, sequence_length,
                )
                for i in range(min(NUM_OPEN_LOOP_STEPS, len(chunk))):
                    action_queue.append(chunk[i])

            raw_action = action_queue.popleft()
            action = process_action(raw_action)
            obs, reward, done, info = env.step(action.tolist())
        except Exception as e:
            print(f"[rollout] step {step}: {e}")
            traceback.print_exc()
            return False, step

        if done or info.get("success", False):
            return True, step + 1

    return False, max_steps


def evaluate(args):
    set_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}")

    print(f"[a1-eval] benchmark={args.benchmark}, n_rollouts={args.n_rollouts}, seed={args.seed}")

    model = load_a1_model(args.checkpoint, device, tokenizer_path=getattr(args, 'tokenizer_path', None))
    norm_stats = load_norm_stats(args.checkpoint)
    unnorm_key = UNNORM_KEY_MAP[args.benchmark]
    assert unnorm_key in norm_stats, f"Key {unnorm_key} not in norm_stats"

    preprocessor = build_mm_preprocessor(
        model_config=model.config,
        shuffle_messages=True,
        require_image_features=True,
        is_training=False,
    )

    max_steps = SUITE_MAX_STEPS[args.benchmark]
    libero_suite_name = SUITE_TO_LIBERO[args.benchmark]

    task_suite = benchmark.get_benchmark(libero_suite_name)()
    num_tasks = task_suite.n_tasks

    print(f"[a1-eval] suite={libero_suite_name}, tasks={num_tasks}, max_steps={max_steps}")

    from libero.libero.envs import OffScreenRenderEnv
    results = {}
    total_success = 0
    total_episodes = 0

    for task_id in range(num_tasks):
        task = task_suite.get_task(task_id)
        task_name = task.name
        task_desc = task.language
        task_bddl = task_suite.get_task_bddl_file_path(task_id)
        init_states = task_suite.get_task_init_states(task_id)

        env_args = {
            "bddl_file_name": task_bddl,
            "camera_heights": 256,
            "camera_widths": 256,
            "camera_names": ["agentview", "robot0_eye_in_hand"],
            "render_gpu_device_id": int(os.environ.get("MUJOCO_EGL_DEVICE_ID", "0")),
        }
        env = OffScreenRenderEnv(**env_args)

        task_successes = 0
        for trial in range(args.n_rollouts):
            set_seed(args.seed + trial)
            init_state = init_states[trial % len(init_states)]

            success, steps = run_rollout(
                env, init_state, model, device, task_desc, max_steps,
                norm_stats, unnorm_key, preprocessor, args.sequence_length,
            )
            task_successes += int(success)
            total_success += int(success)
            total_episodes += 1

            status = "OK" if success else "FAIL"
            print(f"  task {task_id}/{num_tasks} [{task_name}] "
                  f"trial {trial+1}/{args.n_rollouts}: {status} ({steps} steps)")

        task_sr = task_successes / args.n_rollouts
        results[task_name] = {"success_rate": task_sr, "successes": task_successes, "trials": args.n_rollouts}
        print(f"[a1-eval] Task {task_id} [{task_name}]: SR={task_sr:.1%} ({task_successes}/{args.n_rollouts})")

        env.close()

    overall_sr = total_success / total_episodes if total_episodes > 0 else 0.0
    print(f"\n[a1-eval] Overall: SR={overall_sr:.1%} ({total_success}/{total_episodes})")

    summary = {
        "model": "a1-libero",
        "benchmark": args.benchmark,
        "mode": "vla_only",
        "seed": args.seed,
        "n_rollouts": args.n_rollouts,
        "overall_success_rate": overall_sr,
        "total_successes": total_success,
        "total_episodes": total_episodes,
        "per_task": results,
    }

    out_path = Path(args.output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(summary, indent=2))
    print(f"[a1-eval] Results saved to {args.output_file}")
    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--benchmark", default="object", choices=["object", "spatial", "goal", "long", "90"])
    p.add_argument("--checkpoint", default="/root/autodl-tmp/models/a1-libero/")
    p.add_argument("--n_rollouts", type=int, default=20)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--sequence_length", type=int, default=1024)
    p.add_argument("--output_file", default=None)
    p.add_argument("--tokenizer_path", default=None)
    args = p.parse_args()

    if args.output_file is None:
        args.output_file = f"logs/eval_{args.benchmark}_a1_vla_only_seed{args.seed}.json"

    evaluate(args)


if __name__ == "__main__":
    main()
