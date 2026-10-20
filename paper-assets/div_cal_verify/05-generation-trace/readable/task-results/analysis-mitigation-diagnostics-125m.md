# analysis mitigation diagnostics 125m

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mitigation_diagnostics_125m_20260514T122933_result.json`
- **Structured JSON:** [`e6ff80946d7f33fe4c8e.json`](../../sessions/e6/e6ff80946d7f33fe4c8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项分析全部完成。汇总结果：

---

## 分析 1: 近重复度分析 (Contriever embeddings)

```
Gen 1: N=977
  Sim dist: min=-0.002 P25=0.187 median=0.218 P75=0.251 P95=0.308 max=1.000
  ε=0.95: 14/977 (1.4%) near-duplicates
  ε=0.90: 19/977 (1.9%)
  ε=0.85: 29/977 (3.0%)

Gen 4: N=977
  ε=0.95: 19/977 (1.9%)
  ε=0.90: 39/977 (4.0%)
  ε=0.85: 47/977 (4.8%)

Gen 7: N=977
  ε=0.95: 22/977 (2.3%)
  ε=0.90: 40/977 (4.1%)
  ε=0.85: 54/977 (5.5%)
```

**结论：ADR/SemDeDup 去重空间很小。** 即使在最宽松阈值 ε=0.70，Gen 7 也只有 8.9% 近重复。近重复比例随代数略增（1.4%→2.3% at ε=0.95），但绝对数量太少，去重无法显著缓解 collapse。

---

## 分析 2: Gen-0 PPL 分布

```
Gen 1: N=977
  Mean=2.0, Median=1.8, P10=1.3, P25=1.5, P75=2.2, P90=2.8, P95=3.2, P99=4.4

Gen 4: N=977
  Mean=1.4, Median=1.4, P10=1.2, P25=1.3, P75=1.5, P90=1.7, P95=1.8, P99=2.1

Gen 7: N=977
  Mean=1.4, Median=1.4, P10=1.2, P25=1.3, P75=1.5, P90=1.8, P95=1.9, P99=2.1

分布漂移：
  Gen1→Gen4: mean shift -0.5, KS stat=0.492 (p=0.0000)
  Gen4→Gen7: mean shift -0.0, KS stat=0.089 (p=0.0009)

高 PPL 尾部样本（Gen 7, P95+）:
  [PPL=2.1] 正常 Wikipedia 风格文本
  [PPL=2.2] 公式重复退化文本（E°(No3+→No2+) 循环重复）
```

**结论：RPF 过滤信号极弱。** PPL 分布极度压缩（Gen 4/7 的 mean=1.4，P99 仅 2.1），说明合成数据已经高度"模板化"——Gen-0 模型对这些文本几乎完全确定。分布太窄，无法用 PPL 阈值有效区分"好"与"退化"样本。唯一的例外是极少数公式循环样本。

---

## 分析 3: RGDS 选中 vs 拒绝 PPL 对比

```
Gen 4:
  Selected  (N=488): mean PPL=1.30, median=1.30, P90=1.50
  Rejected  (N=489): mean PPL=1.50, median=1.50, P90=1.80
  差异: selected mean - rejected mean = -0.20
  t-test: t=-17.40, p=0.0000
  Cohen's d: -1.11

Gen 7:
  Selected  (N=488): mean PPL=1.20, median=1.20, P90=1.30
  Rejected  (N=489): mean PPL=1.30, median=1.30, P90=1.60
  差异: selected mean - rejected mean = -0.20
  t-test: t=-14.66, p=0.0000
  Cohen's d: -0.94
```

**结论：RGDS 系统性地选择低 PPL（更模板化）样本，而非高 PPL 样本。** Cohen's d 达到 -1.11（大效应量），方向与预期相反——RGDS 的 diversity selection 反而偏好 Gen-0 模型最确定的文本。这解释了 RGDS 为什么无法缓解 collapse：它选的是分布最集中的部分，加速而非抑制了模式坍缩。

---
