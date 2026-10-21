"""GSM8K generation quality comparison: dense vs KL sparse 50% Llama-3.1-8B."""

import importlib.util
import os
import sys
import random
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset

sys.path.insert(0, "/root/distill_sparse_swiglu/src")
from data_utils import get_eval_dataset
from predictor import PredictorWrapper

MODEL_PATH = "/root/autodl-tmp/models/llama-3.1-8b"
PREDICTOR_PATH = "/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt"
SPARSITY_TARGET = 0.5
NUM_SAMPLES = 10
MAX_NEW_TOKENS = 256
SEQ_LEN = 2048
CALIB_SAMPLES = 32
OUTPUT_PATH = "/root/distill_sparse_swiglu/artifacts/gsm8k_gen_compare.txt"
SEED = 42


def best_attn_impl():
    if importlib.util.find_spec("flash_attn"):
        return "flash_attention_2"
    return "sdpa"


def global_topk_masks(layer_scores, sparsity_target):
    items = sorted(layer_scores.items())
    normalized = []
    for li, s in items:
        s_f = s.float()
        mu = s_f.mean()
        normalized.append((li, s_f / mu if mu > 1e-12 else s_f))
    all_s = torch.cat([s for _, s in normalized])
    num_keep = int(len(all_s) * (1.0 - sparsity_target))
    thr = torch.topk(all_s, num_keep).values[-1]
    return {li: (s >= thr).to(torch.bfloat16) for li, s in normalized}


def teal_global_masks(wrapper, input_ids, sparsity_target, calib_batch_size=4):
    accum_scores = {}
    n_batches = 0
    for start in range(0, input_ids.size(0), calib_batch_size):
        batch = input_ids[start:start + calib_batch_size]
        wrapper.forward_dense(batch, capture_intermediates=True)
        intermediates = wrapper.get_intermediates()
        layer_inputs = wrapper.get_layer_inputs()
        with torch.no_grad():
            for layer_idx in range(len(wrapper.predictors)):
                if layer_idx not in layer_inputs or layer_idx not in intermediates:
                    continue
                logits = wrapper.predictors[layer_idx](layer_inputs[layer_idx])
                hard_mask = (logits > 0).float()
                mag = intermediates[layer_idx].abs().float()
                scores = (mag * hard_mask).mean(dim=(0, 1))
                if layer_idx not in accum_scores:
                    accum_scores[layer_idx] = scores
                else:
                    accum_scores[layer_idx] = accum_scores[layer_idx] + scores
        n_batches += 1
    layer_scores = {li: accum_scores[li] / n_batches for li in sorted(accum_scores)}
    return global_topk_masks(layer_scores, sparsity_target)


def apply_static_masks(model, global_masks, device):
    for layer_idx, layer in enumerate(model.model.layers):
        if layer_idx not in global_masks:
            continue
        mask = global_masks[layer_idx].to(device=device, dtype=layer.mlp.gate_proj.weight.dtype)
        mlp = layer.mlp

        def make_masked_fwd(gp, up, dp, af, m):
            def fwd(x):
                intermediate = af(gp(x)) * up(x)
                return dp(intermediate * m.unsqueeze(0).unsqueeze(0))
            return fwd

        layer.mlp.forward = make_masked_fwd(
            mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn, mask
        )


def restore_original_forwards(model):
    for layer in model.model.layers:
        mlp = layer.mlp
        gp, up, dp, af = mlp.gate_proj, mlp.up_proj, mlp.down_proj, mlp.act_fn

        def _make_orig(g, u, d, a):
            def fwd(x):
                return d(a(g(x)) * u(x))
            return fwd

        layer.mlp.forward = _make_orig(gp, up, dp, af)


def format_gsm8k_prompt(question):
    return f"Question: {question}\nLet's solve this step by step.\n"


@torch.no_grad()
def generate_text(model, tokenizer, prompt, device, max_new_tokens=256):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output_ids = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        temperature=None,
        top_p=None,
    )
    new_tokens = output_ids[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True)


def main():
    device = torch.device("cuda:0")
    random.seed(SEED)

    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        device_map={"": device},
        attn_implementation=best_attn_impl(),
    )
    model.eval()

    print("Loading GSM8K dataset...")
    gsm8k = load_dataset("openai/gsm8k", "main", split="test")
    indices = random.sample(range(len(gsm8k)), NUM_SAMPLES)
    samples = [gsm8k[i] for i in indices]

    # --- Dense generation ---
    print("Generating dense outputs...")
    dense_outputs = []
    for i, sample in enumerate(samples):
        prompt = format_gsm8k_prompt(sample["question"])
        output = generate_text(model, tokenizer, prompt, device, MAX_NEW_TOKENS)
        dense_outputs.append(output)
        print(f"  Dense sample {i+1}/{NUM_SAMPLES} done")

    # --- Compute TEAL masks ---
    print("Loading predictor and computing TEAL masks...")
    wrapper = PredictorWrapper(model, bottleneck_size=128)
    ckpt = torch.load(PREDICTOR_PATH, map_location=device, weights_only=True)
    wrapper.predictors.load_state_dict(ckpt["predictors"])
    wrapper.predictors.to(device=device, dtype=torch.bfloat16)
    wrapper.predictors.eval()
    wrapper.gumbel_mask.hard = True

    calib_data = get_eval_dataset("wikitext2", tokenizer, SEQ_LEN)
    n_calib = min(CALIB_SAMPLES, len(calib_data))
    calib_ids = torch.stack([calib_data[i]["input_ids"] for i in range(n_calib)]).to(device)
    print(f"  Using {n_calib} calibration sequences")

    global_masks = teal_global_masks(wrapper, calib_ids, SPARSITY_TARGET)

    total_n = sum(m.numel() for m in global_masks.values())
    total_z = sum((m == 0).sum().item() for m in global_masks.values())
    actual_sp = total_z / total_n
    print(f"  Actual sparsity: {actual_sp:.3f}")

    # Restore original forwards (PredictorWrapper patched them), then apply static masks
    restore_original_forwards(model)
    apply_static_masks(model, global_masks, device)
    print("  Static masks applied.")

    del wrapper, ckpt, calib_ids, calib_data
    torch.cuda.empty_cache()

    # --- Sparse generation ---
    print("Generating sparse outputs...")
    sparse_outputs = []
    for i, sample in enumerate(samples):
        prompt = format_gsm8k_prompt(sample["question"])
        output = generate_text(model, tokenizer, prompt, device, MAX_NEW_TOKENS)
        sparse_outputs.append(output)
        print(f"  Sparse sample {i+1}/{NUM_SAMPLES} done")

    # --- Write comparison output ---
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    lines = []
    lines.append("=" * 80)
    lines.append("GSM8K Generation Comparison: Dense vs KL Sparse 50%")
    lines.append(f"Model: {MODEL_PATH}")
    lines.append(f"Predictor: {PREDICTOR_PATH}")
    lines.append(f"Sparsity target: {SPARSITY_TARGET}, actual: {actual_sp:.3f}")
    lines.append(f"Samples: {NUM_SAMPLES}, max_new_tokens: {MAX_NEW_TOKENS}")
    lines.append("=" * 80)

    for i, sample in enumerate(samples):
        lines.append(f"\n{'─' * 80}")
        lines.append(f"SAMPLE {i+1} (index={indices[i]})")
        lines.append(f"{'─' * 80}")
        lines.append(f"\n[QUESTION]\n{sample['question']}")
        lines.append(f"\n[GROUND TRUTH]\n{sample['answer']}")
        lines.append(f"\n[DENSE OUTPUT]\n{dense_outputs[i]}")
        lines.append(f"\n[SPARSE OUTPUT]\n{sparse_outputs[i]}")

    output_text = "\n".join(lines) + "\n"
    with open(OUTPUT_PATH, "w") as f:
        f.write(output_text)
    print(f"\nResults saved to {OUTPUT_PATH}")
    print("\n" + output_text)


if __name__ == "__main__":
    main()
