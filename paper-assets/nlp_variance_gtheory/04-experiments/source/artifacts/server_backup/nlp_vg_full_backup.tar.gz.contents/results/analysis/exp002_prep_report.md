# exp-002 Multi-Benchmark Infrastructure Prep Report

Generated: 2026-05-21

---

## 1. Data Status

| Benchmark | HF Dataset | Split | Total Items | Sampled | Format | Size on Disk |
|-----------|-----------|-------|-------------|---------|--------|-------------|
| MMLU | cais/mmlu | test | ~14,042 (57 subjects) | 200 (exp-001) | 4-choice MC (A/B/C/D) | Already cached |
| GSM8K | openai/gsm8k | test | 1,319 | 200 | Open-ended generation (numerical) | ~2.3 MB |
| ARC-Challenge | allenai/ai2_arc | test | 1,172 | 200 | MC (3-5 choices, mostly 4) | ~1.5 MB |
| HellaSwag | Rowan/hellaswag | validation | 10,042 | 200 | 4-choice MC | ~30 MB |

All datasets downloaded to `/root/autodl-tmp/.hf_cache/hub/`.
Sampled item files in `/root/nlp_variance_gtheory/data/`:
- `gsm8k_items_exp002.json` (174 KB)
- `arc_items_exp002.json` (114 KB)
- `hellaswag_items_exp002.json` (142 KB)

---

## 2. Code Compatibility Analysis

### 2.1 `src/data/prompt_templates.py` — **Major changes needed**

| Issue | Detail | Affected Benchmarks |
|-------|--------|-------------------|
| Hardcoded 4 choices (A/B/C/D) | All 6 templates use `{A}`, `{B}`, `{C}`, `{D}` placeholders | ARC (3/5-choice items), GSM8K (no choices) |
| `ANSWER_MAP = {0:"A", 1:"B", 2:"C", 3:"D"}` | Only maps 4 indices | ARC (up to 5 choices) |
| `subject` parameter in all templates | MMLU-specific | GSM8K, ARC, HellaSwag |
| No generation-style templates | All templates expect MC answer | GSM8K (needs CoT generation prompt) |

**Required changes:**
1. New GSM8K template set: generation-style with "solve step by step" instruction, no MC choices
2. Extend choice formatting to handle 3-5 choices dynamically
3. Add HellaSwag templates with completion-style format (context + endings)
4. Make `subject` parameter optional; add `benchmark` parameter
5. Extend `ANSWER_MAP` to handle indices 0-4

**Effort: ~2 days**

### 2.2 `src/inference/run_experiment.py` — **Major changes needed**

| Issue | Detail |
|-------|--------|
| `extract_answer()` | Only matches `^[A-Da-d]`. GSM8K needs numerical extraction from CoT (`#### N` pattern or last number) |
| `few_shot[subject][str(ordering)]` | Keyed by MMLU subject. Other benchmarks have no subject hierarchy |
| Scoring: `ANSWER_MAP[item["answer_idx"]]` | Assumes letter comparison. GSM8K needs numerical equivalence check |
| `item["subject"]` used throughout | MMLU-specific field. Need `item["benchmark"]` routing |
| Single `--items` file | Need per-benchmark item loading or unified format |
| Record output: `"subject"` field | Need `"benchmark"` field |

**Required changes:**
1. Benchmark-aware answer extraction: MC vs. generation
2. Refactor few-shot loading: per-benchmark few-shot bank, or skip for benchmarks without few-shot
3. Benchmark-aware scoring logic
4. Add `--benchmark` CLI argument and routing logic
5. Update output record schema with `benchmark` field

**Effort: ~3 days**

### 2.3 `src/inference/vllm_runner.py` — **Minor change**

| Issue | Detail |
|-------|--------|
| `max_tokens=16` hardcoded in `SamplingParams` | Fine for MC, too short for GSM8K (needs 256-512 for CoT) |

**Required change:** Make `max_tokens` a parameter (passed from `run_experiment.py`, benchmark-dependent).

**Effort: ~0.5 day**

### 2.4 `src/design/generate_design.py` — **Moderate changes**

| Issue | Detail |
|-------|--------|
| No `benchmark` factor | Need to add as crossed factor |
| 3 precision levels | exp-002 uses 2 (bf16, fp16) |
| 3 temperature configs | exp-002 uses 2 (0.0, 0.7) |
| `ordering` factor | MMLU-specific (few-shot ordering). Unclear if applicable to GSM8K |

**Required changes:**
1. Add `benchmark` factor: ["mmlu", "gsm8k", "arc_challenge", "hellaswag"]
2. Update precision levels to [bf16, fp16]
3. Update temperature configs to [0.0, 0.7/top_p=0.9]
4. Decide ordering strategy per benchmark (keep for MC, potentially drop for GSM8K)

**Effort: ~0.5 day**

### 2.5 `src/data/few_shot.py` — **New development needed**

Current implementation is MMLU-specific (generates per-subject few-shot examples with 4 orderings).

**Required changes:**
1. ARC-Challenge: create few-shot examples from train split, 4 orderings
2. HellaSwag: create few-shot examples from train split, 4 orderings
3. GSM8K: create few-shot CoT examples from train split, or use 0-shot

**Effort: ~1.5 days**

### Summary: Total Estimated Adaptation Effort

| Module | Effort |
|--------|--------|
| prompt_templates.py | 2 days |
| run_experiment.py | 3 days |
| vllm_runner.py | 0.5 day |
| generate_design.py | 0.5 day |
| few_shot.py (new per-benchmark) | 1.5 days |
| Testing & integration | 1 day |
| **Total** | **~8.5 days** |

---

## 3. Sampling Results

### GSM8K — Stratified by Difficulty (step-count proxy)

| Difficulty | Steps | Sampled |
|-----------|-------|---------|
| easy | 1-2 | 50 |
| medium | 3-4 | 50 |
| hard | 5-6 | 50 |
| very_hard | 7+ | 50 |
| **Total** | | **200** |

### ARC-Challenge — Stratified by Number of Choices

| Choices | Sampled | % of test set |
|---------|---------|---------------|
| 4 | 193 | ~97% are 4-choice |
| 3 | 4 | ~2% |
| 5 | 3 | ~1% |
| **Total** | **200** | |

### HellaSwag — Stratified by Activity Label

- 200 items covering 192 unique activities (out of ~700+ in validation set)
- Most activities have 1 representative item; a few (e.g., "Personal Care and Style") have up to 6
- High diversity: near-maximum spread across activity types

---

## 4. Experiment Design Parameters

### exp-002 Factorial Design

| Factor | Levels | Count |
|--------|--------|-------|
| Model | Qwen3-8B, Llama-3.1-8B, Gemma-2-9B, Mistral-7B-v0.3 | 4 |
| Benchmark | MMLU, GSM8K, ARC-Challenge, HellaSwag | 4 |
| Precision | bf16, fp16 | 2 |
| Temperature | 0.0 (greedy), 0.7 (top_p=0.9) | 2 |
| Prompt template | 1-6 | 6 |
| Seed | 42, 123, 456, 789, 1024, 2048 | 6 |
| Ordering | 1-4 (few-shot ordering) | 4 |

### Calculations

- **Total conditions**: 4 × 4 × 2 × 2 × 6 × 6 × 4 = **9,216**
  - Per model: 2,304 conditions
  - Per model per benchmark: 576 conditions
- **Total inferences**: 9,216 × 200 = **1,843,200**
- **Total output records**: 1,843,200 JSONL rows

> **Note**: The task description stated 4,608 conditions; the correct full-factorial cross is 9,216.
> If ordering is dropped for GSM8K (no few-shot), conditions reduce to:
> - MC benchmarks (3): 4 × 3 × 2 × 2 × 6 × 6 × 4 = 6,912
> - GSM8K: 4 × 1 × 2 × 2 × 6 × 6 × 1 = 576 (no ordering)
> - Total: 7,488 conditions × 200 = 1,497,600 inferences

### GPU Time Estimation

**Reference**: exp-001 on westd-32570 (4× GPU)
- Qwen shard_0: 64,800 records in ~82 min on 1 GPU (including model load)
- Throughput: ~14 records/sec for MC (max_tokens=16)

**exp-002 estimates** (4 GPUs, models loaded sequentially):

| Component | Records | Throughput | Time (4 GPU) |
|-----------|---------|-----------|--------------|
| MC benchmarks (MMLU+ARC+HellaSwag) | 1,382,400 | ~14 rec/s/GPU | ~7 hours |
| GSM8K (generation, max_tokens≈256) | 460,800 | ~1-2 rec/s/GPU | ~16-32 hours |
| **Total** | **1,843,200** | | **~23-39 hours** |

### Cost Consideration

- GSM8K generation is the bottleneck: 10-15× slower per item than MC due to longer token generation
- Reducing GSM8K to 0-shot (dropping ordering factor) cuts GSM8K records from 460,800 to 115,200
- Alternative: use GSM8K with only 100 items (halve the work)

---

## 5. Open Design Questions

1. **GSM8K few-shot?** Using few-shot CoT with 4 orderings keeps the design balanced but multiplies cost. 0-shot CoT is common in the literature.
2. **ARC 3/5-choice items**: Only 7 of 200 items have non-4-choice format. Consider filtering to 4-choice only for cleaner design alignment with MMLU/HellaSwag.
3. **Ordering factor for generation tasks**: Does few-shot ordering matter for GSM8K? If not, can drop this factor for GSM8K to save ~75% of GSM8K compute.
4. **exp-002 precision**: Task specifies bf16/fp16 only (dropping float32). This is a reasonable reduction from exp-001's 3 levels, but loses the reference baseline.

---

## 6. File Inventory

```
data/
├── mmlu_items_exp001.json        # exp-001 MMLU items (200)
├── gsm8k_items_exp002.json       # exp-002 GSM8K items (200, stratified)
├── arc_items_exp002.json         # exp-002 ARC items (200, stratified)
├── hellaswag_items_exp002.json   # exp-002 HellaSwag items (200, stratified)

scripts/
├── sample_benchmarks.py          # Stratified sampling script (new)

src/data/
├── sample_benchmarks.py          # Simple random sampling (existing, not used for exp-002)
├── prompt_templates.py           # MMLU-only templates (needs adaptation)
├── few_shot.py                   # MMLU-only few-shot (needs per-benchmark versions)

src/inference/
├── run_experiment.py             # Main runner (needs multi-benchmark adaptation)
├── vllm_runner.py                # vLLM backend (needs configurable max_tokens)

src/design/
├── generate_design.py            # Design matrix (needs benchmark factor + param updates)
```
