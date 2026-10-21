# analysis r5 ablation results

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r5_ablation_results_20260516T182640_result.json`
- **Structured JSON:** [`dbc065efc8e20aed9def.json`](../../sessions/db/dbc065efc8e20aed9def.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验 registry 已更新完毕。

---

## 结果汇总

| 实验 | 状态 | 结论 | 关键指标 |
|------|------|------|----------|
| **lora_rank_ablation_001** | DONE | **success** | rank_4=0.718, **rank_16=0.7645**, rank_64=0.731 (倒U型趋势，rank=16最优，AUC=0.8434) |
| **gpt2xl_ref_ablation_001** | DONE | **negative** | GPT-2 XL ref=0.6734 vs Pythia ref=0.7854, Δ=-11.2pp (远超±5pp阈值) |

**关键发现：**
- LoRA rank 有明确影响：rank=16 是甜点，过小(4)欠拟合，过大(64)略有过拟合。top features 在所有 rank 上一致（var_surprisal, p90_ppl 为主导）。
- Reference model 选择显著影响 depth signal 提取：matched-architecture (Pythia) 比 cross-architecture (GPT-2 XL) 高 11.2pp，说明 depth signal 不是纯统计现象，需要架构匹配的 reference model。

---
