"""
OpenVLA LIBERO Evaluation: Zero-mask vs Hard-prune Ablation.

Distinguishes two failure mechanisms of token pruning:
  (a) information loss (pruned token content gone)
  (b) position disruption (remaining tokens shift in position embedding)

--ablation_mode hard_prune : physically removes pruned tokens (sequence length shrinks)
--ablation_mode zero_mask  : sets value of pruned tokens to 0, keeps sequence length / positions

Usage:
    python eval_openvla_zeromask_libero.py --mode l2norm_prune --ablation_mode zero_mask \\
        --k_ratio 0.5 --suite libero_object
"""
import argparse, io, json, math, os, sys, time
os.environ["MUJOCO_GL"] = "egl"
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "0")
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

# Use transformers 4.40.1 for OpenVLA compat
sys.path.insert(0, "/root/autodl-tmp/openvla_deps")

import numpy as np
import torch
from PIL import Image

# Import OpenVLA model code
hf_dir = "/root/autodl-tmp/openvla-repo/prismatic/extern/hf"
init_path = os.path.join(hf_dir, "__init__.py")
if not os.path.exists(init_path):
    open(init_path, "w").close()
sys.path.insert(0, "/root/autodl-tmp/openvla-repo/prismatic/extern")
from hf.configuration_prismatic import OpenVLAConfig
from hf.modeling_prismatic import OpenVLAForActionPrediction
from hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor

DEVICE = torch.device("cuda:0")
CHECKPOINT_PATH = "/root/autodl-tmp/openvla-libero-object"
UNNORM_KEY = "libero_object"

SUITE_MAX_STEPS = {
    "libero_spatial": 280,
    "libero_object": 280,
    "libero_goal": 300,
    "libero_10": 520,
}


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["baseline", "random_prune", "l2norm_prune", "attention_prune"], default="baseline")
    p.add_argument("--ablation_mode", choices=["hard_prune", "zero_mask"], default="hard_prune",
                   help="hard_prune: physically remove pruned tokens. "
                        "zero_mask: zero out pruned tokens, keep positions.")
    p.add_argument("--k_ratio", type=float, default=0.5)
    p.add_argument("--suite", type=str, default="libero_object")
    p.add_argument("--num_episodes", type=int, default=50)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--output", type=str, default=None)
    p.add_argument("--center_crop", action="store_true", default=True)
    p.add_argument("--num_steps_wait", type=int, default=10)
    p.add_argument("--model_path", type=str, default="/root/autodl-tmp/openvla-libero-object")
    p.add_argument("--unnorm_key", type=str, default="libero_object")
    return p.parse_args()


def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    import random
    random.seed(seed)


def load_model():
    print("[*] Loading OpenVLA from:", CHECKPOINT_PATH, flush=True)
    config = OpenVLAConfig.from_pretrained(CHECKPOINT_PATH)
    vla = OpenVLAForActionPrediction.from_pretrained(
        CHECKPOINT_PATH,
        config=config,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
    ).to(DEVICE)
    with open(os.path.join(CHECKPOINT_PATH, "dataset_statistics.json")) as f:
        vla.norm_stats = json.load(f)
    vla.eval()

    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT_PATH)
    image_processor = PrismaticImageProcessor.from_pretrained(CHECKPOINT_PATH)
    processor = PrismaticProcessor(image_processor=image_processor, tokenizer=tokenizer)
    print(f"[*] Model loaded, GPU: {torch.cuda.max_memory_allocated()/1e9:.1f} GB", flush=True)
    return vla, processor


def center_crop_image(image: Image.Image, crop_scale=0.9) -> Image.Image:
    w, h = image.size
    new_w = int(w * math.sqrt(crop_scale))
    new_h = int(h * math.sqrt(crop_scale))
    left = (w - new_w) // 2
    top = (h - new_h) // 2
    cropped = image.crop((left, top, left + new_w, top + new_h))
    return cropped.resize((w, h), Image.LANCZOS)


def preprocess_image(obs, center_crop=True):
    img = obs["agentview_image"]
    img = img[::-1, ::-1]
    pil_img = Image.fromarray(img)
    buf = io.BytesIO()
    pil_img.save(buf, format="JPEG")
    buf.seek(0)
    pil_img = Image.open(buf).convert("RGB")
    pil_img = pil_img.resize((224, 224), Image.LANCZOS)
    if center_crop:
        pil_img = center_crop_image(pil_img, crop_scale=0.9)
    return pil_img


def get_action(vla, processor, image: Image.Image, task_label: str):
    prompt = f"In: What action should the robot take to {task_label.lower()}?\nOut:"
    inputs = processor(prompt, image).to(DEVICE, dtype=torch.bfloat16)
    action = vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)
    return action


def normalize_gripper_action(action, binarize=True):
    action[..., -1] = 2 * action[..., -1] - 1
    if binarize:
        action[..., -1] = np.sign(action[..., -1])
    return action


def invert_gripper_action(action):
    action[..., -1] *= -1.0
    return action


def _apply_selection(output, keep_indices, ablation_mode):
    """Apply pruning given indices to keep.

    output: (B, N, D)
    keep_indices: (B, keep) -- indices into N dimension, already sorted ascending.
    ablation_mode: 'hard_prune' (gather, len=keep) or 'zero_mask' (mask out
        non-selected positions, len=N preserved).
    """
    B, N, D = output.shape
    if ablation_mode == "hard_prune":
        return torch.gather(output, 1, keep_indices.unsqueeze(-1).expand(-1, -1, D))
    # zero_mask: build (B, N) keep-mask, zero the rest, preserve shape & positions
    mask = torch.zeros(B, N, dtype=torch.bool, device=output.device)
    mask.scatter_(1, keep_indices, True)
    return output * mask.unsqueeze(-1).to(output.dtype)


class RandomPruningHook:
    def __init__(self, k_ratio=0.5, ablation_mode="hard_prune"):
        self.k_ratio = k_ratio
        self.ablation_mode = ablation_mode
        self.logged = False

    def __call__(self, module, input, output):
        B, N, D = output.shape
        keep = int(N * self.k_ratio)
        if keep >= N:
            return output
        perm = torch.randperm(N, device=output.device)[:keep].sort().values
        keep_indices = perm.unsqueeze(0).expand(B, -1)
        out = _apply_selection(output, keep_indices, self.ablation_mode)
        if not self.logged:
            print(f"[Random {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})", flush=True)
            self.logged = True
        return out


class L2NormPruningHook:
    """Keep top-k vision tokens ranked by L2 norm (largest norm = most important)."""
    def __init__(self, k_ratio=0.5, ablation_mode="hard_prune"):
        self.k_ratio = k_ratio
        self.ablation_mode = ablation_mode
        self.logged = False

    def __call__(self, module, input, output):
        B, N, D = output.shape
        keep = int(N * self.k_ratio)
        if keep >= N:
            return output
        norms = torch.norm(output.float(), dim=-1)  # (B, N)
        _, indices = torch.topk(norms, keep, dim=-1)
        keep_indices = indices.sort(dim=-1).values
        out = _apply_selection(output, keep_indices, self.ablation_mode)
        if not self.logged:
            print(f"[L2 {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio})", flush=True)
            self.logged = True
        return out


class AttentionPruningHook:
    """Keep top-k vision tokens ranked by attention importance (2-layer probe)."""
    def __init__(self, k_ratio, vla, ablation_mode="hard_prune"):
        self.k_ratio = k_ratio
        self.vla = vla
        self.ablation_mode = ablation_mode
        self.logged = False

    def __call__(self, module, input, output):
        import torch.nn.functional as F

        B, N, D = output.shape
        keep = max(1, int(N * self.k_ratio))
        if keep >= N:
            return output

        lm = self.vla.language_model.model
        position_ids = torch.arange(N, device=output.device).unsqueeze(0).expand(B, -1)

        hidden = output
        all_attn = []

        with torch.no_grad():
            for layer_idx in range(min(2, len(lm.layers))):
                layer = lm.layers[layer_idx]
                normed = layer.input_layernorm(hidden)

                head_dim = layer.self_attn.head_dim
                n_q_heads = layer.self_attn.num_heads
                n_kv_heads = layer.self_attn.num_key_value_heads

                q = layer.self_attn.q_proj(normed)
                k = layer.self_attn.k_proj(normed)
                v = layer.self_attn.v_proj(normed)

                q = q.view(B, N, n_q_heads, head_dim).transpose(1, 2)
                k = k.view(B, N, n_kv_heads, head_dim).transpose(1, 2)
                v = v.view(B, N, n_kv_heads, head_dim).transpose(1, 2)

                cos, sin = layer.self_attn.rotary_emb(v, position_ids)
                from transformers.models.llama.modeling_llama import rotate_half
                q_embed = (q * cos) + (rotate_half(q) * sin)
                k_embed = (k * cos) + (rotate_half(k) * sin)

                if n_kv_heads != n_q_heads:
                    n_rep = n_q_heads // n_kv_heads
                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)
                    v = v.repeat_interleave(n_rep, dim=1)

                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)
                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)
                all_attn.append(attn_weights)

                attn_out = torch.matmul(attn_weights.to(v.dtype), v)
                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)
                attn_out = layer.self_attn.o_proj(attn_out)
                hidden = hidden + attn_out

                normed2 = layer.post_attention_layernorm(hidden)
                mlp_out = layer.mlp(normed2)
                hidden = hidden + mlp_out

        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]
        importance = avg_attn.sum(dim=1)  # [B, N]

        _, indices = torch.topk(importance, keep, dim=-1)
        keep_indices = indices.sort(dim=-1).values
        out = _apply_selection(output, keep_indices, self.ablation_mode)

        if not self.logged:
            print(f"[Attn {self.ablation_mode}] {N} -> keep {keep} (k={self.k_ratio}), "
                  f"importance range=[{importance.min():.4f}, {importance.max():.4f}]", flush=True)
            self.logged = True

        return out


def count_vision_tokens(vla, processor):
    dummy = Image.new("RGB", (224, 224), (128, 128, 128))
    prompt = "In: What action should the robot take to pick up the object?\nOut:"
    inputs = processor(prompt, dummy).to(DEVICE, dtype=torch.bfloat16)
    count = {}
    def hook(m, i, o):
        count["n_tokens"] = o.shape[1]
        count["hidden_dim"] = o.shape[2]
        return o
    h = vla.projector.register_forward_hook(hook)
    with torch.no_grad():
        vla.predict_action(**inputs, unnorm_key=UNNORM_KEY, do_sample=False)
    h.remove()
    return count


def main():
    args = parse_args()
    global CHECKPOINT_PATH, UNNORM_KEY
    CHECKPOINT_PATH = args.model_path
    UNNORM_KEY = args.unnorm_key
    set_seed(args.seed)
    max_steps = SUITE_MAX_STEPS.get(args.suite, 300)

    if args.mode == "baseline" and args.ablation_mode != "hard_prune":
        print(f"[!] ablation_mode={args.ablation_mode} ignored for baseline mode", flush=True)

    vla, processor = load_model()

    token_info = count_vision_tokens(vla, processor)
    print(f"[*] Vision tokens: {token_info['n_tokens']}, dim: {token_info['hidden_dim']}", flush=True)

    hook_handle = None
    if args.mode == "random_prune":
        hook_handle = vla.projector.register_forward_hook(
            RandomPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))
        print(f"[*] Random pruning: k={args.k_ratio} ablation={args.ablation_mode}", flush=True)
    elif args.mode == "l2norm_prune":
        hook_handle = vla.projector.register_forward_hook(
            L2NormPruningHook(args.k_ratio, ablation_mode=args.ablation_mode))
        print(f"[*] L2 norm pruning: k={args.k_ratio} ablation={args.ablation_mode}", flush=True)
    elif args.mode == "attention_prune":
        hook_handle = vla.projector.register_forward_hook(
            AttentionPruningHook(args.k_ratio, vla, ablation_mode=args.ablation_mode))
        print(f"[*] Attention pruning: k={args.k_ratio} ablation={args.ablation_mode}", flush=True)

    from libero.libero import benchmark, get_libero_path
    from libero.libero.envs import OffScreenRenderEnv

    benchmark_dict = benchmark.get_benchmark_dict()
    task_suite = benchmark_dict[args.suite]()
    n_tasks = task_suite.n_tasks
    print(f"[*] {args.suite}: {n_tasks} tasks x {args.num_episodes} episodes = {n_tasks * args.num_episodes} total", flush=True)

    per_task_results = {}
    total_successes = 0
    total_episodes = 0
    t_start = time.time()

    for task_id in range(n_tasks):
        task = task_suite.get_task(task_id)
        task_description = task.language
        task_bddl_file = os.path.join(
            get_libero_path("bddl_files"), task.problem_folder, task.bddl_file
        )
        env = OffScreenRenderEnv(
            bddl_file_name=task_bddl_file, camera_heights=256, camera_widths=256
        )
        env.seed(args.seed)

        task_successes = 0
        print(f"\n[Task {task_id+1}/{n_tasks}] {task_description}", flush=True)

        for ep in range(args.num_episodes):
            env.reset()
            init_states = task_suite.get_task_init_states(task_id)
            obs = env.set_init_state(init_states[ep])
            done = False
            t = 0

            while t < max_steps + args.num_steps_wait:
                try:
                    if t < args.num_steps_wait:
                        obs, reward, done, info = env.step([0, 0, 0, 0, 0, 0, -1])
                        t += 1
                        continue

                    img = preprocess_image(obs, center_crop=args.center_crop)
                    action = get_action(vla, processor, img, task_description)
                    action = normalize_gripper_action(action, binarize=True)
                    action = invert_gripper_action(action)
                    obs, reward, done, info = env.step(action.tolist())
                    if done:
                        task_successes += 1
                        total_successes += 1
                        break
                    t += 1
                except Exception as e:
                    print(f"  Exception t={t}: {e}", flush=True)
                    break

            total_episodes += 1
            if (ep + 1) % 10 == 0:
                elapsed = time.time() - t_start
                eps_per_min = total_episodes / (elapsed / 60)
                print(f"  Ep {ep+1}/{args.num_episodes} task_sr={task_successes}/{ep+1} "
                      f"({eps_per_min:.1f} eps/min)", flush=True)

        task_sr = task_successes / args.num_episodes
        per_task_results[task_description] = {
            "success_rate": task_sr,
            "successes": task_successes,
            "episodes": args.num_episodes,
        }
        print(f"  => Task SR: {task_sr:.3f} ({task_successes}/{args.num_episodes})", flush=True)
        env.close()

    overall_sr = total_successes / total_episodes
    elapsed = time.time() - t_start
    print(f"\n{'='*60}", flush=True)
    print(f"Overall SR: {overall_sr:.4f} ({total_successes}/{total_episodes})", flush=True)
    print(f"Time: {elapsed/60:.1f} min", flush=True)
    print(f"{'='*60}", flush=True)

    results = {
        "model": os.path.basename(CHECKPOINT_PATH),
        "mode": args.mode,
        "ablation_mode": args.ablation_mode,
        "suite": args.suite,
        "k_ratio": args.k_ratio if args.mode != "baseline" else None,
        "overall_success_rate": overall_sr,
        "total_successes": total_successes,
        "total_episodes": total_episodes,
        "per_task": per_task_results,
        "vision_tokens": token_info,
        "max_steps": max_steps,
        "seed": args.seed,
        "elapsed_minutes": elapsed / 60,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    if args.output:
        out_path = args.output
    else:
        out_dir = "/root/autodl-tmp/importance_margin_vla_compress/eval_results"
        os.makedirs(out_dir, exist_ok=True)
        suite_short = args.suite.replace('libero_', '')
        if args.mode == "baseline":
            out_path = f"{out_dir}/openvla_baseline_{suite_short}_seed{args.seed}.json"
        else:
            k_str = str(args.k_ratio).replace(".", "")
            abl_tag = "zm" if args.ablation_mode == "zero_mask" else "hp"
            out_path = f"{out_dir}/openvla_{args.mode}_{abl_tag}_k{k_str}_{suite_short}_seed{args.seed}.json"

    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"[*] Saved: {out_path}", flush=True)

    if hook_handle:
        hook_handle.remove()


if __name__ == "__main__":
    main()
