# paper experiments draft

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiments-draft_20260515T143453_result.json`
- **Structured JSON:** [`37ac85dbbf383a85c0e6.json`](../../sessions/37/37ac85dbbf383a85c0e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/_project/paper/experiments.tex` 并注册。

结构和数据摘要：

**§4.1 Setup** — 数据集规模、模型配置、LoRA、seed/精度说明（789/0 NF4 已注明）、val-best checkpoint 协议、统计方法（clustered bootstrap + TOST）

**§4.2 Function-Level (Table 1)** — CLS 88.43±0.78 vs CWM 87.19±0.37 (gap 1.24pp, p=0.025)；TRAJ 86.30±0.97；ZS 8B 64.40% / 32B NF4 71.69%

**§4.3 Scaling (Table 2)** — 8B CLS 89.39 vs CWM 86.96 (gap 2.43pp, p=0.008)；CLS +0.96pp scaling gain, CWM −0.23pp；generation bottleneck 论证

**§4.4 CLS-TRAJ Equivalence** — gap −0.45pp, TOST p=0.007, ICC=0.191, DEFF=3.97；等价精度+免费诊断粒度

**§4.5 Oracle Frontier (Table 3)** — T=1 (69%) 无优势；T=2 (19%) block advantage 31.69pp, 55% contribution；P2P ~1% honest negative

**§4.6 Repo-Level (Table 4)** — 4B CLS 83.63% vs CWM 58.04% = 25.59pp (primary)；8B CLS 83.52/85.60% (secondary)；CWM 低于 majority baseline 14pp；unparseable 54-67%；8B-8B CWM 标 in progress

**§4.7 Analysis** — error complementarity (oracle 90.63%)、CWM 三类 error mode (77% token exhaustion / 23% ambiguous / hallucinated failures)、per-repo variation、seq_length ablation (drop 0.69pp)、LoRA rank ablation (−0.51pp)、ICC=0.191

---
