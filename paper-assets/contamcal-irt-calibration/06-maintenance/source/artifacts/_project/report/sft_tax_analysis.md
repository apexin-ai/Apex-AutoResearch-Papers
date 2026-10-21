# SFT Tax Analysis: Pre-training vs Post-SFT d000 Baseline

**Date**: 2026-05-22
**Definition**: SFT tax = Pre-training MMLU baseline (raw base model) − d000 Post-SFT MMLU baseline (clean SFT, 0% contamination). Positive = SFT degraded MMLU.

## MMLU 5-shot

| Model Family | Pre-training Baseline | d000 Post-SFT | SFT Tax (Δ) | Pre-training Source | d000 Source |
|---|---|---|---|---|---|
| Phi-4 14.7B | 84.8% | 76.44% | **+8.36 pp** | Phi-4 Technical Report (arXiv:2412.08905) | registry: memory.md 6-family summary |
| Qwen2.5-14B | 79.7% | 69.44% | **+10.26 pp** | Qwen2.5 Technical Report (arXiv:2412.15115) | registry: memory.md 6-family summary |
| Qwen2.5-7B | 74.2% | 66.11% | **+8.09 pp** | Qwen2.5 Technical Report (arXiv:2412.15115) | registry: memory.md 6-family summary |
| Gemma-2 9B | 71.3% | 61.86% | **+9.44 pp** | Gemma 2 Technical Report (arXiv:2408.00118) | registry: memory.md 6-family summary |
| Falcon3-7B-Base | 67.4% | 58.77% | **+8.63 pp** | Falcon 3 Blog (TII, falcon-lm.github.io) | registry: eval_falcon3_d000_s42_v2 |
| LLaMA-3.1 8B | 66.7% | 53.50% | **+13.20 pp** | Meta eval_details.md (github.com/meta-llama) | registry: memory.md LLaMA-3 validation |
| OLMo-2 7B | 63.7% | 53.79% | **+9.91 pp** | OLMo 2 Paper (AI2, arXiv:2501.00656) | registry: memory.md 6-family summary (rerun verified) |

**Mean SFT Tax**: 9.70 pp (std: 1.64 pp)
**Range**: 8.09 pp (Qwen2.5-7B) to 13.20 pp (LLaMA-3.1 8B)

## Key Findings

1. **Universal SFT tax**: All 7 families show positive SFT tax (8–13 pp). LoRA SFT on QA-format data consistently degrades MMLU 5-shot performance relative to the raw base model.

2. **LLaMA-3.1 is an outlier** (13.20 pp, 1.5 std above mean). Possible causes: (a) LLaMA-3.1 architecture is more sensitive to LoRA-based SFT; (b) format mismatch between SFT data and LLaMA-3.1's pretraining distribution; (c) LLaMA-3.1's tokenizer handling of MC options differs.

3. **Qwen2.5-14B has the second-highest tax** (10.26 pp) despite being the largest Qwen model tested. The Collapse pattern observed at d100 (−15.70 pp) compounds on top of this already-high SFT tax, giving a total gap of ~26 pp between pre-training baseline and d100.

4. **Tax magnitude does not predict contamination pattern**: Phi-4 (tax=8.36, Immune), Qwen-14B (tax=10.26, Collapse), OLMo-2 (tax=9.91, Benefit) all have similar SFT taxes but radically different contamination responses.

5. **No clear correlation with model size**: The 14.7B Phi-4 (8.36 pp) has lower tax than 7B OLMo-2 (9.91 pp). Architecture matters more than parameter count.

## Caveats

- **Format difference**: Published pre-training baselines use standard 5-shot completion format. d000 post-SFT uses 5-shot aligned MC format (instruction template + logprob MC extraction). Small systematic differences may exist, though both are 5-shot MMLU on identical item sets.
- **OLMo-2 pre-training score** (63.7%) derived from arXiv:2501.00656 Table 3. If AI2 used a different MMLU variant (e.g., OLMES), the number may not be directly comparable.
- **Falcon3 pre-training score** (67.4%) from the official blog; exact evaluation details (harness version, prompt template) not fully specified.
- All d000 post-SFT models use LoRA r=16, α=32, lr=5e-5, 1 epoch on sft_dosage_000.jsonl (clean QA data, 0% benchmark contamination).

## Sorted by SFT Tax (ascending)

| Rank | Model | SFT Tax | Contamination Pattern |
|------|-------|---------|----------------------|
| 1 | Qwen2.5-7B | 8.09 pp | V-recovery |
| 2 | Phi-4 14.7B | 8.36 pp | Immune |
| 3 | Falcon3-7B-Base | 8.63 pp | TBD (eval in progress) |
| 4 | Gemma-2 9B | 9.44 pp | Benefit |
| 5 | OLMo-2 7B | 9.91 pp | Benefit |
| 6 | Qwen2.5-14B | 10.26 pp | Collapse |
| 7 | LLaMA-3.1 8B | 13.20 pp | Immune |
