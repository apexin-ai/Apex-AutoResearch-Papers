# audit fewnerd dals n mismatch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_fewnerd_dals_n_mismatch_20260518T072647_result.json`
- **Structured JSON:** [`931a01b50a0c9f117198.json`](../../sessions/93/931a01b50a0c9f117198.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部到位，整理结论。

## 结论

### 数据来源

| 指标 | n (gold-filtered) | 来源文件/目录 | n_samples | 备注 |
|------|---------|-------------|-----------|------|
| **+0.30pp** | **32,565** | `dals_hardening_results.json` → `fewnerd_n8`&lt;br>数据: `exp_021_inference/samples.jsonl` (37,648行, gold-filtered→32,565) | 8 | 全量 Few-NERD test set |
| **+1.08pp** | **4,351** | `fewnerd_dals_multiseed_results.json` → `task1_multiseed`&lt;br>数据: `exp_027_fewnerd_n16/samples.jsonl` (5,000行, gold-filtered→4,351) | 16 | 5K 子采样 |

### 关键发现

- **n=32,565** = exp_021_inference 的 gold-filtered 数量（全量 test set 37,648 行去除无 gold entity 的 instance）。这就是 `tab:fewnerd` 所用数据。
- **+0.30pp (τ=0.05)** 已经是基于 n=32,565 的 DALS gain，无需重新计算。来自 `dals_hardening_results.json`，bootstrap CI=[0.18, 0.42], p<0.001。
- **+1.08pp** 和 +0.30pp 差异的原因：
  1. **n_samples 不同**：n=16 vs n=8。更多样本→更低 degeneracy (4.5% vs 38.2%)→LP 区分度更高
  2. **数据集不同**：5K subsample vs 全量 32,565
- 论文 `tab:fewnerd` 对应的正确 DALS gain（n=32,565, τ=0.05, n_samples=8）：**+0.30pp**

---
