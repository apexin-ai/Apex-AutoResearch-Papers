# analysis batch completion check a

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_batch_completion_check_a_20260516T140049_result.json`
- **Structured JSON:** [`8fee08e2eb1f02017f1f.json`](../../sessions/8f/8fee08e2eb1f02017f1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 实验 | 状态 | 核心发现 |
|------|------|---------|
| **exp_022_seed789** | SUCCESS | 551行完整，NER ρ_sj=0.384，结构指标优于表面指标(+0.15)，RE 弱 |
| **exp_025_n32** | SUCCESS | 551行完整，N=32 使 NER ρ_sj 提升至 0.440（+15%），oracle headroom +51%，RE 仍不达标 |
| **exp_020_fewnerd_smoke** | INCOMPLETE | 训练到 step 5000/8236（60%）被中断，loss 从 0.96 降至 0.041，checkpoint-4000 可用(eval_loss=0.051) |

报告已写入 `artifacts/batch_completion_check_a.md`。

---
