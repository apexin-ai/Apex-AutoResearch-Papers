# analysis method ablation mvp

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_method-ablation-mvp_20260514T195856_result.json`
- **Structured JSON:** [`eef0611cca7c390b0d48.json`](../../sessions/ee/eef0611cca7c390b0d48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存（2933 行）。

---

## 方法论 Ablation 结果

### 四方法对比表

| Canary | Downstream | Naive | Diff(Δ) | Thresh(2σ) | Toda-Yamamoto | Spurious? |
|---|---|---|---|---|---|---|
| token_entropy | perplexity | SIG | SIG | SIG | n.s. | **YES** |
| token_entropy | distinct_1 | SIG | SIG | SIG | **SIG** | |
| token_entropy | distinct_2 | SIG | SIG | SIG | **SIG** | |
| token_entropy | distinct_3 | SIG | SIG | SIG | **SIG** | |
| self_bleu | perplexity | SIG | n.s. | SIG | n.s. | **YES** |
| self_bleu | distinct_1 | SIG | n.s. | n.s. | n.s. | **YES** |
| self_bleu | distinct_2 | SIG | SIG | n.s. | n.s. | **YES** |
| self_bleu | distinct_3 | SIG | SIG | n.s. | n.s. | **YES** |
| ece | perplexity | SIG | SIG | SIG | n.s. | **YES** |
| ece | distinct_1 | SIG | SIG | SIG | **SIG** | |
| ece | distinct_2 | SIG | SIG | SIG | n.s. | **YES** |
| ece | distinct_3 | SIG | SIG | SIG | n.s. | **YES** |
| effective_rank | perplexity | SIG | SIG | n.s. | n.s. | **YES** |
| effective_rank | distinct_1 | SIG | SIG | n.s. | n.s. | **YES** |
| effective_rank | distinct_2 | SIG | SIG | n.s. | n.s. | **YES** |
| effective_rank | distinct_3 | SIG | SIG | n.s. | n.s. | **YES** |

### 汇总

| 方法 | 显著 pair 数 |
|---|---|
| Naive Pearson (raw levels) | **16/16** (100%) |
| Differenced xcorr (Δ) | 14/16 (87.5%) |
| Threshold onset (2σ) | 9/16 (56.3%) |
| Toda-Yamamoto Granger | **4/16** (25%) |

### 核心发现

**伪回归率 = 75%**（12/16 naive 显著但 TY 不显著），远超 30% 阈值 → **Claim 3 强成立**。

**仅 4 个 pair 通过最严格检验（Robust）：**
1. **token_entropy → distinct_1/2/3** — 全 4 seed 均 p<0.001，F 值 100-550，因果关系确凿
2. **ece → distinct_1** — 3/4 seed 显著（seed 44 是唯一例外，F=2.74）

**关键结论：**
- **token_entropy 是唯一 gold-standard canary** — 对三个 diversity 指标都有真实的 Granger 因果预测力
- **perplexity 作为 downstream 全军覆没** — 与所有 canary 的相关性都是非平稳驱动的伪回归
- **self_bleu 和 effective_rank 作为 canary 完全失效** — 无真实预测力
- **ece 部分有效** — 仅对 distinct_1 有因果预测力

产出文件：
- 脚本：`/root/autodl-tmp/distrib_canary_collapse/method_ablation.py`
- 数据：`results/mvp/analysis/method_ablation.json`

---
