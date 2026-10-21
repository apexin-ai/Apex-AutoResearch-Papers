# analysis alpha sweep a025 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a025_s43_20260515T173716_result.json`
- **Structured JSON:** [`cf1652237bb4753c541c.json`](../../sessions/cf/cf1652237bb4753c541c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

---

## 1. Gen 0–10 完整指标表

| Gen | token_entropy | ECE | perplexity | distinct_1 | distinct_2 | distinct_3 | eff_rank | mauve |
|-----|-------------|-------|-----------|-----------|-----------|-----------|---------|-------|
| 0 | 3.2342 | 0.0108 | 26.949 | 0.0983 | 0.5132 | 0.8057 | 46.61 | 0.0335 |
| 1 | 2.9953 | 0.0077 | 19.455 | 0.0996 | 0.5177 | 0.8097 | 49.63 | 0.0299 |
| 2 | 3.0369 | 0.0101 | 20.217 | 0.0807 | 0.4267 | 0.7109 | 49.98 | 0.0330 |
| 3 | 3.0516 | 0.0094 | 20.710 | 0.0725 | 0.3701 | 0.6219 | 50.41 | 0.0315 |
| 4 | 3.0337 | 0.0144 | 20.920 | 0.0664 | 0.3131 | 0.5166 | 50.44 | 0.0272 |
| 5 | 3.0467 | 0.0155 | 21.116 | 0.0640 | 0.2858 | 0.4653 | 49.59 | 0.0242 |
| 6 | 3.0428 | 0.0188 | 21.478 | 0.0621 | 0.2636 | 0.4179 | 49.67 | 0.0219 |
| 7 | 3.0554 | 0.0184 | 21.671 | 0.0611 | 0.2540 | 0.3976 | 47.47 | 0.0226 |
| 8 | 3.0878 | 0.0185 | 21.923 | 0.0597 | 0.2389 | 0.3647 | 47.07 | 0.0194 |
| 9 | 3.0691 | 0.0203 | 21.845 | 0.0593 | 0.2317 | 0.3476 | 45.61 | 0.0193 |
| 10 | 3.0723 | 0.0215 | 21.899 | 0.0585 | 0.2236 | 0.3330 | 45.37 | 0.0187 |

## 2. Seed=42 vs Seed=43 对比

| Metric | seed=42 drift | seed=43 drift | 比值 (43/42) |
|--------|-------------|-------------|------------|
| token_entropy | **-4.1%** | **-5.0%** | 1.22x |
| ECE | **+79.7%** | **+98.6%** | 1.24x |
| perplexity | **-17.2%** | **-18.7%** | 1.09x |
| distinct_1 | **-40.3%** | **-40.5%** | 1.00x |
| distinct_2 | **-57.1%** | **-56.4%** | 0.99x |
| distinct_3 | **-59.9%** | **-58.7%** | 0.98x |

## 3. Conclusion: **success**

所有 6 项指标 drift 方向完全一致（entropy↓、ECE↑、perplexity↓、diversity 三指标↓）。diversity 三指标幅度几乎完全复现（偏差 <2%）。entropy 和 ECE 的幅度 seed=43 略大（~22-24%），但均在 ±50% 判定阈值以内。perplexity drift 也高度吻合（偏差 9%）。

α=0.25 低污染设置下的温和 collapse 模式在 seed=43 上完全复现。无 lead-lag 分析结果（本次 run 未包含 Granger/TY 检验）。

---
