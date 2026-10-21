"""Dose-Response Curve: L1 Head Ablation — ablate top-N heads by instruction attention fraction."""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---

import argparse
import gc
import glob
import json
import os
import sys
import time

sys.path.insert(0, LIBERO_ROOT)
os.environ["MUJOCO_GL"] = "egl"
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from scipy import stats

np.random.seed(42)
torch.manual_seed(42)

MODEL_PATH = f"{PROJECT_ROOT}/checkpoints/openvla-7b"
UNNORM_KEY = "bridge_orig"
DATA_DIR = f"{PROJECT_ROOT}/data/libero/libero_goal"
RESULTS_DIR = f"{PROJECT_ROOT}/results"

NUM_IMAGE_TOKENS = 256
INST_START = 1 + NUM_IMAGE_TOKENS
DIM_NAMES = ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]

# Per-head instruction attention fraction (trained model, per task)
_FRAC_T0 = [0.8536376953125,0.53509521484375,0.68304443359375,0.471466064453125,0.5867233276367188,0.498046875,0.394805908203125,0.569671630859375,0.58123779296875,0.452606201171875,0.7152099609375,0.5701904296875,0.5364990234375,0.41016387939453125,0.69647216796875,0.6108169555664062,0.525848388671875,0.55120849609375,0.5181121826171875,0.6407318115234375,0.5516357421875,0.458770751953125,0.8058147430419922,0.57220458984375,0.366424560546875,0.769256591796875,0.56707763671875,0.653472900390625,0.503387451171875,0.589263916015625,0.5357666015625,0.5589599609375]
_FRAC_T1 = [0.856719970703125,0.5569610595703125,0.7030029296875,0.4571533203125,0.5877685546875,0.4925537109375,0.40106201171875,0.557342529296875,0.5824584960937,0.437347412109375,0.71026611328125,0.6070327758789062,0.53277587890625,0.5465087890625,0.5405426025390625,0.6549072265625,0.52325439453125,0.452239990234375,0.8254013061523438,0.590728759765625,0.3663177490234375,0.781494140625,0.55816650390625,0.6743011474609375,0.498626708984375,0.611358642578125,0.542572021484375,0.547607421875,0.5181121826171875,0.6407318115234375,0.5516357421875,0.458770751953125]
_FRAC_T2 = [0.852569580078125,0.54840087890625,0.7081298828125,0.475555419921875,0.5866012573242188,0.50164794921875,0.413299560546875,0.573699951171875,0.5865478515625,0.4401397705078125,0.71649169921875,0.57843017578125,0.534912109375,0.4060821533203125,0.71636962890625,0.6230087280273438,0.538482666015625,0.5455322265625,0.5452117919921875,0.646087646484375,0.53546142578125,0.45086669921875,0.8309307098388672,0.576568603515625,0.3722991943359375,0.787872314453125,0.5629119873046875,0.686920166015625,0.503082275390625,0.60833740234375,0.54925537109375,0.55242919921875]

MEAN_INSTR_FRAC = np.mean([_FRAC_T0, _FRAC_T1, _FRAC_T2], axis=0)
HEADS_SORTED_DESC = np.argsort(-MEAN_INSTR_FRAC).tolist()


def load_model():
    from transformers import AutoModelForVision2Seq, AutoProcessor

    processor = AutoProcessor.from_pretrained(MODEL_PATH, trust_remote_code=True)
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
    ).to("cuda:0").eval()
    return model, processor


def predict_action_with_logits(model, input_ids, pixel_values, unnorm_key):
    action_dim = model.get_action_dim(unnorm_key)
    if not torch.all(input_ids[:, -1] == 29871):
        input_ids = torch.cat(
            (input_ids, torch.tensor([[29871]], device=input_ids.device, dtype=input_ids.dtype)),
            dim=1,
        )
    with torch.no_grad():
        outputs = model(
            input_ids=input_ids,
            attention_mask=torch.ones_like(input_ids),
            pixel_values=pixel_values,
            past_key_values=None,
            use_cache=True,
        )
    past_key_values = outputs.past_key_values
    next_token_logits = outputs.logits[:, -1, :]

    generated_ids = []
    all_logits = []

    for _ in range(action_dim):
        all_logits.append(next_token_logits.float().cpu())
        next_token = torch.argmax(next_token_logits, dim=-1, keepdim=True)
        generated_ids.append(next_token.squeeze().item())
        attn_mask = torch.ones(
            (1, past_key_values[0][0].shape[2] + 1),
            device=input_ids.device,
            dtype=input_ids.dtype,
        )
        with torch.no_grad():
            outputs = model(
                input_ids=next_token,
                attention_mask=attn_mask,
                pixel_values=None,
                past_key_values=past_key_values,
                use_cache=True,
            )
        past_key_values = outputs.past_key_values
        next_token_logits = outputs.logits[:, -1, :]

    predicted_action_token_ids = np.array(generated_ids)
    discretized_actions = model.vocab_size - predicted_action_token_ids
    discretized_actions = np.clip(
        discretized_actions - 1, a_min=0, a_max=model.bin_centers.shape[0] - 1
    )
    normalized_actions = model.bin_centers[discretized_actions]
    action_norm_stats = model.get_action_stats(unnorm_key)
    mask = action_norm_stats.get("mask", np.ones_like(action_norm_stats["q01"], dtype=bool))
    action_high = np.array(action_norm_stats["q99"])
    action_low = np.array(action_norm_stats["q01"])
    action = np.where(
        mask,
        0.5 * (normalized_actions + 1) * (action_high - action_low) + action_low,
        normalized_actions,
    )

    logits_tensor = torch.cat(all_logits, dim=0)
    return action, predicted_action_token_ids, logits_tensor


def install_ablation_hook(model):
    import math
    from transformers.models.llama.modeling_llama import apply_rotary_pos_emb, repeat_kv

    layer_attn = model.language_model.model.layers[1].self_attn
    layer_attn._ablate_heads = None
    original_forward = layer_attn.forward

    def ablated_forward(
        hidden_states,
        attention_mask=None,
        position_ids=None,
        past_key_value=None,
        output_attentions=False,
        use_cache=False,
        cache_position=None,
        **kwargs,
    ):
        bsz, q_len, _ = hidden_states.size()
        query_states = layer_attn.q_proj(hidden_states)
        key_states = layer_attn.k_proj(hidden_states)
        value_states = layer_attn.v_proj(hidden_states)

        query_states = query_states.view(bsz, q_len, layer_attn.num_heads, layer_attn.head_dim).transpose(1, 2)
        key_states = key_states.view(bsz, q_len, layer_attn.num_key_value_heads, layer_attn.head_dim).transpose(1, 2)
        value_states = value_states.view(bsz, q_len, layer_attn.num_key_value_heads, layer_attn.head_dim).transpose(1, 2)

        pkv = getattr(layer_attn, "past_key_value", past_key_value)
        cos, sin = layer_attn.rotary_emb(value_states, position_ids)
        query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)

        if pkv is not None:
            cache_kwargs = {"sin": sin, "cos": cos, "cache_position": cache_position}
            key_states, value_states = pkv.update(key_states, value_states, layer_attn.layer_idx, cache_kwargs)

        key_states = repeat_kv(key_states, layer_attn.num_key_value_groups)
        value_states = repeat_kv(value_states, layer_attn.num_key_value_groups)

        attn_weights = torch.matmul(query_states, key_states.transpose(2, 3)) / math.sqrt(layer_attn.head_dim)
        if attention_mask is not None:
            causal_mask = attention_mask[:, :, :, :key_states.shape[-2]]
            attn_weights = attn_weights + causal_mask

        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query_states.dtype)
        attn_weights = nn.functional.dropout(attn_weights, p=layer_attn.attention_dropout, training=layer_attn.training)

        if layer_attn._ablate_heads is not None:
            kv_len = attn_weights.shape[-1]
            if INST_START < kv_len:
                attn_weights[:, layer_attn._ablate_heads, :, INST_START:] = 0.0
                row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)
                attn_weights = attn_weights / row_sums

        attn_output = torch.matmul(attn_weights, value_states)
        attn_output = attn_output.transpose(1, 2).contiguous()
        attn_output = attn_output.reshape(bsz, q_len, layer_attn.hidden_size)
        attn_output = layer_attn.o_proj(attn_output)

        if not output_attentions:
            attn_weights = None
        return attn_output, attn_weights, pkv

    layer_attn.forward = ablated_forward
    return original_forward, layer_attn


def compute_kl_divergence(logits_p, logits_q):
    log_p = F.log_softmax(logits_p, dim=-1)
    log_q = F.log_softmax(logits_q, dim=-1)
    p = F.softmax(logits_p, dim=-1)
    kl = (p * (log_p - log_q)).sum(dim=-1)
    return kl.numpy()


def get_task_files(n_tasks):
    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.hdf5")))
    return hdf5_files[:n_tasks]


def get_language_instruction(hdf5_path):
    with h5py.File(hdf5_path, "r") as f:
        info = json.loads(f["data"].attrs["problem_info"])
    return info["language_instruction"]


def bootstrap_cohens_d_ci(paired_mse, n_boot=1000):
    n = len(paired_mse)
    rng = np.random.RandomState(42)
    d_boots = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, n, n)
        sample = paired_mse[idx]
        d_boots[i] = np.mean(sample) / (np.std(sample, ddof=1) + 1e-12)
    return float(np.percentile(d_boots, 2.5)), float(np.percentile(d_boots, 97.5))


def compute_condition_metrics(b_actions, a_actions, b_ids, a_ids, kl_divs, per_task):
    all_b = np.array(b_actions)
    all_a = np.array(a_actions)
    all_b_ids = np.array(b_ids)
    all_a_ids = np.array(a_ids)
    all_kls = np.array(kl_divs)

    paired_mse = np.mean((all_b - all_a) ** 2, axis=1)
    t_res = stats.ttest_1samp(paired_mse, 0)
    cohens_d = np.mean(paired_mse) / (np.std(paired_mse, ddof=1) + 1e-12)
    ci_lo, ci_hi = bootstrap_cohens_d_ci(paired_mse)

    per_dim_shift = np.abs(all_b - all_a)
    token_div = np.mean(all_b_ids != all_a_ids)

    return {
        "paired_mse": {
            "mean": float(np.mean(paired_mse)),
            "std": float(np.std(paired_mse)),
            "t_stat": float(t_res.statistic),
            "p_value": float(t_res.pvalue),
            "cohens_d": float(cohens_d),
            "ci_95": [ci_lo, ci_hi],
        },
        "per_dim_shift": {
            dim: {"mean": float(np.mean(per_dim_shift[:, i])),
                  "std": float(np.std(per_dim_shift[:, i]))}
            for i, dim in enumerate(DIM_NAMES)
        },
        "token_divergence_rate": float(token_div),
        "kl_divergence": {
            "mean": float(np.mean(all_kls)),
            "std": float(np.std(all_kls)),
        },
        "n_samples": int(len(all_b)),
        "per_task": per_task,
    }


def run_conditions(args):
    conditions = [int(x) for x in args.conditions.split(",")]
    n_tasks = 1 if args.dry_run else 5
    n_demos = 1 if args.dry_run else 10
    n_timesteps = 2 if args.dry_run else 50

    os.makedirs(RESULTS_DIR, exist_ok=True)

    print(f"Heads sorted by instruction attention (descending):")
    for i, h in enumerate(HEADS_SORTED_DESC):
        print(f"  #{i+1}: head {h} (frac={MEAN_INSTR_FRAC[h]:.4f})")

    condition_heads = {}
    for n in conditions:
        heads = HEADS_SORTED_DESC[:n]
        condition_heads[n] = heads
        print(f"Condition top-{n}: {heads}")

    print(f"\nLoading model...")
    model, processor = load_model()
    print("Model loaded.")

    original_fn, layer1_attn = install_ablation_hook(model)

    task_files = get_task_files(n_tasks)
    print(f"Tasks ({n_tasks}): {[os.path.basename(f) for f in task_files]}")
    print(f"Config: {n_demos} demos/task, {n_timesteps} steps/demo, conditions={conditions}")

    cond_store = {n: {
        "b_act": [], "a_act": [], "b_ids": [], "a_ids": [], "kls": [],
        "per_task": {},
    } for n in conditions}

    total_calls = 0
    n_dp = n_tasks * n_demos * n_timesteps
    expected_calls = n_dp * (1 + len(conditions))
    t_start = time.time()

    for task_idx, hdf5_path in enumerate(task_files):
        task_name = os.path.basename(hdf5_path).replace("_demo.hdf5", "")
        instruction = get_language_instruction(hdf5_path)
        print(f"\n{'='*60}")
        print(f"Task {task_idx}: {task_name}")
        print(f"  Instruction: {instruction}")

        task_buf = {n: {"b": [], "a": [], "bi": [], "ai": [], "k": []} for n in conditions}

        prompt = f"In: What action should the robot take to {instruction}?\nOut:"

        with h5py.File(hdf5_path, "r") as f:
            for demo_idx in range(n_demos):
                demo_key = f"data/demo_{demo_idx}"
                actions_data = f[f"{demo_key}/actions"][:]
                images_data = f[f"{demo_key}/obs/agentview_rgb"][:]
                n_steps = min(n_timesteps, len(actions_data))

                for step_idx in range(n_steps):
                    img = Image.fromarray(images_data[step_idx])
                    inputs = processor(prompt, img).to("cuda:0", dtype=torch.bfloat16)
                    input_ids = inputs["input_ids"]
                    pixel_values = inputs["pixel_values"]

                    layer1_attn._ablate_heads = None
                    b_action, b_ids, b_logits = predict_action_with_logits(
                        model, input_ids, pixel_values, UNNORM_KEY
                    )
                    total_calls += 1

                    for n in conditions:
                        layer1_attn._ablate_heads = condition_heads[n]
                        a_action, a_ids, a_logits = predict_action_with_logits(
                            model, input_ids, pixel_values, UNNORM_KEY
                        )
                        total_calls += 1

                        kl = compute_kl_divergence(b_logits, a_logits)

                        cond_store[n]["b_act"].append(b_action)
                        cond_store[n]["a_act"].append(a_action)
                        cond_store[n]["b_ids"].append(b_ids)
                        cond_store[n]["a_ids"].append(a_ids)
                        cond_store[n]["kls"].append(kl)

                        task_buf[n]["b"].append(b_action)
                        task_buf[n]["a"].append(a_action)
                        task_buf[n]["bi"].append(b_ids)
                        task_buf[n]["ai"].append(a_ids)
                        task_buf[n]["k"].append(kl)

                        del a_logits

                    del b_logits
                    torch.cuda.empty_cache()

                    if total_calls % 50 == 0:
                        elapsed = time.time() - t_start
                        rate = total_calls / elapsed
                        eta = (expected_calls - total_calls) / max(rate, 0.01)
                        print(
                            f"  [{total_calls}/{expected_calls} calls, "
                            f"{elapsed:.0f}s, {rate:.1f}/s, ETA {eta:.0f}s]"
                        )

        for n in conditions:
            tb = task_buf[n]
            if tb["b"]:
                arr_b = np.array(tb["b"])
                arr_a = np.array(tb["a"])
                p_mse = np.mean((arr_b - arr_a) ** 2, axis=1)
                tok_div = np.mean(np.array(tb["bi"]) != np.array(tb["ai"]))
                kl_m = np.mean(np.array(tb["k"]))
                cond_store[n]["per_task"][task_name] = {
                    "paired_mse_mean": float(np.mean(p_mse)),
                    "token_divergence_rate": float(tok_div),
                    "kl_mean": float(kl_m),
                    "n_samples": len(tb["b"]),
                }
                print(
                    f"  [top-{n}] mse={np.mean(p_mse):.6f}, "
                    f"tok_div={tok_div:.4f}, kl={kl_m:.4f}"
                )

        gc.collect()
        torch.cuda.empty_cache()

    layer1_attn._ablate_heads = None

    for n in conditions:
        cd = cond_store[n]
        result = compute_condition_metrics(
            cd["b_act"], cd["a_act"], cd["b_ids"], cd["a_ids"],
            cd["kls"], cd["per_task"],
        )
        result["n_heads_ablated"] = n
        result["heads_ablated"] = condition_heads[n]
        result["heads_ablated_fracs"] = [float(MEAN_INSTR_FRAC[h]) for h in condition_heads[n]]
        result["config"] = {
            "n_tasks": n_tasks,
            "n_demos_per_task": n_demos,
            "n_timesteps_per_demo": n_timesteps,
            "model": "openvla-7b",
            "unnorm_key": UNNORM_KEY,
        }

        out_path = os.path.join(RESULTS_DIR, f"dose_response_top{n}.json")
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)
        m = result["paired_mse"]
        print(
            f"\nSaved {out_path}\n"
            f"  top-{n}: mse={m['mean']:.6f}, d={m['cohens_d']:.3f} "
            f"[{m['ci_95'][0]:.3f}, {m['ci_95'][1]:.3f}], "
            f"tok_div={result['token_divergence_rate']:.4f}, "
            f"kl={result['kl_divergence']['mean']:.4f}"
        )

    elapsed_total = time.time() - t_start
    print(f"\nDone. {total_calls} calls in {elapsed_total:.0f}s ({elapsed_total/60:.1f}min)")


def merge_results(args):
    all_ns = [int(x) for x in args.merge.split(",")]
    merged = {"conditions": [], "head_ranking": HEADS_SORTED_DESC,
              "head_fracs": [float(MEAN_INSTR_FRAC[h]) for h in HEADS_SORTED_DESC]}
    for n in sorted(all_ns):
        path = os.path.join(RESULTS_DIR, f"dose_response_top{n}.json")
        if os.path.exists(path):
            with open(path) as f:
                merged["conditions"].append(json.load(f))
            print(f"Loaded {path}")
        else:
            print(f"WARNING: {path} not found, skipping")
    out_path = os.path.join(RESULTS_DIR, "dose_response_curve.json")
    with open(out_path, "w") as f:
        json.dump(merged, f, indent=2)
    print(f"\nMerged {len(merged['conditions'])} conditions -> {out_path}")

    print("\n=== Summary ===")
    print(f"{'N heads':>8} {'MSE':>10} {'Cohen d':>10} {'95% CI':>20} {'Tok div':>10} {'KL':>10}")
    for c in merged["conditions"]:
        m = c["paired_mse"]
        print(
            f"{c['n_heads_ablated']:>8} {m['mean']:>10.6f} {m['cohens_d']:>10.3f} "
            f"[{m['ci_95'][0]:>8.3f}, {m['ci_95'][1]:>7.3f}] "
            f"{c['token_divergence_rate']:>10.4f} {c['kl_divergence']['mean']:>10.4f}"
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--conditions", type=str, help="Comma-separated N values, e.g. '4,8,12,16'")
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--merge", type=str, help="Merge mode: comma-separated N values to combine")
    args = parser.parse_args()

    if args.merge:
        merge_results(args)
    elif args.conditions:
        run_conditions(args)
    else:
        parser.error("Provide --conditions or --merge")


if __name__ == "__main__":
    main()
