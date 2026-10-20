# paper writing experiments

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260518T032841_result.json`
- **Structured JSON:** [`333b98dac701a807e0e4.json`](../../sessions/33/333b98dac701a807e0e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Complete. Here's a summary of what was written:

**experiments.tex** (full rewrite, 8 subsections):
- **§4.1 Setup**: Base model, 4 pruning methods (CKA-only/Random/Standard/RASP), GRPO v5 config (beta=0.01, temp=0.4), hardware
- **§4.2 Recovery Capacity Gradient**: Central finding with Table 1 + Figure 2 + Figure 3. CKA-only >> Random >> Standard > RASP, 5.8x peak reward gap
- **§4.3 Reward-Accuracy Decoupling**: Table 2, GRPO reward ≠ accuracy across all configs
- **§4.4 SFT Gradient**: CKA-only 63.91% > RASP 61.49% > Standard 59.29%
- **§4.5 Sparsity Cliff**: Table 4, universal collapse at 30%
- **§4.6 Inference**: Table 5, RASP 37.8% vs Standard 7.7% speedup
- **§4.7 Ablation**: Table 3 updated with new alpha values (0.0/0.25/0.5/1.0/2.0)
- **§4.8 Discussion**: Gradient importance as harmful signal for RLVR recovery

**5 table files** created/updated:
- `tab1_recovery_gradient.tex` (new)
- `tab2_decoupling.tex` (new)
- `table3_alpha.tex` (updated with new data)
- `table4_sparsity_cliff.tex` (updated formatting)
- `table5_inference.tex` (updated formatting)

**Figures directory** created at `figures/paper/` (PDFs not yet generated).

Old table files (`table1_postprune.tex`, `table2_recovery.tex`) are no longer referenced but remain on disk.

---
