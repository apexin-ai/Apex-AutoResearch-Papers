# writing cross scale section

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_cross_scale_section_20260516T060926_result.json`
- **Structured JSON:** [`afea93525672d2736bb9.json`](../../sessions/af/afea93525672d2736bb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§4.6 已写入 `generalization.tex`（lines 152-213）。内容包含：

- **Intro**: 引入 scale 维度，说明 Qwen2.5-7B 实验设置
- **Table 1** (`tab:cross_scale`): 4-class acc + EDD + d0v1 AUC 跨规模对比
- **Finding (1)**: 60.1% vs 25% chance，d0 separability preserved (AUC>0.92)
- **Finding (2)**: EDD 随规模增大 (EDD>5 at T=0.70 vs EDD=4 for 1-1.5B)
- **Table 2** (`tab:cross_scale_auc`): 完整 consecutive binary AUC
- **Finding (3)**: Non-monotonic U-shape caveat，含 formulaic degradation hypothesis
- **Caveats**: CI lower bound、non-uniform signal、instruction-tuning confound、Llama-3 待验证

严格遵循了 Director 约束：未声称 monotonic decay 在 7B 复现，未说 pairwise AUC 衰减趋势一致。`% TODO: Add Llama-3-8B results when available` 占位已留。所有数值追溯 `cross_scale_qwen7b_001`，provenance 已注册。

---
