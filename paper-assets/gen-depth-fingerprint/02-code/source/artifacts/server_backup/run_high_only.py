"""
Run only high_t10_p095 config on a separate GPU.
Phases: generate -> features (skip evaluate, needs all configs).
"""
import sys
sys.path.insert(0, "/root/gen-depth-fingerprint")

import sampling_ablation as sa
import torch

DEVICE = torch.device("cuda:0")  # CUDA_VISIBLE_DEVICES=2 maps to cuda:0

print(f"=== HIGH-TEMP ONLY on {DEVICE} ===")
print(f"Config: temperature=1.0, top_p=0.95")
print(f"Output: {sa.DATA_DIR / 'qwen3-1.7b-high-temp'}")
print()

# Phase 1: Generation (high only)
print("=" * 60)
print("PHASE 1: Generation (high_t10_p095 only)")
print("=" * 60)

from transformers import AutoModelForCausalLM, AutoTokenizer

print("Loading Qwen3-1.7B-Base...")
gen_tokenizer = AutoTokenizer.from_pretrained(
    sa.GENERATOR_MODEL, trust_remote_code=True)
gen_model = AutoModelForCausalLM.from_pretrained(
    sa.GENERATOR_MODEL, dtype=torch.float16, trust_remote_code=True
).to(DEVICE)
gen_model.eval()
if gen_tokenizer.pad_token is None:
    gen_tokenizer.pad_token = gen_tokenizer.eos_token
print(f"Model on {DEVICE}")

seeds = sa.load_seeds(sa.SEED_FILE, gen_tokenizer)
print(f"Loaded {len(seeds)} seeds")

cfg_name = "high_t10_p095"
cfg = sa.CONFIGS[cfg_name]
print(f"\n--- {cfg_name}: T={cfg['temperature']}, p={cfg['top_p']} ---")
torch.manual_seed(sa.SEED)
torch.cuda.manual_seed(sa.SEED)
sa.run_generation(cfg_name, cfg, seeds, gen_model, gen_tokenizer, DEVICE)

del gen_model, gen_tokenizer
torch.cuda.empty_cache()
print("\nGeneration complete\n")

# Phase 2: Feature Extraction (high only)
print("=" * 60)
print("PHASE 2: Feature Extraction (high_t10_p095 only)")
print("=" * 60)

print("Loading Pythia-410M reference model...")
ref_tokenizer = AutoTokenizer.from_pretrained(sa.REFERENCE_MODEL, local_files_only=True)
ref_model = AutoModelForCausalLM.from_pretrained(
    sa.REFERENCE_MODEL, local_files_only=True, torch_dtype=torch.float16
).to(DEVICE).eval()
if ref_tokenizer.pad_token is None:
    ref_tokenizer.pad_token = ref_tokenizer.eos_token
print(f"Reference model on {DEVICE}")

sa.extract_features_for_config(cfg_name, cfg, ref_tokenizer, ref_model, DEVICE)

del ref_model, ref_tokenizer
torch.cuda.empty_cache()

print("\n=== HIGH-TEMP DONE ===")
print("Features saved. Run evaluate phase separately after all configs finish.")
