# Open LLM Leaderboard Data Availability Report

**Date**: 2026-05-20  
**Experiment**: exp-leaderboard-data-recon  
**Objective**: Determine whether per-item binary response data is available from the Open LLM Leaderboard for large-scale person-fit (lz*) analysis.

---

## 1. Conclusion

**Per-item binary response data IS available** from Open LLM Leaderboard v1, covering 13,000+ models across 4 of our 5 target benchmarks (MMLU, HellaSwag, ARC-Challenge, GSM8K). HumanEval is not covered. Zero GPU-hours needed for the bulk of the analysis.

---

## 2. Data Format

### v1 Details Datasets (Primary Source)

**Location**: `open-llm-leaderboard-old/details_{org}__{model_name}` on HuggingFace  
**Format**: Parquet (via HF Datasets library)  
**Granularity**: One row per question per model

**Fields per item**:
| Field | Type | Description |
|-------|------|-------------|
| `example` | string | Question text |
| `choices` | list[string] | Answer options |
| `gold` | int | Correct answer index |
| `predictions` | list[float] | Model log-probabilities per choice |
| `acc` | float | Binary accuracy (0 or 1) |
| `acc_norm` | float | Length-normalized accuracy (0 or >0) |

**Binary response derivation**: `acc > 0` or `acc_norm > 0` → correct (1), else incorrect (0).

**Loading example**:
```python
from datasets import load_dataset

# Load MMLU abstract algebra results for a specific model
data = load_dataset(
    "open-llm-leaderboard-old/details_meta-llama__Llama-2-7b-hf",
    "harness_hendrycksTest_abstract_algebra_5",
    split="train"
)
```

Each task has its own configuration name:
- ARC-Challenge: `harness_arc_challenge_25`
- HellaSwag: `harness_hellaswag_10`
- MMLU subtasks: `harness_hendrycksTest_{subtask}_5` (57 subtasks)
- GSM8K: `harness_gsm8k_5`
- Winogrande: `harness_winogrande_5`
- TruthfulQA: `harness_truthfulqa_mc_0`

**Confirmed by**: ZenoML tutorial (https://zenoml.com/docs/tutorials/leaderboard/) which loads and visualizes per-item data from these datasets.

---

## 3. Coverage

### Open LLM Leaderboard v1 (archived June 2024)
- **Models**: 13,000+ (evaluated over 2 years on 8×H100 cluster)
- **Benchmarks**: 6 total
  - ✅ MMLU (5-shot, 57 subtasks, 14,042 items) — matches our PSN-IRT data
  - ✅ HellaSwag (10-shot, 10,042 items) — matches
  - ✅ ARC-Challenge (25-shot, ~1,172 items) — matches (our data has 295 items, subset)
  - ✅ GSM8K (5-shot, 1,319 items) — matches
  - ❌ HumanEval — NOT in v1 benchmarks
  - ⚠️ TruthfulQA (0-shot) — not in our current analysis but available
  - ⚠️ Winogrande (5-shot) — not in our current analysis but available

### Open LLM Leaderboard v2 (current, since June 2024)
- **Models**: 4,580+ models
- **Benchmarks**: BBH, GPQA, IFEval, MATH Hard, MMLU-PRO, MUSR
- **Per-item data**: Also has `details` datasets per model (same pattern: `open-llm-leaderboard/{model}-details`)
- **Relevance**: Low for our project — different benchmarks from PSN-IRT data. MMLU-PRO is related to MMLU but is a harder variant with different items.

---

## 4. GPU Budget Impact

### If using v1 data (recommended): ~0 GPU-hours
The per-item data already exists for 13K models. We only need compute for:
- Downloading and parsing parquet files (CPU only, minutes)
- IRT parameter estimation and lz* computation (CPU only, minutes per model)

### If running inference ourselves (fallback for HumanEval or custom models):

**lm-eval-harness with `--log_samples`** outputs per-item JSONL with binary `exact_match` (0/1) field.

Estimated inference time per model on single A100:
| Benchmark | Items | ~Time (7B model) |
|-----------|-------|-------------------|
| MMLU (57 subtasks) | 14,042 | ~2 hours |
| HellaSwag | 10,042 | ~10 min |
| GSM8K | 1,319 | ~5 min |
| ARC-Challenge | 1,172 | ~5 min |
| HumanEval | 164 | ~5 min |
| **Total per 7B model** | | **~2.5 GPU-hrs** |

Scaling estimates:
| Scenario | GPU-hours |
|----------|-----------|
| 20 models (7B), HumanEval only | ~2 GPU-hrs |
| 20 models (7B), all benchmarks | ~50 GPU-hrs |
| 50 mixed-size models, all benchmarks | ~200-500 GPU-hrs |

---

## 5. Recommendations

### Optimal Strategy (minimal GPU cost)

1. **Download v1 per-item data** for a curated set of models (e.g., top-50 by different criteria, known contaminated models, diverse architectures). Script needed to:
   - Enumerate available `details` datasets under `open-llm-leaderboard-old/`
   - Load per-task splits and extract binary response vectors
   - Align items with our existing IRT parameters from PSN-IRT

2. **Item alignment check**: Verify that question IDs/content in v1 details match our PSN-IRT item parameters. The v1 leaderboard used the same lm-eval-harness version as PSN-IRT, so item ordering should be deterministic.

3. **For HumanEval**: Run lm-eval-harness ourselves with `--log_samples` on selected models. Only 164 items, ~5 min per 7B model.

4. **Scale**: Start with ~50 well-known models from v1, compute lz* using our existing 4PL parameters, then expand if results are promising.

### Key Risks
- **Item ordering**: Must verify that v1 details items align 1:1 with our IRT parameter items. Different lm-eval-harness versions may reorder items.
- **v1 models are older**: Most v1 models are from 2023-mid 2024. Newer models (post June 2024) are only on v2 with different benchmarks.
- **ARC-Challenge item count mismatch**: Our PSN-IRT data has 295 ARC-C items; standard ARC-Challenge has 1,172. Need to check which subset PSN-IRT used.

---

## 6. Data Sources

| Source | URL | Data Type |
|--------|-----|-----------|
| v1 Details (per model) | `huggingface.co/datasets/open-llm-leaderboard-old/details_{model}` | Per-item binary |
| v1 Results (aggregate) | `huggingface.co/datasets/open-llm-leaderboard-old/results` | Aggregate scores |
| v2 Details (per model) | `huggingface.co/datasets/open-llm-leaderboard/{model}-details` | Per-item (different benchmarks) |
| v2 Contents (aggregate) | `huggingface.co/datasets/open-llm-leaderboard/contents` | Aggregate scores |
| ZenoML Tutorial | `zenoml.com/docs/tutorials/leaderboard/` | Data format documentation |
| lm-eval-harness | `github.com/EleutherAI/lm-evaluation-harness` | `--log_samples` for self-run |
