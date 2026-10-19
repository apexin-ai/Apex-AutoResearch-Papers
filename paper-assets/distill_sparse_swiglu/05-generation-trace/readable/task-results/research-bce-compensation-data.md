# research bce compensation data

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bce_compensation_data_20260522T133603_result.json`
- **Structured JSON:** [`e767cc0b276f38a20047.json`](../../sessions/e7/e767cc0b276f38a20047.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已验证。memory.md 中的 "BCE Compensation Data" 段已经包含完整且准确的数据，与 registry.yaml 原始记录一致：

## 数据摘要

### 50% Sparsity
- **BCE + comp**: PPL = 25.44 (`bce_comp_staged_s42`, `predictor_hard_mask_ppl`)
- **BCE no comp**: PPL = 27.96 (`bce_comp_staged_s42`, `predictor_hard_mask_ppl_no_comp`；独立验证 `bce_50pct_teal_global_unified` = 27.97)
- **Δ = 2.52 pp** (comp 提升 ~9%)
- 稀疏度注意: BCE+comp 实际 0.558 vs KL baseline 0.498

### 30% Sparsity
- **BCE + comp**: 不存在（registry 中无 30% BCE+comp 实验）
- **BCE no comp (uniform, 3-seed)**: s42=14.95, s123=15.21, s456=15.11 (`bce_iso_v3_s{42,123,456}_30pct_uniform_eval`)
- **BCE no comp (global_topk)**: 11.24 (`bce_30pct_s42_eval`)
- 30% 的 Δ 无法计算（缺 comp 数据）

memory.md 已在之前的 session 中写入了完整的 "BCE Compensation Data" 段，数据全部可追溯到具体 exp_id，无需更新。

---
