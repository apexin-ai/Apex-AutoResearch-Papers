# exp-009: RL Observational Case Study

## Hypothesis
Instruct/RL-distilled models exhibit measurable contamination signals (gamma > 0) on benchmarks likely included in their training data, detectable via the same 2PL+gamma IRT framework validated on controlled SFT contamination.

## Models

| Model | Path | Status |
|-------|------|--------|
| Qwen2.5-0.5B-Instruct | `/root/autodl-tmp/models/Qwen/Qwen2.5-0.5B-Instruct` | Downloaded, eval done, signals done (exp002) |
| Qwen2.5-1.5B-Instruct | `/root/autodl-tmp/models/Qwen/Qwen2___5-1___5B-Instruct` | Downloaded, eval done, signals done (exp002) |
| Qwen2.5-3B-Instruct | `/root/autodl-tmp/models/Qwen/Qwen2___5-3B-Instruct` | Downloaded, eval done, **signals missing** |
| DeepSeek-R1-Distill-Qwen-1.5B | (not downloaded) | **Need download + eval + signals** |

Reference models for S2 (Min-K++):
- 0.5B-Instruct → `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-0___5B`
- 1.5B-Instruct → `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B`
- 3B-Instruct → `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-3B`
- DeepSeek-R1 → `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B` (base architecture)

## Benchmarks
MMLU, ARC-Challenge, GSM8K (same as main experiments)

## Signals
- S2 (Min-K++ sequence probability)
- S4 (Self-critique entropy collapse / calibration error)
- S1 (Embedding retrieval) — already computed for 0.5B/1.5B in exp002, compute for 3B/DeepSeek if time permits

## Existing Data Inventory

### Eval results (correctness matrices) — exp001
- `Qwen2.5-0.5B-Instruct_aligned/` — 3 benchmarks ✓
- `Qwen2.5-1.5B-Instruct_aligned/` — 3 benchmarks ✓
- `Qwen2.5-3B-Instruct_aligned/` — 3 benchmarks ✓ (acc: MMLU 0.508, GSM8K 0.760, ARC 0.832)
- DeepSeek-R1 — ✗ needs eval

### Signals — exp002
- `Qwen2.5-0.5B-Instruct/` — s1+s2+s4, 3 benchmarks ✓
- `Qwen2.5-1.5B-Instruct/` — s1+s2+s4, 3 benchmarks ✓
- 3B-Instruct — ✗ missing
- DeepSeek-R1 — ✗ missing

## Metrics
1. **gamma estimate** per model x benchmark (2PL+gamma posterior)
2. **gamma CI overlap** with SFT d000 (clean baseline) — separation = evidence of contamination
3. **Expected regret**: E[R_uncalibrated] - E[R_calibrated]
4. **Expected regret**: E[R_uncalibrated] - E[R_remove_rescore]
5. Comparison: Instruct gamma distribution vs SFT d005/d025/d100 gamma (where on the dosage curve?)

## Expected Results
- DeepSeek-R1-Distill-Qwen-1.5B: likely elevated gamma on GSM8K (known math training emphasis in R1 distillation)
- Qwen2.5-Instruct: moderate gamma across benchmarks, lower than SFT d100 but potentially overlapping d005-d025 range
- Expected regret should be positive (calibration helps for contaminated models)
- Key comparison: if Instruct gamma CI overlaps SFT d000, contamination is not detectable; if it separates, framework generalizes to real-world models

## GPU Plan (cuda:3,4,5)

### Phase 1: Download + Eval (~1-2h)
- cuda:3: Download DeepSeek-R1-Distill-Qwen-1.5B (huggingface-cli, ~3GB)
- cuda:3: Eval DeepSeek-R1 on 3 benchmarks (after download)

### Phase 2: Signal computation (~3-4h)
- cuda:3: 3B-Instruct signals (s2+s4, 3 benchmarks)
- cuda:4: DeepSeek-R1 signals (s2+s4, 3 benchmarks)
- cuda:5: (standby / overflow if needed)

### Phase 3: IRT fitting + analysis (~30min, CPU)
- Assemble correctness + exposure matrices for all 4 Instruct/RL models
- Fit 2PL+gamma per benchmark using `exp006/run_irt_calibration.py`
- Compute expected regret
- Compare gamma distributions with SFT baselines

## Script Reuse

| Step | Script | Adaptation needed |
|------|--------|-------------------|
| Eval (DeepSeek) | `exp001/` eval pipeline | Need to verify chat template handling for DeepSeek |
| Signal S2 | `exp008_new/compute_signals_on_model.py` | Direct use with `--model-path` |
| Signal S4 | Same as above | Direct use |
| IRT fitting | `exp006/run_irt_calibration.py` | Need to assemble input data for Instruct models |

## Prerequisites Before Launch
1. [x] Verify Instruct models downloaded
2. [ ] Download DeepSeek-R1-Distill-Qwen-1.5B
3. [ ] Verify eval scripts handle DeepSeek chat template (different from Qwen)
4. [ ] Confirm exp002 signal format compatible with exp006 IRT input
5. [ ] Verify GPU 3/4/5 are idle (nvidia-smi)

## Risk / Open Questions
- DeepSeek-R1-Distill uses a different chat template than Qwen — may need minor adaptation in eval script
- S4 selfcritique uses a generic template (not chat-formatted) — should work but quality may differ for instruct-tuned models
- If Instruct gamma is indistinguishable from d000 (clean SFT), the case study would be a null result — still publishable as "framework correctly identifies low/no contamination"

## IRT Exposure Construction Strategy

For controlled SFT models: exposure[i,j] = dosage[i] * tau[j] (known dosage, tau from signals).

For Instruct/RL models (unknown dosage), two approaches:
1. **Signal-as-exposure**: Use normalized s2/s4 signal scores directly as exposure. Gamma then measures how well signals predict performance inflation.
2. **Pool with SFT models**: Add Instruct models to the pooled respondent matrix alongside SFT models. Assign exposure = signal_score (s2 or aggregated). The pooled model shares item parameters, letting us compare gamma across model types on a common scale.

**Recommended**: Approach 2 (pooled). This leverages existing SFT calibration data as anchors and tests whether the same gamma mechanism explains Instruct model behavior.

## Command Templates

### Phase 1: Eval DeepSeek-R1
```bash
CUDA_VISIBLE_DEVICES=3 python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B \
  --benchmarks mmlu gsm8k arc_challenge \
  --output-dir /root/autodl-tmp/exp001/eval_results/DeepSeek-R1-Distill-Qwen-1.5B \
  --instruct \
  --mc-format aligned \
  --cache-dir /root/autodl-tmp/.hf_cache
```

### Phase 2a: 3B-Instruct Signals
```bash
CUDA_VISIBLE_DEVICES=3 python /root/contamcal-irt-calibration/exp008_new/compute_signals_on_model.py \
  --model-path /root/autodl-tmp/models/Qwen/Qwen2___5-3B-Instruct \
  --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-3B \
  --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl \
  --benchmarks mmlu gsm8k arc_challenge \
  --output-dir /root/autodl-tmp/exp009/signals/Qwen2.5-3B-Instruct \
  --gpu 0
```

### Phase 2b: DeepSeek-R1 Signals
```bash
CUDA_VISIBLE_DEVICES=4 python /root/contamcal-irt-calibration/exp008_new/compute_signals_on_model.py \
  --model-path /root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B \
  --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B \
  --sft-data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl \
  --benchmarks mmlu gsm8k arc_challenge \
  --output-dir /root/autodl-tmp/exp009/signals/DeepSeek-R1-Distill-Qwen-1.5B \
  --gpu 0
```

### Phase 3: IRT Fitting (after signals complete)
```bash
python /root/contamcal-irt-calibration/exp006/run_irt_calibration.py \
  --response-matrix /root/autodl-tmp/exp009/irt_input/response_matrix_{bench}.npy \
  --exposure-matrix /root/autodl-tmp/exp009/irt_input/exposure_matrix_{bench}.npy \
  --model-type 2pl_gamma \
  --output-dir /root/autodl-tmp/exp009/irt_results/{bench} \
  --chains 4 --warmup 1000 --samples 1000
```

## Key Script Compatibility Notes
- eval: `--instruct` flag needed for DeepSeek (auto-detected for Qwen by "instruct" in path)
- eval: `tokenizer.apply_chat_template()` handles both Qwen and DeepSeek chat formats natively
- signals: exp008_new/compute_signals_on_model.py takes --model-path directly (no adapter)
- signals: s4 selfcritique uses generic template, not chat-formatted — acceptable since we measure entropy not generation quality
- IRT: run_irt_calibration.py accepts --response-matrix + --exposure-matrix for direct input

## Timeline (optimistic)
- Model download: ~15min (3GB on fast network) — **IN PROGRESS** (tmux session dl_ds)
- DeepSeek eval: ~1h (3 benchmarks)
- Signal computation (3B + DeepSeek): ~3-4h parallel
- IRT fitting: ~30min
- Total: ~5-6h wall time
