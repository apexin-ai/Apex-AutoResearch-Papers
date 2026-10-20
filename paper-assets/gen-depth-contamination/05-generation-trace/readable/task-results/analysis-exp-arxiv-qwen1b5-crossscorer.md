# analysis exp arXiv qwen1b5 crossscorer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_arXiv_qwen1b5_crossscorer_20260518T030331_result.json`
- **Structured JSON:** [`41f977606288b757a503.json`](../../sessions/41/41f977606288b757a503.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册（`art_20260518_f5197e`）。核心结论：

- **arXiv K\*=3 scorer-independent confirmed.** Pythia-1.4B cross-scorer 下 K\* 保持 3，关键 AUC(2v3)=0.6317 > theta=0.60，5 fold 全部达标（最低 0.6157）。
- **与 Wikipedia 形成对照。** Wiki K\*=2→1（scorer artifact），arXiv K\*=3→3（genuine signal）。
- **AUC 衰减集中在浅层边界**（0v1: -0.02, 1v2: -0.05），深层边界（3v4, 4v5）几乎无变化，说明 cross-family tokenizer mismatch 只影响绝对灵敏度，不改变结构模式。

---
