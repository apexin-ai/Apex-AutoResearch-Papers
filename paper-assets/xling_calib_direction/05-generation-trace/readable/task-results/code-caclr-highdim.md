# code caclr highdim

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_caclr-highdim_20260521T090055_result.json`
- **Structured JSON:** [`37f49155205d25d8c546.json`](../../sessions/37/37f49155205d25d8c546.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法和 CLI 均通过。

`code/caclr_highdim.py` 已创建，支持：
- **3 种对齐方法**：`mmd_highdim`（PCA 空间 Gaussian RBF MMD）、`coral`（PCA 空间 CORAL loss，Sun & Saenko 2016）、`mmd_1d`（原始 1-D probe logits MMD baseline）
- **PCA**：在英语 train set 上 fit，transform 应用到所有语言，默认 d=50/100
- **Probe**：2-layer MLP (input_dim → 256 → 1)，支持 LR baseline
- **训练**：Adam + α×β grid sweep + early stopping on validation SB-ECE
- **评估**：AUROC / SB-ECE(15 bins) / Brier，per-language per-layer
- **输出**：per-condition JSON + comparison.json + report.txt
- **数据格式**：兼容 train_probes.py 的 npy/pt_split/pt_flat 三种格式

---
