# analysis eval plan 012 dpo 1ep fixed r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_plan_012_dpo_1ep_fixed_r2_20260515T233756_result.json`
- **Structured JSON:** [`c559636da18a4672a4f7.json`](../../sessions/c5/c559636da18a4672a4f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 指标
- rel_f1: 0.4034
- ign_f1: 0.4034
- evi_f1 (conditional): 0.8088
- evi_f1 (joint): 0.3069
- EDCR: 0.7139
- precision: 0.3809
- recall: 0.4287
- wandb_run_id: 无（日志中未记录）

## 对比分析

| 方法 | rel_f1 | evi_f1 | EDCR |
|------|--------|--------|------|
| **DPO 1ep (本次)** | 0.4034 | 0.8088 | 0.7139 |
| SFT baseline | 0.4057 | 0.7979 | 0.7118 |
| DPO 3ep | 0.3429 | — | — |
| RSFT CED best (s44) | 0.4655 | 0.8087 | — |
| RSFT CED mean | ~0.4596 | — | — |
| CED reranker | 0.4864 | 0.8188 | — |

**vs SFT baseline**: rel_f1 下降 0.0023（-0.6%），本质持平。evi_f1 微升 +0.0109，EDCR 微升 +0.0021。DPO 1ep 没有提升关系抽取能力。

**vs DPO 3ep**: 1ep（0.4034）远优于 3ep（0.3429），确认 3ep 是过拟合。但 1ep 也只是回到 SFT 水平，说明 DPO 在早期就已无正向信号。

**vs RSFT methods**: 差距巨大。RSFT CED best 0.4655 比 DPO 1ep 高 +0.0621（+15.4%），CED reranker 0.4864 高 +0.0830（+20.6%）。

**Evidence decoupling**: 未出现明显 decoupling。evi_f1 从 0.7979→0.8088 微升，rel_f1 基本不变，DPO 对两个维度都没有产生有意义的影响。

## 结论建议
```
conclusion = negative
```
理由：DPO 1ep 的 rel_f1=0.4034 未超过 SFT baseline（0.4057），甚至略低。虽然避免了 3ep 的过拟合崩塌，但完全没有正向提升。与 RSFT 方法差距极大（15-20%），DPO 作为 offline preference optimization 在本任务上无效。

## DPO 论文定位建议

DPO 应作为**负面对比实验（negative baseline）**，用于论证：
1. **Offline preference optimization 不适用于 structured IE 任务** — DPO 的 pair-wise preference signal 在 CED（关系+证据联合生成）场景下无法提供有效梯度，1ep 即饱和、3ep 过拟合。
2. **凸显 RSFT/Reranker 路线的优势** — 相比 DPO 的 0.4034，RSFT CED（0.4655）和 CED reranker（0.4864）显著有效，说明在 structured output 场景下，rejection sampling + 正例强化比 pair-wise preference 更合适。
3. 在论文中用一段话+一行表格数据带过即可，不必详细展开 DPO 消融。核心 message：**"We also explored DPO but found it ineffective for joint relation-evidence extraction (F1=0.40 vs. SFT 0.41), confirming that pair-wise preference signals are insufficient for structured generation tasks with compositional outputs."**

---
