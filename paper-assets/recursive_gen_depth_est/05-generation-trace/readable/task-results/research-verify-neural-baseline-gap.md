# research verify neural baseline gap

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_neural_baseline_gap_20260523T003147_result.json`
- **Structured JSON:** [`75558ab1f3ee325e545e.json`](../../sessions/75/75558ab1f3ee325e545e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。

## DeBERTa "14--32pp" 声明验证结果

### 已有 per-cell DeBERTa 数据：仅 3/9 个 cell

| Cell | DeBERTa (mean) | RF (mean) | Matched Gap |
|------|----------------|-----------|-------------|
| Pythia nucleus | 58.31% | 78.70% | **20.4pp** |
| GPT-2 XL temp09 | 53.14% | 85.91% | **32.8pp** |
| Pythia temp09 | 60.57% | 76.79% | **16.2pp** |

RoBERTa 仅 1 个 cell：Pythia nucleus = 59.48%，gap = 19.2pp。

### 结论

- **实测 gap 范围：16--33pp**，与论文声称的 "14--32pp" 不符。
- 14pp 下界**不存在于任何 cell 的 mean accuracy 中**。唯一能得到 ~14pp 的方式是取 Pythia temp09 最佳单个 fold（62.4%）vs RF mean（76.79%）= 14.4pp，这混用了 best-fold 和 mean，方法学不一致。
- 32pp 上界近似成立（GPT-2 XL temp09 实测 32.8pp）。
- **6 个 cell 完全没有 DeBERTa 数据**（pythia_topk50, gpt2xl_nucleus, gpt2xl_topk50, olmo_nucleus, olmo_temp09, olmo_topk50），"per cell" 声明的覆盖率不足。

**建议**：将论文中 "14--32pp" 修正为 "16--33pp"（基于 cell mean），或标注仅覆盖 3/9 cells。

---

### 7B 实验进度

- **运行时长**：11h 42m
- **当前 Phase**：3.3b — 正在生成 d3（5000 samples with LoRA d2），模型权重已加载完毕，生成刚启动
- **剩余 Phases**：Phase 4（self-reference feature extraction）→ Phase 5（RF + LR classification）
- **预计剩余时间**：d3 生成 ~30-60min + Phase 4 ~30-60min + Phase 5 ~10-30min ≈ **1--2.5 小时**

---
