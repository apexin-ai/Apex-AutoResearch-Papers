# code ablation latex table

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation-latex-table_20260524T232728_result.json`
- **Structured JSON:** [`4d376554e953f442f39b.json`](../../sessions/4d/4d376554e953f442f39b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 LaTeX 表格已生成并注册：

**Table A** (`ablation_mechanism_table.tex`) — CIVO 机制证据汇总，7 行数据：
- dt_emb cosine: trained $-0.94{\sim}-0.70$ vs frozen $-0.15{\sim}+0.07$ (exp_065)
- RSSM fidelity: reward MAE gap $2.695\times$ vs baseline $1.483\times$ (exp_063)
- Value calibration: V/MC median $3.40$ vs control $1.05$ (exp_064)
- NVE: AUROC $0.961$, F1@1.5x $= 0.880$

**Table B** (`temporal_causality_table.tex`) — 时序因果关系：
- Return crash 60-80K → entropy rise 95K+，lag 15-35K steps
- Entropy drift rate $1.14{-}2.11$ nats/10K (collapsed) vs $0.07{-}0.22$ (healthy)，$10{-}20\times$ 差异

每个数字均在 footnote 中标注了来源实验 ID。Paper Agent 可直接 `\input{tables/ablation_mechanism_table.tex}` 引用。

---
