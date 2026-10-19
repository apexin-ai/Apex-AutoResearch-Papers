# research tost bayesian equivalence

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tost-bayesian-equivalence_20260524T170140_result.json`
- **Structured JSON:** [`b3a612dde80fae04b0c4.json`](../../sessions/b3/b3a612dde80fae04b0c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已执行完毕，结果已保存。汇报如下：

---

```
TOST Power Analysis:
  Llama (margin=±2pp):  power=0.014, TOST p=0.424 → fail to reject (insufficient)
  Llama (margin=±5pp):  power=0.103, TOST p=0.180 → fail to reject (insufficient)
  Llama (margin=±10pp): power=0.584, TOST p=0.017 → reject H0 (but power still insufficient)
  Qwen  (margin=±2pp):  power=0.014, TOST p=0.367 → fail to reject (insufficient)
  Qwen  (margin=±5pp):  power=0.092, TOST p=0.154 → fail to reject (insufficient)
  Qwen  (margin=±10pp): power=0.534, TOST p=0.016 → reject H0 (but power still insufficient)
  Margin needed for power=0.80: Llama ±12.3pp, Qwen ±12.8pp

Bayesian Equivalence (prior_scale=5pp):
  Llama: diff=1.2pp, BF01=1.53, anecdotal evidence for equivalence
  Qwen:  diff=0.5pp, BF01=1.51, anecdotal evidence for equivalence

Bayesian Equivalence (prior_scale=10pp):
  Llama: diff=1.2pp, BF01=2.52, anecdotal evidence for equivalence
  Qwen:  diff=0.5pp, BF01=2.46, anecdotal evidence for equivalence
```

**结论：** 两类分析给出互补但一致的图景。TOST 分析表明，由于 SE 较大（~4.1–4.4pp，源于 bootstrap CI 宽度），在严格的等价边界（±2–5pp）下统计功效严重不足（power < 0.11），无法通过 TOST 正式证明等价性；需要放宽到 ±10pp 才能在 α=0.05 下拒绝非等价 H0（p≈0.016），达到 80% power 则需 ±12–13pp 的边界。Bayesian 分析方向一致：所有 BF01 均 >1（1.2–2.5），数据一致地轻微偏向等价假说而非差异假说，但证据强度仅为 anecdotal（未达 BF01>3 的 moderate 阈值）。综合来看，**现有数据与 "asymmetry 非 conflict-specific" 的 claim 方向一致（两个差异仅 0.5–1.2pp），但样本量不足以提供统计上确凿的等价性证据**。论文中应诚实报告这一点：CI 重叠和小差异提供 suggestive evidence，TOST 功效不足是 limitation，Bayesian BF01>1 支持等价方向但证据强度有限。

---
