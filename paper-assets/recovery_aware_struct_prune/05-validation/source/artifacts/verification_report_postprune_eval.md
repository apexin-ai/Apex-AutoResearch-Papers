# Post-Prune Eval Verification Report

**Date:** 2026-05-15  
**Server:** westb-23072  
**Eval script:** `src/eval_gsm8k.py` (commit `e6ce5f7`, 2026-05-15 03:56)  
**Model loader:** `src/model_utils.py::load_pruned_model` — correct non-uniform handling via `from_config` + per-layer resize + `strict=True`

---

## 1. Re-eval Results (Current Code, GPU, 20 samples, greedy, max_new_tokens=512)

| Model | Accuracy | N | EOS Rate | Avg Len | Correct Samples |
|-------|----------|---|----------|---------|-----------------|
| pruned_standard_20 | **0.40 (8/20)** | 20 | 0.65 | 399 | [2,3,8,13,15,17,18,19] |
| pruned_rasp_20 | **0.40 (8/20)** | 20 | 0.65 | 386 | [2,3,7,8,13,15,17,18] |

Both models produce **coherent step-by-step reasoning**. 7 of 8 correct samples overlap.

Output files:
- `/root/autodl-tmp/recovery_aware_struct_prune/results/reeval_standard_20_gpu1.json`
- `/root/autodl-tmp/recovery_aware_struct_prune/results/reeval_rasp_20_gpu0.json`

---

## 2. Comparison with Original Numbers

| Eval | Standard | RASP | Code Version | Notes |
|------|----------|------|-------------|-------|
| Quick eval (reported) | **1%** (1/100) | **29%** (28/100) | Pre-commit (< 03:56) | Relative paths `models/pruned_*` |
| Full eval (GPU1 log) | **23%** (23/100) | N/A | Post-commit | Sequential samples, absolute paths |
| **Re-eval (this report)** | **40%** (8/20) | **40%** (8/20) | Post-commit | Shuffled 20, seed=42 |

**Key: The 29% vs 1% gap is an artifact of the pre-commit eval code.**

---

## 3. Root Cause Analysis

### What went wrong with the quick eval (1% Standard)?

1. **Different code version**: Quick evals ran at 00:15 (RASP) and 01:00 (Standard), **before** the git initial commit at 03:56. The current `eval_gsm8k.py` outputs `mode`, `stderr`, `eos_stats`, `temperature`, `do_sample` fields — all absent from the quick eval JSONs. The quick eval used a different code version.

2. **Quick eval Standard output is degenerate**: All responses are repeating tokens ("10 years, 10 years, 10 years..."), random digit strings ("10000000..."), or looping phrases. This is characteristic of a model with reinitialized weights or broken loading.

3. **Quick eval RASP output is coherent**: Real reasoning, structured answers. This rules out `from_pretrained` as the sole cause (both models have the same non-uniform structure and would fail equally).

4. **Most likely scenario**: The eval code was modified between the RASP eval (00:15) and Standard eval (01:00). RASP was evaluated with working `load_pruned_model`, then the code was changed (possibly to test `from_pretrained`), and Standard was evaluated with the broken version. No git history exists to prove this since the initial commit is at 03:56.

### from_pretrained hypothesis (verified)

Confirmed via `/tmp/test_from_pretrained.py`: using `AutoModelForCausalLM.from_pretrained` on either model causes **size mismatch errors** for layers 6-27 MLP weights. With `ignore_mismatched_sizes=True`, those layers get reinitialized → degenerate output. This matches the Standard quick eval behavior perfectly.

However, this would also break RASP equally, so the eval code change between runs is the more complete explanation.

---

## 4. Current Code Correctness

`load_pruned_model` is correct:
- Reads `per_layer_intermediate_size` from config
- Sets `config.intermediate_size = max(per_layer_sizes)` to create model skeleton
- Resizes each layer's MLP dimensions individually
- Loads state_dict with `strict=True` (no silent mismatches)
- `device_map="cpu"` skips `.cuda()`, `device_map="auto"` calls `.cuda()`

Both models load successfully with `strict=True` — all tensor shapes match.

---

## 5. Conclusion

| Claim | Status |
|-------|--------|
| RASP 29% post-prune accuracy | **Verified** (re-eval: 40% on 20 samples, consistent with 29% on 100) |
| Standard 1% post-prune accuracy | **REFUTED** — artifact of pre-commit eval bug. True accuracy: **~23-40%** |
| 28pp RASP-Standard gap | **REFUTED** — true gap is **~0-10pp** (likely ~6pp based on 23% vs 29% full evals) |
| Current eval code correctness | **Verified** — `load_pruned_model` handles non-uniform MLP correctly |

### Impact on paper thesis

The core claim that "CKA-guided RASP pruning preserves significantly more recoverable structure" rests on a ~28pp post-prune accuracy gap that **does not exist**. The true gap is much smaller (~6pp or less). The downstream SFT/GRPO recovery experiments may still show meaningful differences, but the pruning-stage advantage is far weaker than reported.

### Recommended next steps

1. Run full 100-sample re-eval for both models (once GPU available) to get tighter confidence intervals
2. Verify SFT recovery numbers (sft_standard_20: 64%, sft_rasp_20: 57%) — note Standard already outperforms RASP post-SFT
3. Re-examine whether the paper's thesis holds with corrected numbers
